from questions import Question
from category import Category
from errors import QuestionsNotEmptyError, QuestionsEmptyError
import pytest

@pytest.fixture(scope="function")
def question() -> Question:
    return Question(total=50, category=Category.POP)

def test_question_create(question):
    question.create()
    assert len(question.questions) == 50

def test_question_category(question):
    question.create()
    assert question.questions[0] == "pop question 0"

def test_question_get(question):
    question._total = 1 # override
    question.create()

    assert question.get_question() == "pop question 0"

def test_question_is_empty(question):

    assert question.is_empty()

def test_question_create_raises(question):

    question.create()

    with pytest.raises(QuestionsNotEmptyError) as err:
        question.create()

def test_question_get_raises(question):

    with pytest.raises(QuestionsEmptyError) as err:
        question.get_question()