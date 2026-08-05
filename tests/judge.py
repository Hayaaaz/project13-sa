import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
from difflib import SequenceMatcher
from src.bot import answer

THRESHOLD = 0.85  # groundedness threshold

def similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def run_eval():
    with open("tests/eval_cases.json", "r") as f:
        cases = json.load(f)

    scores = []
    for case in cases:
        resp = answer(case["question"])
        score = similarity(resp, case["expected"])
        scores.append(score)
        print(f"{case['name']}: {score:.3f}")

    avg = sum(scores) / len(scores)
    print(f"Average groundedness: {avg:.3f}")

    if avg < THRESHOLD:
        print("Eval FAILED")
        return 1
    else:
        print("Eval PASSED")
        return 0

if __name__ == "__main__":
    exit(run_eval())


