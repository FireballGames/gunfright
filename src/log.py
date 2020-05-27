import logging


FORMAT = "%(asctime)s %(levelname) -8s %(name) -16s %(message)s"
LEVEL = logging.DEBUG
LOGGER_NAME = 'gunfright'


logging.basicConfig(
    # "filename": "gunfright.log",
    format=FORMAT,
    level=LEVEL,
)

logger = logging.getLogger(LOGGER_NAME)
