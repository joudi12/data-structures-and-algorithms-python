from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_case0():
    mystr='{}(){}'
    actual = multi_bracket_validation(mystr)
    expected = True
    assert actual == expected

def test_case1():
    mystr='()[[Extra Characters]]'
    actual = multi_bracket_validation(mystr)
    expected = True
    assert actual == expected

def test_case2():
    mystr='(){}[[]]'
    actual = multi_bracket_validation(mystr)
    expected = True
    assert actual == expected


def test_case3():
    mystr='[({}]'
    actual = multi_bracket_validation(mystr)
    expected = False
    assert actual == expected

def test_case4():
    mystr='(]('
    actual = multi_bracket_validation(mystr)
    expected = False
    assert actual == expected

def test_case5():
    mystr='{(})'
    actual = multi_bracket_validation(mystr)
    expected = False
    assert actual == expected

