from networkx import draw, Graph
from matplotlib.pylab import show
from src.graph.graph import CustomGraph



graph = CustomGraph()
graph.matrix_adj = [[0, 1, 1], [1, 0, 1], [0, 1, 0]]
graph.list_arc_from_matr_adj()
graph.list_adj_from_matix_adj()
graph.matrix_incedent_from_matix_adj()


def _draw():
    g = Graph()
    g.add_edges_from(graph.list_arc)
    draw(g, with_labels=True)
    show()


while True:
    option = input()
    if option == "vert":
        graph.add_vert()
    if option == "arc":
        a = int(input())
        b = int(input())
        graph.add_arc(a, b)
    if option =="draw":
        _draw()
    if option == "adj_matrix":
        print(graph.matrix_adj)
    if option == "incedent_matrix":
        print(graph.matrix_incidence)
    if option == "adj_list":
        print(graph.list_adj)
    if option == "arc_list":
        print(graph.list_arc)
    if option == "del_arc":
        a = int(input())
        b = int(input())
        graph.del_arc(a, b)
    if option == "dfs":
        s = int(input())
        graph.dfs_path(s)
    if option == "kruskal":
        print(graph.kruskal())
    if option == "exit":
        break


