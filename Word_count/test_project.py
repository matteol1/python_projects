from project import *

def test_word_cleaner():
    assert word_cleaner('\\document')==None
    assert word_cleaner('Hello!')=='hello'

def test_read_file():
    d = read_file(open(TEST_FILE, 'r'))
    assert d['action']==1
    assert d['the']==2

def test_check_file():
    assert check_file('test.txt')

def test_dict_to_data():
    assert dict_to_data(TEST_DICT)['Word'].iloc[0] == "Riddle"