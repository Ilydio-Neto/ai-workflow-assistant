import logging
from config import LOG_DIR

LOG_FILE = LOG_DIR / "assistant.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(message: str) -> None:
    logging.info(message)

def log_error(message: str) -> None:
    logging.error(message)
