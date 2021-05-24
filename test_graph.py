import graph_algorithms.adjaceny_matrix_graph as matrix

g = matrix.AdjacencyMatrixGraph(4)

print("Undirected Graph (Adjacency)")
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)

g.display()

print("Directed Graph (Adjacency)")
g = matrix.AdjacencyMatrixGraph(4, True)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)

g.display()
