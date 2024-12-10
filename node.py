import networkx as nx

class Node:
    def __init__(self, id : str):
        self.id = id
        self.edges : nx.Graph = nx.Graph()

    def add_edge(self, node_id : str, distance : int):
        self.edges.add_edge(self.id, node_id, weight=distance)
        
