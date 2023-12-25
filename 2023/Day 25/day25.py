import networkx as nx
import matplotlib.pyplot as plt


lines = [x.split() for x in open("D:/GitHub/Advent-Of-Code/2023/Day 25/input.txt").read().splitlines()]

g = nx.Graph()

for line in lines:
  start_node = line[0][:-1]
  for node in line[1:]:
    g.add_edge(start_node, node)


network_dict = {}

for line in lines:
  start_node = line[0][:-1]
  network_dict[start_node] = []
  for node in line[1:]:
    network_dict[start_node].append(node)

hanging_threads = [['ddl', 'lcm'], ['rrl', 'pcs'], ['mbk', 'qnd']]
#hanging_threads = [['bvb', 'cmg'], ['jqt', 'nvd'], ['hfx', 'pzl']]
print(g.number_of_nodes())

for node1, node2 in hanging_threads:
  g.remove_edge(node1, node2)

# nx.draw(g, with_labels = True)
# plt.savefig("D:/GitHub/Advent-Of-Code/2023/Day 25/sever.png")
  

networks = list(g.subgraph(c) for c in nx.connected_components(g))

print(networks[0].number_of_nodes()*networks[1].number_of_nodes())