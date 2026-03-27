from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"
LOG_DIR = DATA_DIR / "logs"

for directory in [INPUT_DIR, OUTPUT_DIR, LOG_DIR]:
    directory.mkdir(parents=True, exist_ok=True)
