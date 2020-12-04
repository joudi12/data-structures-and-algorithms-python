from data_structures_and_algorithms.data_structures.linked_list.linked_list.linked_list import LinkedList





def test_empty():
    ll = LinkedList()
    assert ll.head == None

def test_insert_head():
    ll = LinkedList()
    ll.insert(5)
    assert ll.head.value == 5

def test_insert():
    ll = LinkedList()
    ll.insert(3)
    assert ll.head.value == 3

def test_insert_multipal():
    ll =LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(8)
    assert ll.head.value ==8
    assert ll.head.next.value ==7
    assert ll.head.next.next.value ==5
    assert ll.head.next.next.next ==None

def test_include_true():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    assert ll.includes(7)==True

def test_include_false():
    ll =LinkedList()
    ll.insert(4)
    ll.insert(9)
    assert ll.includes(5) == False

def test_string():
    ll=LinkedList()
    ll.insert(9)
    ll.insert(7)
    ll.insert(3)
    assert ll.__str__()=="{ 3 } -> { 7 } -> { 9 } -> NULL"





