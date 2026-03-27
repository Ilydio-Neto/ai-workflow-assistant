from tasks import generate_report, summarize_text, create_task


def route_intent(intent: str, command: str) -> dict:
    if intent == "generate_report":
        return generate_report(command)

    if intent == "summarize_text":
        return summarize_text(command)

    if intent == "create_task":
        return create_task(command)

    return {
        "status": "failed",
        "message": "Unknown intent. No action executed."
    }
