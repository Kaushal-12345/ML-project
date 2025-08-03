import logging
import os
from datetime import datetime

# Create a logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Create a unique log filename based on current time
LOG_FILE = f"{LOG_DIR}/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)
