from typing import Dict


def classify_intent(command: str) -> Dict[str, str]:
    text = command.lower()

    if "report" in text or "csv" in text:
        return {"intent": "generate_report", "confidence": "high"}

    if "summarize" in text or "summary" in text:
        return {"intent": "summarize_text", "confidence": "high"}

    if "task" in text or "todo" in text or "reminder" in text:
        return {"intent": "create_task", "confidence": "medium"}

    return {"intent": "unknown", "confidence": "low"}
