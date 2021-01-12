
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


    def append(self,value):
        """
           Takes any value as an argument and adds a new node with that value to the end of the list.

           Arguments:
               a value to be added to the list
        """
        try:
            node =Node(value)
            if self.head ==None:
                self.head=node
            else:
                current = self.head
                while current.next !=None:
                    current=current.next
                current.next=node
        except Exception as error:
            print(f'this is error in this method {error}')


    def insert_before(self,value, newVal):


        try:
            node =Node(newVal)
            if not self.head:
                self.head = node
            else:
                # To add before the first node
                if self.head.value == value:
                        swap = self.head
                        self.head = node
                        node.next = swap
                        return
                else:

                    current = self.head
                    while current.next != None:
                        if current.next.value == value:
                            swap = current.next
                            current.next = node
                            node.next = swap
                            return
                        else:
                            current = current.next

                    return "this node doesn't exist!"
        except Exception as error:
            print(f'this is error in this method {error}')



    def insert_after(self,value, newVal):
        try:
            node=Node(newVal)
            if self.head ==None:
                self.head=node
            else:
                current = self.head
                while current:
                    if current.value == value:
                        node.next = current.next
                        current.next = node

                        break

                    else:
                        current = current.next

                return "this node doesn't exist!"
        except Exception as error:
            print(f'this is error in this method {error}')



    def kth_from_end(self, k):


        try:


            counter = -1
            current = self.head
            while current:
                current = current.next
                counter = counter + 1
            if counter >= k:
                current = self.head
                for i in range(counter - k):
                    current = current.next
                return current.value
            else:
                return 'The Value Not Found'

        except:
            return "The Value Not Found"













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



# def getIntersectionNode( headA, headB):
#     curA,curB = headA,headB
#     lenA,lenB = 0,0
#     while curA is not None:
#         lenA += 1
#         curA = curA.next
#     while curB is not None:
#         lenB += 1
#         curB = curB.next
#     curA,curB = headA,headB
#     if lenA > lenB:
#         for i in range(lenA-lenB):
#             curA = curA.next
#     elif lenB > lenA:
#         for i in range(lenB-lenA):
#             curB = curB.next
#     while curB.value != curA.value:
#         curB = curB.next
#         curA = curA.next
#     return curA.value





if __name__ == "__main__":
    # node1 = Node(5)
    # nodee=LinkedList()
    # # print(node1.value)
    # nodee.insert(5)
    # nodee.insert(7)
    # nodee.insert(2)
    # # print(nodee)
    # # print(nodee.includes(5))
    # # print(nodee.__str__())
    # print(nodee.insert_Before(2,3))
    # ll = LinkedList()
    # ll.append(1)
    # ll.append(6)
    # ll.append(9)
    # ll.append(4)
    # ll.insert_after(1,3)
    # print(ll.__str__())
    li1=LinkedList()
    # li1.append(4)
    li1.append(-9)
    li1.append('joudi')
    li1.append(2)
    li1.append(3)
    li1.append(4)
    li2=LinkedList()
    li2.append(99)
    li2.append(1)
    li2.append(2)
    li2.append(3)
    li2.append(4)
    print(li1)
    print(li1.kth_from_end(3))


