"""
logger.py
Saves results to a JSON file and prints a summary table.
"""

import json
import os
from datetime import datetime


def log_results(results: list):
    """Save all results to a timestamped JSON file."""
    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/consistency_results_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n📁 Results saved to: {filename}")


def print_summary(results: list):
    """Print a clean summary table to the console."""
    print("\n" + "="*60)
    print("  SUMMARY")
    print("="*60)
    print(f"{'Q#':<5} {'Min':>5} {'Max':>5} {'Variance':>10}  {'Status'}")
    print("-"*60)

    total = len(results)
    consistent_count = 0

    for r in results:
        status = "✅ Consistent" if r["is_consistent"] else "⚠️  Inconsistent"
        if r["is_consistent"]:
            consistent_count += 1
        print(f"Q{r['question_id']:<4} {r['min_score']:>5} {r['max_score']:>5} {r['variance']:>10}  {status}")

    print("-"*60)
    print(f"\nConsistency Rate: {consistent_count}/{total} questions were fully consistent")

    if consistent_count == total:
        print("✅ VERDICT: AI evaluation engine is CONSISTENT across all test cases.")
    else:
        print("⚠️  VERDICT: AI evaluation engine shows INCONSISTENCY — review flagged questions.")
    print("="*60 + "\n")
