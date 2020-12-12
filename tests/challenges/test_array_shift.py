from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray




def test_odd():
    actual = insertShiftArray([1,2,4,6,3], 8)
    expected = [1,2,4,8,6,3]
    assert actual == expected
def test_even():
    actual = insertShiftArray([1,2,4,6,3,99], 10)
    expected = [1,2,4,10,6,3,99]
    assert actual == expected


