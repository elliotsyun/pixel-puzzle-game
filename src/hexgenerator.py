import random

CEILING = 255
FLOOR = 0


def generate_rgb():
    """Generates a random color tuple that has each value between 0 and 255"""

    color = (
        random.randint(FLOOR, CEILING),
        random.randint(FLOOR, CEILING),
        random.randint(FLOOR, CEILING),
    )

    return color
