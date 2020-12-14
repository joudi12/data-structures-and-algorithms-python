from data_structures_and_algorithms.stacks_and_queues.stacks_and_queues import Node,Queue
class Dog:
    type = 'dog'
    def __init__(self,name):
        self.name = name

class Cat:
    type = 'cat'
    def __init__(self,name):
        self.name = name

class AnimalShelter():
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self,animal):
        try:
            if animal.type == 'cat':
                self.cats.enqueue(animal)
            elif animal.type == 'dog':
                self.dogs.enqueue(animal)
        except AttributeError as e:
            return 'Add Cat or Dog Only'

    def dequeue(self,pref):

        try:
            if pref == 'cat':
                cat = self.cats.dequeue()
                return cat.name
            elif pref == 'dog':
                dog = self.dogs.dequeue()
                return dog.name
        except AttributeError as e:
            return None
