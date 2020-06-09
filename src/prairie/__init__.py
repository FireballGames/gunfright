from .player import Player
from .story import story


class Prairie:
    def __init__(self):
        self.player = Player()
        self.player.char_sheet()
        self.article_id = None

    def look(self):
        return story(self.article_id)

    def go(self, article_id):
        self.article_id = article_id
        return self.look()
