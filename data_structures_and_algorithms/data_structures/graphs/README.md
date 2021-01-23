# Graph ;)


## Here is some common terminology used when working with Graphs:

- Vertex - A vertex, also called a “node”, is a data object that can have zero or more adjacent vertices.
- Edge - An edge is a connection between two nodes.
- Neighbor - The neighbors of a node are its adjacent nodes, i.e., are connected via an edge.
- Degree - The degree of a vertex is the number of edges connected to that vertex.
- Challenge
- Implement a graph, the graph should be represented as an adjacency list, with the ability to add new vertices, - add thier edgees, and retrieve the all nodes and neighbors.

## API

- add_node():
### Adds a new node to the graph.Takes in the value of that node.Returns the added node.
- add_edge():
### Adds a new edge between two nodes in the graph. Include the ability to have a “weight”. Takes in the two nodes to be connected by the edge. Both nodes should already be in the Graph.
- get_nodes():
### Returns all of the vertexes in the graph as a collection.
- get_neighbors():
### Returns a collection of edges connected to the given node.Takes in a given node.Include the weight of the connection in the returned collection.
- size():
### Returns the total number of nodes in the graph.Approach & Efficiency


## The graph class passes the following tests successfully:

1. Node can be successfully added to the graph
2. An edge can be successfully added to the graph
3. A collection of all nodes can be properly retrieved from the graph
4. All appropriate neighbors can be retrieved from the graph
5. Neighbors are returned with the weight between nodes included
6. The proper size is returned, representing the number of nodes in the graph
7. A graph with only one node and edge can be properly returned
8. An empty graph properly returns null
