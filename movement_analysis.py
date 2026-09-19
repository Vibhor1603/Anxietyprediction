"""
AI-Based Movement Analysis for Pediatric Dentistry Study

Tracks:
1. Eye Blink Frequency
2. Head Movement
3. Facial Movement
4. Hand Movement
5. Body Movement

Output:
CSV file containing movement metrics.

Author: Research Prototype
Modified: Works with OpenCV (compatible with all MediaPipe versions)
"""

import pandas as pd
import numpy as np
from math import sqrt
import os
import site
import urllib.request

try:
    import cv2
except ImportError as exc:  # pragma: no cover - environment/setup issue
    cv2 = None
    _CV2_IMPORT_ERROR = exc
else:
    _CV2_IMPORT_ERROR = None


def _require_cv2():
    """Fail with a clear message if OpenCV is not installed."""
    if cv2 is None:
        raise ImportError(
            "OpenCV (cv2) is not installed in this environment. "
            "On Streamlit Cloud: App settings → Python version → 3.11 → Reboot. "
            "Or delete the app and create it again with Advanced settings → Python 3.11. "
            f"Original error: {_CV2_IMPORT_ERROR}"
        )
    return cv2


# -----------------------------------------
# LOAD CASCADE CLASSIFIERS
# -----------------------------------------

def _load_cascade(name):
    """Locate and load an OpenCV Haar cascade, with fallbacks for
    environments where cv2.data.haarcascades is missing or incomplete
    (common on Streamlit Cloud / some opencv-python-headless builds).
    """
    cv2_mod = _require_cv2()

    # 1) Project-local cascades/ folder (most reliable for hosting)
    local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cascades", name)
    if os.path.exists(local_path):
        return cv2_mod.CascadeClassifier(local_path)

    # 2) Try cv2.data (modern OpenCV)
    try:
        path = os.path.join(cv2_mod.data.haarcascades, name)
        if os.path.exists(path):
            return cv2_mod.CascadeClassifier(path)
    except AttributeError:
        pass

    # 3) Search common site-packages locations
    search_roots = []
    try:
        search_roots.extend(site.getsitepackages())
    except Exception:
        pass
    try:
        search_roots.append(site.getusersitepackages())
    except Exception:
        pass
    if hasattr(cv2_mod, "__file__") and cv2_mod.__file__:
        search_roots.append(os.path.dirname(cv2_mod.__file__))

    for dir_ in search_roots:
        for candidate in (
            os.path.join(dir_, "cv2", "data", name),
            os.path.join(dir_, "data", name),
        ):
            if os.path.exists(candidate):
                return cv2_mod.CascadeClassifier(candidate)

    # 4) Last resort – download from OpenCV's GitHub
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    url = (
        "https://raw.githubusercontent.com/opencv/opencv/"
        f"master/data/haarcascades/{name}"
    )
    urllib.request.urlretrieve(url, local_path)
    return cv2_mod.CascadeClassifier(local_path)


_face_cascade = None
_eye_cascade = None


def _get_cascades():
    """Lazy-load cascades so the Streamlit UI can start even if OpenCV is missing."""
    global _face_cascade, _eye_cascade
    _require_cv2()
    if _face_cascade is None:
        _face_cascade = _load_cascade("haarcascade_frontalface_default.xml")
        _eye_cascade = _load_cascade("haarcascade_eye.xml")
    return _face_cascade, _eye_cascade

# -----------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------

def euclidean(p1, p2):
    """Calculate Euclidean distance between two points"""
    return sqrt(
        (p1[0] - p2[0])**2 +
        (p1[1] - p2[1])**2
    )

def get_center(x, y, w, h):
    """Get center point of a bounding box"""
    return (x + w//2, y + h//2)

# -----------------------------------------
# MAIN ANALYSIS FUNCTION
# -----------------------------------------

def analyze_video(video_path):
    """
    Analyze a video file and extract movement metrics.
    
    Args:
        video_path (str): Path to the video file
        
    Returns:
        str: Path to the output CSV file with movement metrics
        
    Raises:
        FileNotFoundError: If video file doesn't exist
        IOError: If video cannot be opened
    """
    
    # Check if video file exists
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file '{video_path}' not found.")

    cv2_mod = _require_cv2()
    face_cascade, eye_cascade = _get_cascades()
    
    cap = cv2_mod.VideoCapture(video_path)
    
    if not cap.isOpened():
        raise IOError(f"Cannot open video file '{video_path}'")

    # Read FPS once from the same capture (avoid opening the video twice)
    actual_fps = cap.get(cv2_mod.CAP_PROP_FPS)
    fps = actual_fps if actual_fps and actual_fps > 0 else 30
    
    # -----------------------------------------
    # VARIABLES FOR METRICS
    # -----------------------------------------
    
    frame_count = 0
    eye_blinks = 0
    previous_eye_distance = None
    head_movements = 0
    previous_face_center = None
    body_movements = 0
    # Only last 3 face areas are used for body-movement variance
    face_area_history = []
    
    # -----------------------------------------
    # PROCESS VIDEO
    # -----------------------------------------
    
    print("Processing video...")
    
    while cap.isOpened():
        success, frame = cap.read()
        
        if not success:
            break
        
        frame_count += 1
        
        # Show progress every 30 frames
        if frame_count % 30 == 0:
            print(f"Frame {frame_count}...", end='\r')
        
        gray = cv2_mod.cvtColor(frame, cv2_mod.COLOR_BGR2GRAY)
        # Release BGR frame early — only grayscale is needed after this
        del frame
        
        # ---------------------------------
        # FACE ANALYSIS
        # ---------------------------------
        
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        if len(faces) > 0:
            # Get the largest face (assuming main subject)
            largest_face = max(faces, key=lambda f: f[2] * f[3])
            x, y, fw, fh = largest_face
            
            # Calculate face center
            face_center = get_center(x, y, fw, fh)
            
            # HEAD MOVEMENT
            if previous_face_center is not None:
                movement = euclidean(face_center, previous_face_center)
                if movement > 10:
                    head_movements += 1
            
            previous_face_center = face_center
            
            # BLINK DETECTION - detect eyes within face
            roi_gray = gray[y:y+fh, x:x+fw]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            
            if len(eyes) >= 2:
                # Get top 2 eyes (likely left and right eyes)
                eyes = sorted(eyes, key=lambda e: e[1])[:2]
                
                # Calculate average eye vertical distance
                eye_distances = []
                for (ex, ey, ew, eh) in eyes:
                    eye_distance = eh  # Vertical height of eye
                    eye_distances.append(eye_distance)
                
                avg_eye_distance = np.mean(eye_distances) if eye_distances else 0
                
                # BLINK DETECTION
                if previous_eye_distance is not None:
                    # Blink detected when eye distance drops significantly
                    if avg_eye_distance < previous_eye_distance * 0.5 and previous_eye_distance > 5:
                        eye_blinks += 1
                
                previous_eye_distance = avg_eye_distance

            # BODY/FACIAL MOVEMENT (face area variation over last 3 frames)
            face_area_history.append(fw * fh)
            if len(face_area_history) > 3:
                face_area_history.pop(0)

            if len(face_area_history) > 2:
                area_variance = np.var(face_area_history)
                if area_variance > 5000:
                    body_movements += 1

        # Free per-frame buffers before the next iteration
        del gray
        
    # -----------------------------------------
    # RELEASE VIDEO
    # -----------------------------------------
    
    cap.release()
    # Safe cleanup for headless environments (Streamlit Cloud)
    try:
        if hasattr(cv2_mod, "destroyAllWindows"):
            cv2_mod.destroyAllWindows()
    except Exception:
        pass
    
    # -----------------------------------------
    # CALCULATE METRICS
    # -----------------------------------------
    
    duration_seconds = frame_count / fps
    duration_minutes = duration_seconds / 60
    
    # Calculate blink rate (per minute)
    if duration_minutes > 0:
        blink_rate = eye_blinks / duration_minutes
    else:
        blink_rate = 0
    
    # -----------------------------------------
    # CREATE OUTPUT DATASET
    # -----------------------------------------
    
    results = pd.DataFrame({
        "Frame_Count": [frame_count],
        "Duration_Seconds": [duration_seconds],
        "Duration_Minutes": [duration_minutes],
        "Eye_Blinks": [eye_blinks],
        "Blink_Rate_Per_Minute": [blink_rate],
        "Head_Movements": [head_movements],
        # Hand movement metric removed
        "Body_Movements": [body_movements]
    })
    
    # -----------------------------------------
    # CREATE OUTPUT DIRECTORY
    # -----------------------------------------
    
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # -----------------------------------------
    # SAVE CSV
    # -----------------------------------------
    
    output_path = os.path.join(output_dir, "movement_data.csv")
    results.to_csv(output_path, index=False)
    
    print("\n" + "="*50)
    print("Analysis Complete!")
    print("="*50)
    print(results.to_string(index=False))
    
    return output_path
