class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node


class HashTable:
    def __init__(self, size):
        self.map = [None] * size
        self.size = size

    def hash(self, key):
        try:

            hash_sum = 0
            for char in key:
                hash_sum += ord(char)
            return hash_sum*17 % self.size

        except Exception as error:
            print(f'{error}')



    def add(self, key, value):
        index = self.hash(key)
        if self.map[index] == None:
            self.map[index] = Linkedlist()
            self.map[index].add([key, value])
        else:

            self.map[index].add([key,value])


    def get(self, key):
        idx = self.hash(key)
        if self.map[idx]:
            current = self.map[idx].head
            while current:
                if current.data[0] == key :
                    return current.data[1]
                current = current.next
        else:
            return 'Not in the table'




    def contains(self,key):

        if  self.map[self.hash(key)]:
            return True
        else:
            return False
