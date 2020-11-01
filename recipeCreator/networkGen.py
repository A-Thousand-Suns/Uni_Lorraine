import networkx as nx
import itertools
import matplotlib.pyplot as plt

G = nx.Graph()
path = r'E:\编程文件\python\Uni Lorraine\recipeCreator\nodes.txt'

with open(path, 'r') as file:
    time = 0

    for i in file.readlines():
        time += 1
        nodes = i[:-2].split(' ')
        edges = []
        print(nodes)

        for x in itertools.product(nodes, nodes):

            if x[0]==x[1]:
                continue
            else:
                edges.append(x)
        print(edges)
        G.add_edges_from(edges)

        if time==10:
            break

    pos = nx.shell_layout(G)
    nx.draw(G, pos, with_labels=False, node_size=30)
    plt.show()