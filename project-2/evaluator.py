"""
evaluator.py
Calls the AI API to score a given answer for a question.
"""

import os
import json
import anthropic

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are a strict but fair AI exam evaluator.
When given a question and an answer, evaluate the answer and respond ONLY in this exact JSON format:
{
  "score": <integer from 0 to 10>,
  "verdict": "<Correct | Partially Correct | Incorrect>",
  "reasoning": "<one sentence explanation>"
}
Do not include any text outside the JSON."""


def evaluate_answer(question: str, answer: str) -> dict:
    user_message = f"Question: {question}\nAnswer: {answer}"

    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=300,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_message}]
        )

        raw = response.content[0].text.strip()

        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]

        result = json.loads(raw)
        assert "score" in result and "verdict" in result and "reasoning" in result
        return result

    except Exception as e:
        print(f"   ⚠️  API error: {e}")
        return {"score": -1, "verdict": "ERROR", "reasoning": str(e)}
