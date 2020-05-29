import logging


FORMAT = "%(asctime)s %(levelname) -8s %(name) -16s %(message)s"
LEVEL = logging.DEBUG
LOGGER_NAME = 'gunfright'


def setup_logger():
    logging.basicConfig(
        # "filename": "gunfright.log",
        format=FORMAT,
        level=LEVEL,
    )
