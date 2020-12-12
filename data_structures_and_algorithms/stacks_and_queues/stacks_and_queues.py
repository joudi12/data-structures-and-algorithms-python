class Node :
    def __init__(self,value):
        self.value= value
        self.next = None

class Stack:
    def __init__(self):
        self.top=None

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):

        try:
            temp = self.top
            self.top = self.top.next
            return temp.value
        except AttributeError :
            return 'Stack is empty'

    def peek(self):
        try:

            return self.top.value
        except AttributeError :
            return 'Stack is empty'

    def isEmpty(self):
        if self.top:
            return False
        else :
            return True




class Queue:
    def __init__(self):
        self.front = None
        self.rear= None

    def enqueue(self, data):
        node = Node(data)

        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node

    def dequeue(self):
        try:
            temp = self.front
            self.front = self.front.next
            return temp.value
        except AttributeError :
            return 'Queue is empty'


    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            return 'Queue is empty'

    def isEmpty(self):
        if self.front:
            return False
        else :
            return True


if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(6)
    stack.push('cat')
    print(stack.top)
