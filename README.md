---
title: Pediatric Anxiety Prediction
emoji: 🎬
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: 1.42.0
app_file: app.py
pinned: false
license: mit
short_description: Upload a video to analyze movement and predict anxiety risk
---

# Pediatric Movement Analysis & Anxiety Prediction

Upload a short video to extract movement metrics (blinks, head/body movement) and get an anxiety risk prediction.

## How to use

1. Click **Upload Video** (mp4 / avi / mov)
2. Click **Analyze Video**
3. View movement metrics and the predicted anxiety level

## Run locally

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

App opens at http://localhost:8501
