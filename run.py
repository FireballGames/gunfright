#!/usr/bin/env python
# -*- coding: utf-8 -*-
import config
from gunfright.game import Game
from log import logger


def main():
    logger.info("Starting Gunfright!")
    logger.debug("Loading game configuration")

    game = Game(config.load('game.yml'))
    game.run()
    game.quit()


if __name__ == '__main__':
    main()
