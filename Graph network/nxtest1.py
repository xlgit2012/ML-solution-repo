# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:29:54 2019

@author: fbai_
"""

import networkx as nx
import matplotlib.pyplot as plt
import json
from networkx.readwrite import json_graph

import pandas as pd

G1 = nx.Graph()
G1.add_edge('A', 'B', weight=4)
G1.add_edge('B', 'D', weight=2)
G1.add_edge('A', 'C', weight=3)
G1.add_edge('C', 'D', weight=4)
nx.shortest_path(G1, 'A', 'D', weight='weight')
G1_jason = json_graph.node_link_data(G1)
json.dump(G1_jason,open('g1.json', 'w'))

G2 = nx.petersen_graph()
G2_jason = json_graph.node_link_data(G2)
json.dump(G2_jason,open('g2.json', 'w'))



afp_graph = nx.Graph()

df = pd.DataFrame(pd.read_csv('k.tau.csv'))

for i in range(len(df)):
    if(df['value'][i]>0.8):
        afp_graph.add_edge(df['response'][i], df['variable'][i], weight=df['value'][i])

        #a = "{:4.2f}".format(df['value'][i])
        #afp_graph.add_edge(df['response'][i], df['variable'][i], weight=a)
        
afp_graph_json = json_graph.node_link_data(afp_graph)
json.dump(afp_graph_json,open('afp_graph.json', 'w'))


fname = "afp_graph.json"
d = json.load(open(fname))
print(d)

# =============================================================================
# G = nx.Graph()
# G.add_nodes_from(d['nodes'])
# G.add_edges_from(d['links'])
# 
# =============================================================================
G2 = json_graph.node_link_graph(d)

#plt.subplot(121)

plt.figure(figsize=(20,20)) 
#pos = nx.circular_layout(G2)
pos = nx.spring_layout(G2)
#pos = nx.random_layout(G2)
#pos = nx.fruchterman_reingold_layout(G2)
nx.draw_networkx_nodes(G2, pos=pos, node_size=500, with_labels=True, font_size=8, node_color='c')
nx.draw_networkx_edges(G2, pos=pos)
nx.draw_networkx_labels(G2, pos=pos,  font_size=8)
#grafo_labels = nx.get_edge_attributes(G2,'weight')
grafo_labels = {i[0:2]:'{:4.2f}'.format(i[2]['weight']) for i in G2.edges(data=True)}
print(grafo_labels)
nx.draw_networkx_edge_labels(G2, pos=pos, edge_labels = grafo_labels, font_size=6)
plt.show()
#plt.savefig("g2.png",dpi=1000)
#plt.subplot(122)
#nx.draw_shell(G2, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')




