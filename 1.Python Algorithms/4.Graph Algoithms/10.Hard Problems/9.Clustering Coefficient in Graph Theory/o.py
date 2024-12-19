import networkx as nx
G=nx.erdos_renyi_graph(10,0.4)
cc=nx.average_clustering(G)
cc
#Output of Global CC
0.08333333333333333
c=nx.clustering(G)
c
# Output of local CC
{0: 0.0, 1: 0.3333333333333333, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0,7: 0.3333333333333333,
 8: 0.0, 9: 0.16666666666666666}
