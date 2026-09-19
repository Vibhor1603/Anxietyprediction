# Anxiety Prediction App

Upload a short video → get movement metrics + anxiety prediction.

Repo: https://github.com/Vibhor1603/Anxietyprediction

---

## What you need

- A computer (Mac or Windows)
- Internet (first time only)
- About 15 minutes

---

## Step 1 — Download the project

1. Open https://github.com/Vibhor1603/Anxietyprediction in your browser
2. Click the green **Code** button
3. Click **Download ZIP**
4. Unzip the file (Mac: double-click · Windows: right-click → **Extract All**)
5. You should see a folder with `app.py` inside

---

## Step 2 — Install Python 3.11

1. Open https://www.python.org/downloads/release/python-3119/
2. Download the installer for your computer:
   - **Mac:** macOS 64-bit universal2 installer
   - **Windows:** Windows installer (64-bit)
3. Run the installer
4. **Windows only:** tick **Add python.exe to PATH** before clicking Install
5. Finish install, then close and reopen any terminal windows

---

## Step 3 — Open Terminal in the project folder

### Mac

1. Press `Cmd + Space`, type **Terminal**, press Enter
2. Copy this, paste into Terminal, press Enter  
   (change the path if your folder is somewhere else)

```bash
cd ~/Downloads/Anxietyprediction-main
```

3. Check you are in the right place — copy, paste, Enter:

```bash
ls
```

You should see `app.py` in the list.

### Windows

1. Press the Windows key, type **cmd**, open **Command Prompt**
2. Copy this, paste, press Enter  
   (change the path if your folder is somewhere else)

```bat
cd %USERPROFILE%\Downloads\Anxietyprediction-main
```

3. Check you are in the right place — copy, paste, Enter:

```bat
dir
```

You should see `app.py` in the list.

---

## Step 4 — Create the environment (one time)

### Mac — copy each line, paste, press Enter

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

You should now see `(venv)` at the start of the line.

```bash
pip install -r requirements.txt
```

Wait until it finishes.

### Windows — copy each line, paste, press Enter

```bat
python -m venv venv
```

```bat
venv\Scripts\activate
```

You should now see `(venv)` at the start of the line.

```bat
pip install -r requirements.txt
```

Wait until it finishes.

---

## Step 5 — Start the app

With `(venv)` still showing, copy, paste, Enter:

```bash
streamlit run app.py
```

1. Wait a few seconds
2. Open your browser and go to: **http://localhost:8501**
3. Click **Upload Video** → choose a short `.mp4` → click **Analyze Video**

To stop the app later: click the Terminal / Command Prompt window and press **Ctrl + C**.

---

## Next time you want to run it

Open Terminal / Command Prompt again, then:

### Mac

```bash
cd ~/Downloads/Anxietyprediction-main
source venv/bin/activate
streamlit run app.py
```

### Windows

```bat
cd %USERPROFILE%\Downloads\Anxietyprediction-main
venv\Scripts\activate
streamlit run app.py
```

Then open **http://localhost:8501**.

---

## For developers — what’s in this project

| Item | Details |
|------|---------|
| Language | Python 3.11 |
| UI | Streamlit (`app.py`) |
| Video analysis | OpenCV (`movement_analysis.py`, files in `cascades/`) |
| ML model | scikit-learn (`anxiety_model.pkl`) |
| Data libs | pandas, numpy |
| Install list | `requirements.txt` |
| Train script | `TrainData.py` |
