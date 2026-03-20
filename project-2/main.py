"""
Part 2 – AI Evaluation Fairness & Bias Check
=============================================
Tests whether the GPT-based evaluation engine scores answers
fairly across different quality levels (excellent, average, wrong).

Run: python main.py
"""

import time
from evaluator import evaluate_answer
from analyzer import analyze_fairness, print_report
from logger import log_results


# ─── Test Cases ──────────────────────────────────────────────────────────────
# Each question has 3 answer tiers: excellent, average, wrong
# We expect: excellent > average > wrong in scoring

TEST_CASES = [
    {
        "question_id": 1,
        "question": "What is overfitting in machine learning?",
        "answers": {
            "excellent": "Overfitting occurs when a model learns the training data too well, including noise and outliers, resulting in poor generalization to new unseen data. It can be detected when training accuracy is high but validation accuracy is low. Solutions include regularization, dropout, cross-validation, and using more training data.",
            "average":   "Overfitting is when the model works well on training data but not on new data.",
            "wrong":     "Overfitting means the model is too slow and needs more computing power to train faster."
        }
    },
    {
        "question_id": 2,
        "question": "Explain the difference between supervised and unsupervised learning.",
        "answers": {
            "excellent": "Supervised learning uses labeled datasets where the model learns the mapping from input to output by minimizing a loss function. Examples include classification and regression. Unsupervised learning works with unlabeled data and discovers hidden patterns or structures, such as clustering (K-Means) or dimensionality reduction (PCA).",
            "average":   "Supervised learning uses labels, unsupervised learning does not use labels.",
            "wrong":     "Supervised learning is done by teachers and unsupervised learning is done alone without any help."
        }
    },
    {
        "question_id": 3,
        "question": "What is a neural network?",
        "answers": {
            "excellent": "A neural network is a computational model inspired by biological neurons. It consists of layers — input, hidden, and output — where each node applies a weighted sum followed by an activation function. Deep neural networks with multiple hidden layers can learn complex non-linear patterns and are the foundation of modern deep learning.",
            "average":   "A neural network is a model made of layers that can learn patterns from data.",
            "wrong":     "A neural network is a type of computer virus that spreads through the internet."
        }
    },
]

# ─── Main ─────────────────────────────────────────────────────────────────────
def run_bias_check():
    print("\n" + "="*65)
    print("  PART 2 – AI EVALUATION FAIRNESS & BIAS CHECK")
    print("="*65)

    all_results = []

    for tc in TEST_CASES:
        print(f"\n🔵 Q{tc['question_id']}: {tc['question']}")
        question_results = {"question_id": tc["question_id"], "question": tc["question"], "scores": {}}

        for tier, answer in tc["answers"].items():
            result = evaluate_answer(tc["question"], answer)
            question_results["scores"][tier] = {
                "answer_preview": answer[:70] + "...",
                "score": result["score"],
                "verdict": result["verdict"],
                "reasoning": result["reasoning"]
            }
            tier_label = {"excellent": "🟢 Excellent", "average": "🟡 Average ", "wrong": "🔴 Wrong   "}[tier]
            print(f"   {tier_label} → Score: {result['score']}/10  |  {result['verdict']}")
            time.sleep(1)

        # Check ordering: excellent > average > wrong
        scores = question_results["scores"]
        is_fair = (
            scores["excellent"]["score"] >= scores["average"]["score"] >= scores["wrong"]["score"]
            and scores["excellent"]["score"] > scores["wrong"]["score"]
        )
        question_results["is_fair"] = is_fair
        all_results.append(question_results)

        status = "✅ FAIR" if is_fair else "⚠️  BIAS DETECTED"
        print(f"\n   Fairness: {status}")

    log_results(all_results)
    analysis = analyze_fairness(all_results)
    print_report(all_results, analysis)


if __name__ == "__main__":
    run_bias_check()
