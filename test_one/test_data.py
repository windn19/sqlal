import pytest

from new.packet.data import QA

def questions(questions, cur_answer, user_answer):
    print(questions)
    if user_answer == cur_answer:
        return 'CORRECT'
    return 'INCORRECT'


def test_one():
    for q, cur_ans, user_ans, res in QA:
        assert questions(q, cur_ans, user_ans) == res, 'Ошибочный ответ'


@pytest.mark.parametrize('question, cur_answer, user_answer, result', QA)
def test_two(question, cur_answer, user_answer, result):
    assert questions(question, cur_answer, user_answer) == result, 'Ошибочный ответ'


@pytest.fixture()
def data():
    return QA


def test_three(data):
    for q, cur_ans, user_ans, res in data:
        assert questions(q, cur_ans, user_ans) == res, 'Ошибочный ответ'


pytest.main()
