from data_structures_and_algorithms.challenges.mergesort.mergesort import Mergesort


def test_revers_sort():
    assert Mergesort([20,18,12,8,5,-2])== [-2,5,8,12,18,20]


def test_few_uniques():
    assert Mergesort([5,12,7,5,5,7])== [5,5,5,7,7,12]

def test_nearly_sorted():
    assert Mergesort([2,3,5,7,13,11])== [2,3,5,7,11,13]

