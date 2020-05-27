import yaml
from log import logger


class Config:
    __instance = None
    __params = {}

    def __init__(self):
        pass

    def __getitem__(self, key):
        if key in self.__params:
            return self.__params[key]
        else:
            return False

    def __getattr__(self, key):
        if key in self.__params:
            return self.__params[key]
        else:
            return False

    def __str__(self):
        return str(self.__params)

    def update(self, **params):
        self.__params.update(params)

    def screen(self, index):
        return self.screens[index]

    @classmethod
    def config(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    @classmethod
    def load_from_file(cls, filename=None):
        if filename:
            logger.debug("Loading config from \"%s\"...", filename)
            with open(filename, 'r') as f:
                data = yaml.load(f)
                cls.config().update(**data)

    @classmethod
    def level(cls, index):
        levels = cls.__instance.levels
        if index in levels:
            return levels[index]
        else:
            return levels[-1]

    @classmethod
    def get_map(cls):
        return [
            [1, 1, 2],
            [1, 2, 3],
            [2, 3, 3]
        ]

    @classmethod
    def get_screen(cls, index):
        return cls.config().screen(index)


CONFIG = Config()
