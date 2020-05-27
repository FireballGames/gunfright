#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config import Config
from gunfright.game import Gunfright
from log import logger


CONFIG_FILE = 'game.yml'


def main():
    logger.info("Loading config...")
    config = Config()
    config.load_from_file(CONFIG_FILE)

    logger.info("Starting Game...")
    game = Gunfright(config)

    logger.info("Running Game...")
    game.run()

    logger.info("Quiting game...")
    game.quit()

    logger.info("Bye!")


if __name__ == '__main__':
    main()
