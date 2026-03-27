from pathlib import Path
import pandas as pd
from config import OUTPUT_DIR


def generate_report(command: str) -> dict:
    data = [
        {"month": "March", "sales": 12000, "region": "South"},
        {"month": "March", "sales": 18500, "region": "Southeast"},
        {"month": "March", "sales": 9700, "region": "Northeast"},
    ]

    df = pd.DataFrame(data)
    output_file = OUTPUT_DIR / "sales_report.csv"
    df.to_csv(output_file, index=False)

    return {
        "status": "success",
        "message": "Report generated successfully",
        "output_file": str(output_file)
    }


def summarize_text(command: str) -> dict:
    sample_summary = (
        "This workflow assistant can interpret simple commands and execute "
        "predefined automation tasks such as report generation and task creation."
    )

    return {
        "status": "success",
        "message": "Summary generated successfully",
        "summary": sample_summary
    }


def create_task(command: str) -> dict:
    output_file = OUTPUT_DIR / "tasks.txt"

    with open(output_file, "a", encoding="utf-8") as file:
        file.write(f"{command}\n")

    return {
        "status": "success",
        "message": "Task created successfully",
        "output_file": str(output_file)
    }
