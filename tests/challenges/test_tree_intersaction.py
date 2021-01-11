from data_structures_and_algorithms.challenges.tree_intersection.tree_intersection import tree_intetsaction
from data_structures_and_algorithms.data_structures.tree.tree import BinaryTree ,Node

def test_test_three_common():
    tr1=BinaryTree()
    tr2 = BinaryTree()
    tr1.root = Node(5)
    tr1.root.right = Node(10)
    tr1.root.left = Node(-2)
    tr1.root.right.left = Node(15)
    tr1.root.left.left = Node(17)
    tr2.root = Node(5)
    tr2.root.right = Node(11)
    tr2.root.left = Node(-2)
    tr2.root.right.left = Node(15)
    tr2.root.left.left = Node(111)
    assert tree_intetsaction(tr1,tr2) == [5,-2,15]

def test_test_empty_tree():
    tr1=BinaryTree()
    tr2 = BinaryTree()
    assert tree_intetsaction(tr1,tr2) == []

def test_test_with_string():
    tr1=BinaryTree()
    tr2 = BinaryTree()
    tr1.root = Node(5)
    tr1.root.right = Node('joudi')
    tr1.root.left = Node(-2)
    tr1.root.right.left = Node(15)
    tr1.root.left.left = Node(17)
    tr2.root = Node(5)
    tr2.root.right = Node(11)
    tr2.root.left = Node(-2)
    tr2.root.right.left = Node(15)
    tr2.root.left.left = Node('joudi')
    assert tree_intetsaction(tr1,tr2) == [5,-2,'joudi',15]

def test_test_with_one_node():
    tr1=BinaryTree()
    tr2 = BinaryTree()
    tr1.root = Node(5)
    assert tree_intetsaction(tr1,tr2) == []


