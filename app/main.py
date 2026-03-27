import argparse
from classifier import classify_intent
from router import route_intent
from logger import log_info, log_error


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Workflow Assistant")
    parser.add_argument("--command", required=True, help="Natural language command")
    args = parser.parse_args()

    command = args.command
    log_info(f"Received command: {command}")

    try:
        classification = classify_intent(command)
        intent = classification["intent"]

        log_info(f"Classified intent: {intent}")

        result = route_intent(intent, command)

        log_info(f"Execution result: {result}")
        print(result)

    except Exception as exc:
        log_error(str(exc))
        print({"status": "error", "message": str(exc)})


if __name__ == "__main__":
    main()
