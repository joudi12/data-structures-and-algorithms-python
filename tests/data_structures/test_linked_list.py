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

def test_append():
    ll=LinkedList()
    ll.append(5)
    ll.append(3)
    ll.append(2)
    assert ll.head.value ==5
    assert ll.head.next.value ==3
    assert ll.head.next.next.value ==2
    assert ll.head.next.next.next ==None


def test_append_once():
    ll = LinkedList()
    ll.append(1)
    assert ll.head.value == 1


def test_insert_before():
    ll = LinkedList()
    ll.append(1)
    ll.append(6)
    ll.append(9)
    ll.insert_before(6, 33)
    assert ll.head.next.value == 33

def test_insert_before_first_node():
    ll = LinkedList()
    ll.append(1)
    ll.insert_before(1, 33)
    assert ll.head.value == 33


def test_insert_after_mid():
    ll = LinkedList()
    ll.append(1)
    ll.append(6)
    ll.append(9)
    ll.append(4)
    ll.insert_after(6,11)
    assert  ll.head.next.next.value == 11

def test_insert_after():
    ll = LinkedList()
    ll.append(1)
    ll.append(6)
    ll.append(9)
    ll.insert_after(9,11)
    assert  ll.head.next.next.next.value == 11



def test_middle_k():
    ll = LinkedList()
    ll.append('1')
    ll.append('2')
    ll.append('3')
    ll.append('4')
    ll.append('5')
    ll.append('6')
    assert ll.kth_from_end(3) == '3'

def test_kth_from_end_0():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = 2
    actual =ll.kth_from_end(0)
    assert expected == actual

def test_kth_from_end_2():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = 3
    actual =ll.kth_from_end(2)
    assert expected == actual

def test_kth_from_end_6():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = "The Value Not Found"
    actual =ll.kth_from_end(6)
    assert expected == actual

def test_kth_from_end_size_one():
    ll = LinkedList()
    ll.append(1)
    expected = 1
    actual =ll.kth_from_end(0)
    assert expected == actual


def test_kth_from_end_negative():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = "The Value Not Found"
    actual =ll.kth_from_end(-2)
    assert expected == actual
def test_kth_from_end_same():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = "The Value Not Found"
    actual =ll.kth_from_end(4)
    assert expected == actual









