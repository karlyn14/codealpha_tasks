# Part 1 – AI Evaluation Consistency Check

## What This Project Does
Tests whether the GPT/AI evaluation engine gives the **same score and verdict** every time
the same answer is submitted. Flags any inconsistency in the AI model's responses.

---

## How to Run in VS Code

### Step 1 – Open the folder
Open VS Code → File → Open Folder → select `part1_ai_consistency_check`

### Step 2 – Open terminal
Press `` Ctrl + ` `` to open terminal inside VS Code

### Step 3 – Create virtual environment
```bash
python -m venv venv
```

### Step 4 – Activate virtual environment
**Windows:**
```bash
venv\Scripts\activate
```
**Mac/Linux:**
```bash
source venv/bin/activate
```

### Step 5 – Install dependencies
```bash
pip install -r requirements.txt
```

### Step 6 – Set your API key
**Windows:**
```bash
set ANTHROPIC_API_KEY=your_api_key_here
```
**Mac/Linux:**
```bash
export ANTHROPIC_API_KEY=your_api_key_here
```
> Get your free API key from: https://console.anthropic.com

### Step 7 – Run the project
```bash
python main.py
```

---

## What You Will See
- Each question tested 5 times
- Score and verdict printed for each run
- Consistency check: ✅ or ⚠️ per question
- Final summary table
- Results saved in `outputs/` folder as a JSON file

---

## Output Example
```
Run 1: Score=8/10  Verdict=Correct
Run 2: Score=8/10  Verdict=Correct
Run 3: Score=7/10  Verdict=Partially Correct   ← inconsistency flagged
...
⚠️  INCONSISTENT (variance: 1)
```

---

## Resume Line
> *Validated GPT-based answer evaluation engine by designing consistency tests across
> multiple inference runs; identified output variance patterns and documented model
> reliability metrics.*
