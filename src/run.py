#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from config import Config
from gunfright.game import Gunfright
from log import setup_logger


CONFIG_FILE = 'game.yml'


setup_logger()


def main():
    logging.info("Loading config...")
    config = Config()
    config.load_from_file(CONFIG_FILE)

    logging.info("Starting Game...")
    game = Gunfright(config)

    logging.info("Running Game...")
    game.run()

    logging.info("Quiting game...")
    game.quit()

    logging.info("Bye!")


if __name__ == '__main__':
    main()
