from data_structures_and_algorithms.stacks_and_queues.stacks_and_queues import Stack,Node

class PseudoQueue:
    def __init__(self):
        self.first_stack =Stack()
        self.secound_stack =Stack()
    def enqueue(self,value):
        self.first_stack.push(value)



    def dequeue(self):
        if (self.first_stack.top == None and self.secound_stack.top == None):
            return "Queue is empty."
        if (self.secound_stack.top == None):
            while(self.first_stack.top):
                self.secound_stack.push(self.first_stack.pop())
        return self.secound_stack.pop()










if __name__ == "__main__":
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)


