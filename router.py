from node import Node
import networkx as nx
from dijkstra import dijkstra

class Router(Node):
    def __init__(self, id : str):
        Node.__init__(self, id)
        self.network_graph : nx.Graph = nx.Graph()    # graph as adjacent list
        self.routing_table : dict[str, tuple[int, str]] = {}     # dest : (cost, next hop)
    
    def receive_link_state_packet(self, router):
        self.network_graph = nx.compose(self.network_graph, router.edges)  # Add the edges of other graph to the current graph

    def calculate_shortest_path(self):
        dist, path = nx.single_source_dijkstra(self.network_graph, self.id)
        # Here we need to find the routing table from the pred dictionary
        for node in self.network_graph.nodes:
            if node != self.id:
                self.routing_table[node] = (dist[node], path[node][1])

    def print_routing_table(self):
        print("----------------------------------------------")
        print(f"Routing table for router {self.id}:")
        for key in self.routing_table.keys():
            print(f"Node {key}\n\t Cost: {self.routing_table[key][0]}\t Next hop: {self.routing_table[key][1]}")
        print("----------------------------------------------")