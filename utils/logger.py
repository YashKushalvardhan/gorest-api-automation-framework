# utils/logger.py
import logging
import os
from datetime import datetime

# Log directory ensure karo
log_dir = "reports"
os.makedirs(log_dir, exist_ok=True)

log_file = f"reports/test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()   # Console pe bhi dikhega
    ]
)

logger = logging.getLogger("gorest_api_framework")

# Convenience functions
def log_info(message):
    logger.info(message)

def log_error(message):
    logger.error(message)

def log_debug(message):
    logger.debug(message)

def log_warning(message):
    logger.warning(message)