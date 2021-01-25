from data_structures_and_algorithms.data_structures.graphs.graphs import Graph


def get_edge(graph,cities):
    sum=0
    arr = []
    for i in range(len(cities)):
        neighbors=graph.get_neighbours(cities[i])
        for j in neighbors:
            arr.append(j[0])
        if i+1==len(cities):
            break
        if cities[i+1] in arr:
            nm= graph.adjacency_list[cities[i+1]]
            for k in nm:
                if k[0]== cities[i]:
                    sum+=k[1]
        else:
            return 0,False
    return True,sum
if __name__=='__main__':
    cities=['Pandora','Metroville', 'Narnia']
    graph=Graph()
    graph.add_node('Pandora')
    graph.add_node('Metroville')
    graph.add_node('Narnia')
    graph.add_node('Naboo')
    graph.add_node('Arendelle')
    graph.add_node('Monstropolis')
    graph.add_edge('Pandora','Arendelle',150)
    graph.add_edge('Pandora','Metroville',82)
    graph.add_edge('Metroville','Narnia',37)
    # print(graph.adjacency_list)
    print(get_edge(graph,cities))
