import logging
from src.logg import LOGGING_CONFIG
logging.config.dictConfig(LOGGING_CONFIG)
logger=logging.getLogger(__name__)