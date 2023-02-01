import logging
import sys


LOG_FORMAT: str = "{levelname:<9s} {message}"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(logging.Formatter(LOG_FORMAT, style="{"))

logger.addHandler(handler)
