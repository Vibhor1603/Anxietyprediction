# Setup Guide — Run This App on Your Computer

This guide is written for **beginners**.  
You do **not** need to know Python. Follow the steps **in order**, exactly as written.

When you finish, the app will open in your web browser. You can upload a video and get movement + anxiety results.

---

## What this app does (in plain words)

1. You upload a short video (`.mp4`, `.avi`, or `.mov`).
2. The app looks at face / eye / head / body movement in the video.
3. It shows numbers (blinks, movements) and an anxiety prediction.

**Tip:** Start with a **short** video (10–30 seconds). Longer videos take more time.

---

## Before you start — checklist

You need:

- A computer with **Windows 10/11** or **macOS**
- Internet connection (only for the first install)
- About **15–20 minutes** the first time
- This project folder on your computer (see Part A below)

---

# Part A — Get the project onto your computer

Pick **one** method.

### Option 1 (easiest) — Download as ZIP

1. Open this page in your browser:  
   **https://github.com/Vibhor1603/Anxietyprediction**
2. Click the green **Code** button.
3. Click **Download ZIP**.
4. Find the downloaded ZIP file (usually in your **Downloads** folder).
5. **Unzip / Extract** it:
   - **Windows:** Right‑click the ZIP → **Extract All…** → Extract
   - **Mac:** Double‑click the ZIP
6. You should now have a folder named something like **`Anxietyprediction-main`**.  
   Rename it to **`Anxietyprediction`** if you want (optional).
7. Remember where this folder is (example: `Downloads/Anxietyprediction`).

### Option 2 — Using Git (only if you already use Git)

```bash
git clone https://github.com/Vibhor1603/Anxietyprediction.git
cd Anxietyprediction
```

---

# Part B — Install Python (one-time)

This app needs **Python 3.11** (recommended).  
**Avoid Python 3.14** for this project — some packages may fail.

---

## B1. Mac setup

### Step 1 — Check if Python is already installed

1. Open **Terminal** (press `Cmd + Space`, type `Terminal`, press Enter).
2. Copy and paste this, then press Enter:

```bash
python3 --version
```

- If you see something like `Python 3.11.x` → good, go to **Part C (Mac)**.
- If you see `3.12` or `3.13` → usually OK, continue.
- If you see `3.14` or an error → install Python 3.11 below.

### Step 2 — Install Python 3.11 on Mac

1. Open: **https://www.python.org/downloads/release/python-3119/**
2. Scroll to **Files**.
3. Download **macOS 64-bit universal2 installer**.
4. Open the downloaded `.pkg` file and click through **Continue / Install**.
5. When finished, **quit and reopen Terminal**.
6. Check again:

```bash
python3.11 --version
```

You want to see `Python 3.11.x`.

---

## B2. Windows setup

### Step 1 — Install Python 3.11

1. Open: **https://www.python.org/downloads/release/python-3119/**
2. Scroll to **Files**.
3. Download **Windows installer (64-bit)**.
4. Run the installer.
5. **IMPORTANT:** On the first screen, check the box  
   **“Add python.exe to PATH”**  
   (bottom of the window).
6. Click **Install Now**.
7. When it finishes, click **Close**.

### Step 2 — Check that Python works

1. Press the **Windows** key, type **`cmd`**, open **Command Prompt**.
2. Paste this and press Enter:

```bat
python --version
```

You should see something like `Python 3.11.x`.

If you get `'python' is not recognized`:

- Reinstall Python and make sure **Add to PATH** is checked, **or**
- Try:

```bat
py -3.11 --version
```

If `py -3.11` works, use `py -3.11` instead of `python` in later steps.

---

# Part C — Install the app (one-time)

You will:

1. Open a terminal **inside** the project folder  
2. Create a private “toolbox” folder (`venv`)  
3. Install the required packages  

This only needs to be done **once** per computer.

---

## C1. Mac — install steps

### Step 1 — Go into the project folder

In Terminal:

```bash
cd ~/Downloads/Anxietyprediction
```

> If your folder is somewhere else, change the path.  
> Example: `cd ~/Desktop/Anxietyprediction`  
> Example if ZIP kept the `-main` name: `cd ~/Downloads/Anxietyprediction-main`

Check you are in the right place:

```bash
ls
```

You should see files like `app.py`, `requirements.txt`, `anxiety_model.pkl`.

### Step 2 — Create the virtual environment

Prefer Python 3.11 if you have it:

```bash
python3.11 -m venv venv
```

If that says “command not found”, use:

```bash
python3 -m venv venv
```

### Step 3 — Activate it

```bash
source venv/bin/activate
```

Your Terminal prompt should now start with `(venv)`.

### Step 4 — Install packages

```bash
pip install -r requirements.txt
```

Wait until it finishes (a few minutes).  
When it ends with no red error, you’re good.

### Step 5 — Start the app

```bash
streamlit run app.py
```

### Step 6 — Open in browser

- Your browser may open automatically.
- If not, go to: **http://localhost:8501**

You should see: **AI-Based Pediatric Movement Analysis**

---

## C2. Windows — install steps

### Step 1 — Go into the project folder

In **Command Prompt**:

```bat
cd %USERPROFILE%\Downloads\Anxietyprediction
```

> If needed, change the path.  
> Example: `cd %USERPROFILE%\Desktop\Anxietyprediction`  
> Example with ZIP name: `cd %USERPROFILE%\Downloads\Anxietyprediction-main`

Check:

```bat
dir
```

You should see `app.py`, `requirements.txt`, `anxiety_model.pkl`.

### Step 2 — Create the virtual environment

```bat
python -m venv venv
```

If that fails, try:

```bat
py -3.11 -m venv venv
```

### Step 3 — Activate it

```bat
venv\Scripts\activate
```

Your prompt should now start with `(venv)`.

If you get an execution-policy error in **PowerShell**, use **Command Prompt** instead, or run:

```bat
venv\Scripts\activate.bat
```

### Step 4 — Install packages

```bat
pip install -r requirements.txt
```

Wait a few minutes until it finishes.

### Step 5 — Start the app

```bat
streamlit run app.py
```

### Step 6 — Open in browser

Go to: **http://localhost:8501**

---

# Part D — Use the app

1. Click **Browse files** / **Upload Video**.
2. Choose a short video (`.mp4` recommended).
3. Click **Analyze Video**.
4. Wait for the spinner to finish.
5. Read the metrics and anxiety prediction.
6. Optionally click **Download CSV**.

To **stop** the app later: go back to Terminal / Command Prompt and press **`Ctrl + C`**.

---

# Part E — Next time you want to run it (after first setup)

You do **not** need to install everything again.

## Mac

```bash
cd ~/Downloads/Anxietyprediction
source venv/bin/activate
streamlit run app.py
```

## Windows

```bat
cd %USERPROFILE%\Downloads\Anxietyprediction
venv\Scripts\activate
streamlit run app.py
```

Then open **http://localhost:8501**.

---

# Troubleshooting (common problems)

### 1) `python` / `python3` not found
- Reinstall Python 3.11 from python.org.
- On Windows, check **Add python.exe to PATH**.
- Close and reopen Terminal / Command Prompt after installing.

### 2) `pip install` fails or shows red errors
- Make sure `(venv)` is visible in your prompt.
- Try again:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3) `streamlit: command not found`
- The virtual environment is not activated.
- Run the activate command again (Part E), then:

```bash
streamlit run app.py
```

### 4) Browser shows “This site can’t be reached”
- Make sure `streamlit run app.py` is still running in the terminal.
- Try: **http://127.0.0.1:8501**

### 5) Analysis is very slow
- Use a shorter / smaller video.
- Your own computer is much better than free online hosting for this app.

### 6) Analysis crashes or fails
- Confirm these files exist in the project folder:
  - `anxiety_model.pkl`
  - `cascades/haarcascade_frontalface_default.xml`
  - `cascades/haarcascade_eye.xml`
- If any are missing, download the project ZIP again (don’t delete folders).

### 7) Wrong folder
If `ls` / `dir` does not show `app.py`, you are in the wrong folder.  
Use File Explorer / Finder to find `app.py`, then `cd` to that folder.

---

# Quick reference card

| Task | Mac | Windows |
|------|-----|---------|
| Go to project | `cd ~/Downloads/Anxietyprediction` | `cd %USERPROFILE%\Downloads\Anxietyprediction` |
| Activate | `source venv/bin/activate` | `venv\Scripts\activate` |
| Run app | `streamlit run app.py` | `streamlit run app.py` |
| Open app | http://localhost:8501 | http://localhost:8501 |
| Stop app | `Ctrl + C` | `Ctrl + C` |

---

# What each important file is (optional reading)

| File / folder | Meaning |
|---------------|---------|
| `app.py` | The website you see in the browser |
| `movement_analysis.py` | Looks at the video and counts movements |
| `anxiety_model.pkl` | The trained anxiety prediction model |
| `requirements.txt` | List of packages to install |
| `cascades/` | Face/eye detection files OpenCV needs |
| `venv/` | Your private install folder (do not delete after setup) |

---

# Need help?

If something fails, copy **the full error text** from the terminal and share it with the person helping you.  
Also say whether you are on **Mac** or **Windows**.
