---
title: Pediatric Anxiety Prediction
emoji: 🎬
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false
license: mit
short_description: Upload a video to analyze movement and predict anxiety risk
---

# Pediatric Movement Analysis & Anxiety Prediction

Upload a short video to extract movement metrics (blinks, head/body movement) and get an anxiety risk prediction.

## How to use the app

1. Click **Upload Video** (mp4 / avi / mov)
2. Click **Analyze Video**
3. View movement metrics and the predicted anxiety level

## Install on your own computer (Mac or Windows)

**Follow the beginner setup guide:**

### 👉 [SETUP.md](./SETUP.md)

That guide explains every step for Mac and Windows, including installing Python, even if you are not technical.

### Quick start (if you already know Python)

```bash
# 1. Open the project folder
cd Anxietyprediction

# 2. Create and activate a virtual environment (Python 3.11 recommended)
python3.11 -m venv venv          # Mac/Linux
# python -m venv venv            # Windows

source venv/bin/activate           # Mac/Linux
# venv\Scripts\activate          # Windows

# 3. Install packages
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

Then open **http://localhost:8501** in your browser.

## Project link

GitHub: https://github.com/Vibhor1603/Anxietyprediction
