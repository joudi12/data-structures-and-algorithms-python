from data_structures_and_algorithms.data_structures.hashtable.hashtable import HashTable , Linkedlist


def test_key_value():
    table = HashTable(1024)
    table.add('name','joudi')
    table.add('name','sali')

    assert table.map[table.hash('name')].head.data[1] == 'joudi'

def test_add_key():
    table = HashTable(1024)
    table.add('joudi','19')
    assert table.map[table.hash('joudi')].head.data == ['joudi','19']


def test_get_value():
    table = HashTable(1024)
    table.add('joudi','19')
    assert table.get('joudi') ==  '19'

def test_value_not_in_table():
    table = HashTable(1024)
    assert table.get('joudi') == 'Not in the table'

def test_collision():
    table = HashTable(1024)
    table.add('cloud','19')
    table.add('could','32')
    assert table.map[table.hash('cloud')].head.data == ['cloud','19']
    assert table.map[table.hash('cloud')].head.next.data == ['could','32']


def test_retrieve_collision():
    table = HashTable(1024)
    table.add('cloud','19')
    table.add('could','32')
    assert table.get('cloud') == '19'
    assert table.get('could') == '32'
