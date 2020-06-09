import random


def roll(count=1):
    return sum(random.randint(1, 6) for _ in range(count))
