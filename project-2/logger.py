"""
logger.py
Saves bias check results to a JSON file.
"""

import json
import os
from datetime import datetime


def log_results(results: list):
    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/bias_results_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n📁 Results saved to: {filename}")
