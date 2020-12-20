import pytest


from data_structures_and_algorithms.data_structures.tree.tree import Node,BinarySearchTree,BinaryTree
def test_empty():
    bt = BinaryTree()
    assert bt.root == None
def test_single_root():
    bt = BinaryTree()
    bt.root = Node(5)
    assert bt.root.value == 5
def test_leftchild_rightchild():
    bt = BinaryTree()
    bt.root =Node(5)
    bt.root.left =Node(4)
    bt.root.right = Node(3)
    assert bt.root.value ==5
    assert bt.root.left.value ==4
    assert bt.root.right.value ==3
    assert bt.preorder() ==[5, 4,3]

def test_preorder(prep):
    actual = prep.preorder()
    expected = [5,-2,17,10,5,8]
    assert actual == expected
def test_inorder(prep):
    actual = prep.inorder()
    expected = [17,-2,5,5,10,8]
    assert actual == expected
def test_postorder(prep):
    actual = prep.postOrder()
    expected = [17,-2,5,8,10,5]
    assert actual == expected
def test_maximum_value(prep):
    actual = prep.find_maximum_value()
    expected = 17
    assert actual == expected

def test_maximum_value_empty_tree():
    bt = BinaryTree()
    actual = bt.find_maximum_value()
    expected = "Tree is Empty"
    assert actual == expected

@pytest.fixture
def prep():
    bt = BinaryTree()
    bt.root = Node(5)
    bt.root.right = Node(10)
    bt.root.left = Node(-2)
    bt.root.right.left = Node(5)
    bt.root.left.left = Node(17)
    bt.root.right.right = Node(8)
    return bt
