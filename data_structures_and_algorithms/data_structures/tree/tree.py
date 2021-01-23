class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.max =0


    def preorder(self):
        #1. Initialize
        try :
            output = []
            #2. Define the closure
            def _walk(node):
                output.append(node.value)
                if node.left:
                    _walk(node.left)
                if node.right:
                    _walk(node.right)

            #3. Call the closure with initial value
            _walk(self.root)
            #4. Return the result
            return output
        except Exception as error:
            return f'An error occured during excuting: {error}'
    def inorder(self):
        try:

            output=[]
            def _walk(node):
                if node.left:
                    _walk(node.left)
                output.append(node.value)
                if node.right:
                    _walk(node.right)
            _walk(self.root)
            return output
        except Exception as error:
            return f'An error occured during excuting: {error}'

    def postOrder(self):
        try:

            output=[]
            def _walk(node):
                if node.left:
                    _walk(node.left)
                if node.right:
                    _walk(node.right)
                output.append(node.value)


            _walk(self.root)
            return output
        except Exception as error:
            return f'An error occured during excuting: {error}'
    def find_maximum_value(self):
        try:
            if not self.root:
                return'Tree is Empty'

            def _walk(node):
                if node.value > self.max:
                    self.max = node.value
                if node.left:
                    _walk(node.left)

                if node.right:
                    _walk(node.right)


            _walk(self.root)
            return self.max
        except Exception as error:
            return f'An error occured during excuting: {error}'

    def breadth_first_traversal(self, tree):
        try:
            queue = []
            result = []
            if not tree:
                return 'Tree is empty'
            else:
                if tree:
                    queue.append(tree)
                while queue:
                    current = queue.pop(0)
                    result.append(current.value)
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
            return result
        except Exception as error:
            return f'An error occured during excuting: {error}'

###### recercion################
# def is_bst(bt):
#     if not bt.root:
#             return 'empty tree'
#     node=bt.root
#     isBST=True
#     def _walk(node):
#         nonlocal isBST
#         # if not node:
#         #     return
#         if node.left:
#             if node.left.value>=node.value:
#                 isBST=False
#                 return isBST
#             else:
#                 _walk(node.left)
#         if node.right:
#             if node.right.value<node.value:
#                 isBST=False
#                 return isBST
#             else:
#                 _walk(node.right)
#         return isBST
#     return _walk(node)

def invert(bt):
	temp = []
	if bt.root ==None :
		return 'wrong'
	else :
		temp.append(bt.root)
	while temp :
		node = temp.pop(0)

		if node.left :
			temp.append(node.left)
			temp1 = node.left
		else:
			temp1 = None
		if node.right:
			temp.append(node.right)
			node.left = node.right
			node.right = temp1
		else:
			node.right = node.left
			node.left = None
	return bt

####### level###############
def is_bst(bt):
    if not bt.root:
        return'empty'
    q = []
    boolen = True
    q.append(bt.root)
    while q :
        node = q.pop(0)
        if node.left  :
            if node.left.value> node.value:
                boolen= False
                return boolen
            else :
                q.append(node.left)
        if node.right  :
            if node.right.value < node.value:
                boolen= False
                return boolen
            else :
                q.append(node.right)
    return boolen
################next right####################
def next(tree,num):
    temp = []
    next_q = 0
    if tree.root == None:
        return 'rmpty'
    temp.append(tree.root)
    if tree.root.value == num :
        next_q = tree.root.right
        return next_q.value
    while temp :
        current = temp.pop(0)
        if current.value == num:
            next_q = temp[0]
            return next_q


        if current.left:
            temp.append(current.left)
        if current.right:
            temp.append(current.right)
        else:
            temp.append(None)
        print(temp)

    return next_q


class BinarySearchTree(BinaryTree):
    def add(self, value):
        try:
            if not self.root:
                self.root = Node(value)
            else:
                def _walk(node):
                    if value < node.value:
                        # go left
                        if not node.left:
                            node.left = Node(value)
                            return
                        else:
                            _walk(node.left)
                    else:
                        # go right
                        if not node.right:
                            node.right = Node(value)
                            return
                        else:
                            _walk(node.right)
                _walk(self.root)
        except Exception as error:
            return f'An error occured during excuting: {error}'



    def contains(self, value):
        try:

            if self.root == value:
                return True
            else:
                def _walk(node):
                    if node:
                        if value == node.value :
                            return True
                        elif value<node.value:
                            return _walk(node.left)
                        elif value>node.value:
                            return _walk(node.right)
                    return False
                return _walk(self.root)
        except Exception as error:
            return f'An error occured during excuting: {error}'



if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(10)
    bt.root.right = Node(20)
    bt.root.left = Node(7)
    bt.root.right.left = Node(11)
    bt.root.left.left = Node(55)
    bt.root.right.right = Node(28)
    print(next(bt,55))
    # print(bt.preorder())
    # print(invert(bt))
    # print(bt.root.left.value)
    # print(bt.root.right.right.value)
    # # print(bt.root.right.left.value)
    # print(bt.root.left.left.value)
    # print(bt.root.left.right.value)
    # bst = BinarySearchTree()
    # bst.add(3)
    # bst.add(6)
    # bst.add(4)
    # bst.add(8)
    # bst.add(2)
    # bst.add(7)
    # bst.add(-1)
    # bst.add(5)


    # assert bst.root.value == 3
    # assert bst.root.left.value == 2
    # assert bst.root.left.left.value == -1
    # assert bst.root.right.value == 6
    # assert bst.root.right.left.value == 4
    # assert bst.root.right.left.right.value == 5
    # assert bst.root.right.right.value == 8
    # assert bst.root.right.right.left.value == 7
    # print('==========pass=============')
    # print(bst.contains(11))
    # print(bst.contains(-1))
    # print(bst.contains(1))
    # print(bst.find_maximum_value())





