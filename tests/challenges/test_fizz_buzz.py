from data_structures_and_algorithms.challenges.fizz_buzz_tree.fizz_buzz_tree import Node,BinaryTree,fizz_buzz_tree


def test_fizz_buzz():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(10)
    tree.root.right = Node(15)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(3)
    tree.root.right.right = Node(9)
    tree.root.right.left = Node(4)
    actual = fizz_buzz_tree(tree)
    expect = [2, 'Buzz', 'Buzz', 'Fizz', 'FizzBuzz', 4, 'Fizz']
    assert actual == expect
