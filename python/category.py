from enum import IntEnum


class Category(IntEnum):

    POP = 1
    SCIENCE = 2
    SPORTS = 3
    ROCK = 4

    def __str__(self) -> str:
        return super().name


position_category: dict[int, Category] = {
    0: Category.POP,
    1: Category.SCIENCE,
    2: Category.SPORTS,
    3: Category.ROCK,
    4: Category.POP,
    5: Category.SCIENCE,
    6: Category.SPORTS,
    7: Category.ROCK,
    8: Category.POP,
    9: Category.SCIENCE,
    10: Category.SPORTS,
    11: Category.ROCK,
}