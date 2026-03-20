"""
analyzer.py
Analyzes fairness of AI scoring across answer quality tiers.
"""


def analyze_fairness(results: list) -> dict:
    total = len(results)
    fair_count = sum(1 for r in results if r["is_fair"])
    biased_questions = [r["question_id"] for r in results if not r["is_fair"]]

    # Score gap analysis
    gaps = []
    for r in results:
        excellent = r["scores"]["excellent"]["score"]
        wrong = r["scores"]["wrong"]["score"]
        gaps.append(excellent - wrong)

    avg_gap = sum(gaps) / len(gaps) if gaps else 0

    return {
        "total_questions": total,
        "fair_count": fair_count,
        "biased_count": total - fair_count,
        "biased_questions": biased_questions,
        "average_score_gap": round(avg_gap, 2),
        "fairness_rate": f"{round((fair_count / total) * 100)}%"
    }


def print_report(results: list, analysis: dict):
    print("\n" + "="*65)
    print("  FAIRNESS ANALYSIS REPORT")
    print("="*65)

    print(f"\n{'Q#':<5} {'Excellent':>10} {'Average':>10} {'Wrong':>8}  {'Gap':>6}  {'Status'}")
    print("-"*65)

    for r in results:
        s = r["scores"]
        exc = s["excellent"]["score"]
        avg = s["average"]["score"]
        wrg = s["wrong"]["score"]
        gap = exc - wrg
        status = "✅ Fair" if r["is_fair"] else "⚠️  Biased"
        print(f"Q{r['question_id']:<4} {exc:>10} {avg:>10} {wrg:>8}  {gap:>6}  {status}")

    print("-"*65)
    print(f"\n📊 Fairness Rate     : {analysis['fairness_rate']}")
    print(f"📊 Avg Score Gap     : {analysis['average_score_gap']} pts (Excellent vs Wrong)")
    print(f"📊 Fair Questions    : {analysis['fair_count']} / {analysis['total_questions']}")

    if analysis["biased_questions"]:
        print(f"⚠️  Biased on Q#s     : {analysis['biased_questions']}")

    print()
    if analysis["fair_count"] == analysis["total_questions"]:
        print("✅ VERDICT: AI evaluation engine is FAIR — scores correctly reflect answer quality.")
    elif analysis["fair_count"] >= analysis["total_questions"] / 2:
        print("⚠️  VERDICT: AI evaluation engine is MOSTLY FAIR but shows bias on some questions.")
    else:
        print("❌ VERDICT: AI evaluation engine shows SIGNIFICANT BIAS — review scoring logic.")

    print("="*65 + "\n")
