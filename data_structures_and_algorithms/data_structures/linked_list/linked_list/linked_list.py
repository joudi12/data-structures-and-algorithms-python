
class Node :
    def __init__(self,value):
        self.value=value
        self.next=None





class LinkedList:

    def __init__(self):
        self.head=None


    def insert(self,data):
        """
         Takes any value as an argument and adds a new node with that value to the head of the list.

         Arguments:
            a value to be added to the list
        """
        try:
            node = Node(data)
            if self.head ==None:
                self.head=node
            else:
                node.next= self.head
                self.head=node
        except Exception as error:
            print(f'this is error in this method {error}')




    def includes(self,data):
        """
         method which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node's value somewhere within the list.

         Arguments:
            a value to search for
        """
        try:
            current = self.head
            while current !=None:
                if current.value ==data:
                    return True
                else:
                    current=current.next
            return False
        except Exception as error:
            print(f'this is error in this method {error}')


    def __str__(self):
        """
         method which takes in no arguments and returns a string representing all the values in the Linked List,
          output =
           "{ a } -> { b } -> { c } -> NULL"
        """
        try:
            string =''
            current = self.head
            while current!=None:
                string+=f'{{ {current.value} }} -> '
                current=current.next
                if current == None:
                    string+= 'NULL'
            return string
        except Exception as error:
            print(f'this is error in this method {error}')







if __name__ == "__main__":
    node1 = Node(5)
    nodee=LinkedList()
    print(node1.value)
    nodee.insert(5)
    nodee.insert(7)
    nodee.insert(5)
    print(nodee)
    print(nodee.includes(5))
    print(nodee.__str__())



