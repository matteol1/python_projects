from project import *


def test_word_cleaner():
    assert word_cleaner('\\document')==None
    assert word_cleaner('Hello!')=='hello'

