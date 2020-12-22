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

        try :
            output = []
            def _walk(node):
                output.append(node.value)
                if node.left:
                    _walk(node.left)
                if node.right:
                    _walk(node.right)

            _walk(self.root)

            return output
        except Exception as error:
            return f'An error occured during excuting: {error}'

def fizz_buzz_tree(tree):
    new =[]
    def _walk (node):

        if int(node.value) %15==0:
            new.append('FizzBuzz')

        elif int(node.value) %3==0:
            new.append('Fizz')

        elif int(node.value) %5==0:
            new.append('Buzz')

        else:
            new.append(node.value)
        if node.left:
            _walk(node.left)
        if node.right:
            _walk(node.right)

    _walk(tree.root)
    return new


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(10)
    tree.root.right = Node(15)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(3)
    tree.root.right.right = Node(9)
    tree.root.right.left = Node(4)
    print(fizz_buzz_tree(tree))

