from node import Node
from dijkstra import dijkstra
class Router(Node):
    def __init__(self, id):
        Node.__init__(self, id)
        self.network_graph : dict[str, list[tuple[str, float]]] = {}    # graph as adjacent list
    
    def receive_link_state_packet(self, router_id : str, edges : list[tuple[str, float]]):
        if router_id not in self.network_graph:     # if router not in dictionary
            self.network_graph[router_id] = edges
        else:
            for edge in edges:
                self.network_graph[router_id].append(edge)

    def calculate_shortest_path(self):
        dijkstra(self.network_graph)
        
    def print_routing_table(self):
        return None