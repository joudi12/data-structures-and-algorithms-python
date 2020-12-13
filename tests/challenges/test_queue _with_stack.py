from data_structures_and_algorithms.challenges.queue_with_stacks.queue_with_stacks import PseudoQueue

def test_stacks_enqueue():
    queue = PseudoQueue()
    queue.enqueue(1)
    assert queue.first_stack.top.value == 1


def test_stacks_enqueue_multiple():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.first_stack.top.value == 3
    assert queue.first_stack.top.next.value == 2
    assert queue.first_stack.top.next.next.value == 1

def test_stacks_dequeue():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    assert queue.secound_stack.top.value == 2
    assert queue.secound_stack.top.next.value == 3
    assert queue.secound_stack.top.next.next == None

def test_stacks_dequeue_multiple():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    assert queue.secound_stack.top.value == 3
    assert queue.secound_stack.top.next == None
