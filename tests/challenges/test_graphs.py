from data_structures_and_algorithms.data_structures.graphs.graphs import Graph
import pytest

def test_add_to_graph():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    assert list(g.adjacency_list.keys()) == ['a', 'b']

def test_add_edge():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a' , 'b' , 2)
    g.add_edge('a' , 'c' , 9)
    assert g.adjacency_list['a'][0] == ('b' , 2)
    assert g.adjacency_list['a'][0][0] == 'b'
    assert g.adjacency_list['a'][0][1] == 2
    assert g.adjacency_list['a'][1] == ('c' , 9)
    assert g.adjacency_list['a'][1][0] == 'c'
    assert g.adjacency_list['a'][1][1] == 9


def test_retrieve_nodes():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    assert g.get_nodes() == ['a', 'b']

def test_retrieve_neighbors():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_edge('a' , 'b' , 2)
    g.add_edge('a' , 'c' , 9)
    assert g.get_neighbours('a') == [('b' , 2) , ('c' , 9)]

def test_graph_size():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    assert g.size() == 2

def test_one_node_no_edges():
    g = Graph()
    g.add_node('a')
    assert g.get_neighbours('a') == []

def test_empty_graph():
    g = Graph()
    assert g.get_nodes() == []




