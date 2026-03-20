"""
Part 1 – AI Evaluation Consistency Check
=========================================
Tests whether the GPT-based evaluation engine returns
consistent results when the same answer is submitted multiple times.

Run: python main.py
"""

import json
import time
from evaluator import evaluate_answer
from logger import log_results, print_summary

# ─── Test Inputs ────────────────────────────────────────────────────────────
TEST_CASES = [
    {
        "question_id": 1,
        "question": "What is Python?",
        "answer": "Python is a high-level, interpreted programming language known for its simple syntax.",
        "runs": 5
    },
    {
        "question_id": 2,
        "question": "What is machine learning?",
        "answer": "Machine learning is a subset of AI where models learn patterns from data without being explicitly programmed.",
        "runs": 5
    },
    {
        "question_id": 3,
        "question": "What is overfitting?",
        "answer": "Overfitting is when a model performs well on training data but poorly on unseen test data.",
        "runs": 5
    },
]

# ─── Main ────────────────────────────────────────────────────────────────────
def run_consistency_test():
    print("\n" + "="*60)
    print("  PART 1 – AI EVALUATION CONSISTENCY CHECK")
    print("="*60)

    all_results = []

    for tc in TEST_CASES:
        print(f"\n🔵 Testing Q{tc['question_id']}: {tc['question']}")
        print(f"   Answer: {tc['answer'][:60]}...")
        print(f"   Running {tc['runs']} times...\n")

        results = []
        for i in range(1, tc["runs"] + 1):
            result = evaluate_answer(tc["question"], tc["answer"])
            results.append({
                "run": i,
                "score": result["score"],
                "verdict": result["verdict"],
                "reasoning": result["reasoning"]
            })
            print(f"   Run {i}: Score={result['score']}/10  Verdict={result['verdict']}")
            time.sleep(1)  # avoid rate limiting

        scores = [r["score"] for r in results]
        is_consistent = len(set(scores)) == 1
        variance = max(scores) - min(scores)

        all_results.append({
            "question_id": tc["question_id"],
            "question": tc["question"],
            "answer": tc["answer"],
            "runs": results,
            "is_consistent": is_consistent,
            "min_score": min(scores),
            "max_score": max(scores),
            "variance": variance
        })

        status = "✅ CONSISTENT" if is_consistent else f"⚠️  INCONSISTENT (variance: {variance})"
        print(f"\n   Result: {status}")

    log_results(all_results)
    print_summary(all_results)

if __name__ == "__main__":
    run_consistency_test()
