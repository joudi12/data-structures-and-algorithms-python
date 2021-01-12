from data_structures_and_algorithms.challenges.left_join.left_join import left_join
from data_structures_and_algorithms.data_structures.hashtable.hashtable import HashTable


def test_simple_left_join():

    synonym=HashTable(1024)
    antonyms=HashTable(1024)
    synonym.add('fond','enamored')
    synonym.add('wrath','anger')
    antonyms.add('fond','averse')
    assert left_join(synonym, antonyms) == [['fond', 'enamored', 'averse'], ['wrath', 'anger', 'null']]


def test_no_common_keys():
    synonym=HashTable(1024)
    antonyms=HashTable(1024)
    synonym.add('fond','enamored')
    synonym.add('wrath','anger')
    antonyms.add('see','look')
    assert left_join(synonym, antonyms) == [['fond', 'enamored', 'null'], ['wrath', 'anger', 'null']]




def test_1st_dict_is_empty():
    synonym=HashTable(1024)
    antonyms=HashTable(1024)
    antonyms.add('see','look')
    assert left_join(synonym, antonyms) == []


def test_2nd_dictionary_empty():

    synonym=HashTable(1024)
    antonyms=HashTable(1024)
    synonym.add('fond','enamored')
    synonym.add('wrath','anger')
    assert left_join(synonym, antonyms) == [['fond', 'enamored', 'null'], ['wrath', 'anger', 'null']]
