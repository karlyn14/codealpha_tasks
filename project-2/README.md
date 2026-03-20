# Part 2 – AI Evaluation Fairness & Bias Check

## What This Project Does
Tests whether the AI evaluation engine scores answers **fairly** across
different quality levels. Submits excellent, average, and wrong answers
for the same question and checks if the AI correctly rewards quality.

---

## How to Run in VS Code

### Step 1 – Open the folder
Open VS Code → File → Open Folder → select `part2_ai_bias_check`

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
- Each question tested with 3 answer tiers: 🟢 Excellent / 🟡 Average / 🔴 Wrong
- Score per tier printed live
- Fairness check per question: ✅ Fair or ⚠️ Biased
- Final report with score gap analysis and overall verdict
- Results saved in `outputs/` folder as a JSON file

---

## Output Example
```
Q1: What is overfitting in machine learning?
   🟢 Excellent → Score: 9/10  |  Correct
   🟡 Average   → Score: 6/10  |  Partially Correct
   🔴 Wrong     → Score: 1/10  |  Incorrect
   Fairness: ✅ FAIR

FAIRNESS ANALYSIS REPORT
Q#    Excellent    Average    Wrong     Gap   Status
Q1           9          6        1       8   ✅ Fair
...
✅ VERDICT: AI evaluation engine is FAIR
```

---

## Resume Line
> *Analyzed AI evaluation model for scoring bias by submitting variable-quality responses
> and comparing LLM-generated scores; flagged inconsistencies and proposed fairness
> improvements.*
