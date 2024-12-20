#importing the networkx library
import networkx as nx

#importing the matplotlib library for plotting the graph
import matplotlib.pyplot as plt
G= nx.erdos_renyi_graph(50,0.5)
nx.draw(G, with_labels=True)
plt.show()
