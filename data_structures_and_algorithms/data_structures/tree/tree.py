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
    bt.root = Node(5)
    bt.root.right = Node(10)
    bt.root.left = Node(-2)
    bt.root.right.left = Node(5)
    bt.root.left.left = Node(17)
    bt.root.right.right = Node(8)
    print(bt.preorder())
    print(bt.breadth_first_traversal(bt.root))
    bst = BinarySearchTree()
    bst.add(3)
    bst.add(6)
    bst.add(4)
    bst.add(8)
    bst.add(2)
    bst.add(7)
    bst.add(-1)
    bst.add(5)


    assert bst.root.value == 3
    assert bst.root.left.value == 2
    assert bst.root.left.left.value == -1
    assert bst.root.right.value == 6
    assert bst.root.right.left.value == 4
    assert bst.root.right.left.right.value == 5
    assert bst.root.right.right.value == 8
    assert bst.root.right.right.left.value == 7
    print('==========pass=============')
    print(bst.contains(11))
    print(bst.contains(-1))
    print(bst.contains(1))
    print(bst.find_maximum_value())





