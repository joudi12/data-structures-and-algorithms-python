from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import array_binary_search

def  test_binary_true():
    actual = array_binary_search(15,[4,8,15,16,23,42])
    expected= 2
    assert actual == expected

def  test_binary_false():
    actual = array_binary_search(99,[1,2,3,4,5,6,7])
    expected= -1
    assert actual == expected
def  test_binary_empty():
    actual = array_binary_search(8,[])
    expected= -1
    assert actual == expected

