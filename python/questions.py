from category import Category
from errors import QuestionsNotEmptyError, QuestionsEmptyError

class Question:

    def __init__(self, total: int, category: Category) -> None:
        self._total = total 
        self._category = category
        self._questions = []

    @property
    def questions(self) -> list[str]:
        return self._questions

    def create(self) -> None:
        if not self.is_empty():
            raise QuestionsNotEmptyError(f"{str.lower(self._category.name)} question set is not empty.")
        self._questions = [f"{str.lower(self._category.name)} question {i}" for i in range(self._total)]
    
    def get_question(self) -> str:
        if self.is_empty():
            raise QuestionsEmptyError(f"{str.lower(self._category.name)} question set is empty. Try creating questions first.")
        return self._questions.pop(0) 

    def is_empty(self) -> bool:
        return not self._questions
    
    @classmethod
    def from_pop(cls, total: int) -> 'Question':
        return cls(
            total=total,
            category=Category.POP,
        )

    @classmethod
    def from_science(cls, total: int) -> 'Question':
        return cls(
            total=total,
            category=Category.SCIENCE,
        )

    @classmethod
    def from_sport(cls, total: int) -> 'Question':
        return cls(
            total=total,
            category=Category.SPORTS,
        )

    @classmethod
    def from_rock(cls, total: int) -> 'Question':
        return cls(
            total=total,
            category=Category.ROCK,
        )