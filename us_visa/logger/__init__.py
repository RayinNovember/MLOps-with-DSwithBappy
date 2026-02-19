import logging
import os

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = 'logs'
logs_path = os.path.join(from_root(),log_dir,LOG_FILE)

os.makedirs(log_dir,exist_ok=True)


# https://www.youtube.com/watch?v=jxmzY9soFXg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=53
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("[%(asctime)s] %(name)s - %(levelname)s - %(message)s")

file_handler = logging.FileHandler(logs_path)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

