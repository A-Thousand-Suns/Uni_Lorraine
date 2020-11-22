import networkx as nx
import pickle
import matplotlib.pyplot as plt


network_path = r'E:\编程文件\python\Uni Lorraine\recipeCreator\network.pkl'
G = nx.Graph()

with open(network_path, 'rb') as file:
    network = pickle.load(file)

print(network)

for edge, weight in network.items():
    G.add_weighted_edges_from([(edge[0], edge[1], weight)])

pos = nx.shell_layout(G)
nx.draw(G, pos, with_labels=False, node_size=30)
plt.show()

