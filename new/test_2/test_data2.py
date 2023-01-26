import pytest

from new.packet import data
# QA = [
#     ('Год рождения Ломоносова?', '1711', '1711', 'CORRECT'),
#     ('Год рождения Ландау?', '1908', '1908', 'CORRECT'),
#     ('Год рождения Попова?', '1859', '1859', 'CORRECT'),
#     ('Год рождения Курчатова?', '1903', '1903', 'CORRECT'),
#     ('Год рождения Тамма?', '1895', '1895', 'CORRECT'),
#     ('Год рождения Гейма?', '1958', '1958', 'INCORRECT')
# ]


def questions(questions, cur_answer, user_answer):
    print(questions)
    if user_answer == cur_answer:
        return 'CORRECT'
    return 'INCORRECT'


def test_one():
    for q, cur_ans, user_ans, res in data.QA:
        assert questions(q, cur_ans, user_ans) == res, 'Ошибочный ответ'


@pytest.mark.parametrize('question, cur_answer, user_answer, result', data.QA)
def test_two(question, cur_answer, user_answer, result):
    assert questions(question, cur_answer, user_answer) == result, 'Ошибочный ответ'


@pytest.fixture()
def data1():
    return data.QA


def test_three(data1):
    for q, cur_ans, user_ans, res in data1:
        assert questions(q, cur_ans, user_ans) == res, 'Ошибочный ответ'


pytest.main()
