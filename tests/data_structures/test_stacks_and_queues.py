from data_structures_and_algorithms.stacks_and_queues.stacks_and_queues import (Stack,Node,Queue)

def test_push_4_items():
    lines = Stack()
    lines.push('hello from class')
    lines.push('welcome to demo')
    lines.push('we learn coding')
    lines.push('bye')
    assert lines.peek() == 'bye'

def test_pop():
    lines =Stack()
    lines.push(5)
    lines.push(8)

    assert lines.pop()==8
    assert lines.pop() ==5


def test_pop_from_empty_stack():
    nums = Stack()
    actual = nums.pop()
    expected = 'Stack is empty'
    assert actual == expected

def test_peek_from_stack():
    lines =Stack()
    lines.push(5)
    lines.push(8)

    assert lines.peek()== 8
    assert lines.pop()== 8
    assert lines.peek()==5
    assert lines.pop()==5
    assert lines.peek()=='Stack is empty'

def test_enqueue_one():
    queue = Queue()
    queue.enqueue(6)
    assert queue.rear.value == 6

def test_enqueue_multiple():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.rear.value == 2
    assert queue.front.value == 1

def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(3)
    queue.dequeue()
    assert queue.front.value == 3

def test_queue_peek():
    queue = Queue()
    queue.enqueue(7)
    queue.enqueue(3)
    assert queue.peek() == 7

def test_is_empty():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    queue.dequeue()
    assert queue.isEmpty() == True

def test_init():
    queue = Queue()
    assert queue.front == None
    assert queue.rear == None

def test_peek_from_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.peek()== 1
    assert queue.dequeue()== 1
    assert queue.peek()==2
    assert queue.dequeue()==2
    assert queue.peek()=='Queue is empty'

def test_peek_on_empty_queue():
    nums = Queue()
    actual = nums.peek()
    expected = 'Queue is empty'
    assert actual == expected
