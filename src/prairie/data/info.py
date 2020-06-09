class Info:
    def __init__(self, text, article=lambda p: None):
        self.text = text
        self.article = article


class FoxTrail(Info):
    def __init__(self):
        super().__init__('Лисья Тропа', lambda p: p + 90)


class UncleJacobRanch(Info):
    def __init__(self):
        super().__init__('Ранчо дядюшки Джейкоба', lambda p: p + 180)
