# Pediatric Movement Analysis & Anxiety Prediction

Upload a short video to extract movement metrics (blinks, head/body movement) and get an anxiety risk prediction.

**GitHub:** https://github.com/Vibhor1603/Anxietyprediction

---

## What this project does

- Accepts a video upload (`.mp4`, `.avi`, `.mov`)
- Analyzes face, eye blinks, head movement, and body movement with OpenCV
- Saves metrics to a CSV file
- Predicts anxiety level using a trained scikit-learn model

**Tip:** Use a short video (10–30 seconds) when testing.

---

## Tech stack (for developers)

- **Language:** Python 3.11 (recommended; avoid 3.14)
- **UI:** Streamlit
- **Vision:** OpenCV (`opencv-python-headless`) + Haar cascades in `cascades/`
- **Data:** pandas, numpy
- **ML:** scikit-learn model in `anxiety_model.pkl`
- **Main entry file:** `app.py`
- **Core analysis:** `movement_analysis.py`
- **Dependencies:** `requirements.txt`
- **Optional hosting configs:** `render.yaml`, `Dockerfile`, `.streamlit/config.toml`

---

## Important files

- `app.py` — Streamlit web app
- `movement_analysis.py` — video analysis logic
- `anxiety_model.pkl` — trained anxiety prediction model
- `cascades/` — face and eye detection XML files
- `requirements.txt` — Python packages to install
- `TrainData.py` — model training script (research / offline use)

---

## Setup on a fresh computer

### 1. Get the code

- Open https://github.com/Vibhor1603/Anxietyprediction
- Click **Code** → **Download ZIP**
- Unzip the folder
- Or with Git:

```bash
git clone https://github.com/Vibhor1603/Anxietyprediction.git
cd Anxietyprediction
```

### 2. Install Python 3.11

- Download: https://www.python.org/downloads/release/python-3119/
- **Windows:** run the installer and check **Add python.exe to PATH**
- **Mac:** install the macOS `.pkg`, then reopen Terminal
- Check version:

```bash
python --version
# or
python3 --version
```

### 3. Create a virtual environment

**Mac / Linux**

```bash
cd Anxietyprediction
python3.11 -m venv venv
source venv/bin/activate
```

**Windows (Command Prompt)**

```bat
cd Anxietyprediction
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` at the start of the terminal line.

### 4. Install packages

```bash
pip install -r requirements.txt
```

### 5. Run the app

```bash
streamlit run app.py
```

- Open http://localhost:8501 in your browser
- Upload a video → click **Analyze Video**
- Stop the app later with `Ctrl + C` in the terminal

### 6. Next time (after first setup)

**Mac / Linux**

```bash
cd Anxietyprediction
source venv/bin/activate
streamlit run app.py
```

**Windows**

```bat
cd Anxietyprediction
venv\Scripts\activate
streamlit run app.py
```

---

## How to use the app

- Click **Upload Video**
- Choose an `.mp4` / `.avi` / `.mov` file
- Click **Analyze Video**
- View movement metrics and anxiety prediction
- Optionally download the CSV

---

## Common problems

- **`python` not found** — reinstall Python 3.11; on Windows enable **Add to PATH**
- **`streamlit` not found** — activate `venv` first, then run again
- **Wrong folder** — make sure `app.py` is in the current folder (`ls` on Mac, `dir` on Windows)
- **Analysis slow** — use a shorter video; local computer is faster than free cloud hosting
- **Missing model / cascades** — confirm `anxiety_model.pkl` and the `cascades/` folder exist

---

## Hosting notes

- Free cloud hosts (Render free tier) have **512MB RAM** and may crash on longer videos
- Best results for real analysis: run **locally** on your computer
- Live demo URL (if deployed): check your Render / Streamlit Cloud dashboard
