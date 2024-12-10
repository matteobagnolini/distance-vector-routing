import networkx as nx

class Node:
    def __init__(self, id : str):
        self.id = id
        self.adjacents : nx.Graph = nx.Graph()      # Node's adjacents are represented as a graph

    def add_edge(self, node_id : str, distance : int):
        self.adjacents.add_edge(self.id, node_id, weight=distance)


class Router(Node):
    """This class represents a router inside a network."""
    def __init__(self, id : str):
        Node.__init__(self, id)
        self.network_graph : nx.Graph = nx.Graph()
        self.routing_table : dict[str, tuple[int, str]] = {}    # dest : (cost, next hop)
    
    def receive_link_state_packet(self, router : 'Router'):
        """
        This function simulates the receiving of a link state packet. After each
        call of this function, the router starts building the network graph.
        Once the router received the link state packets of all other routers,
        network graph is completed.
        
        Args:
        router (Router): The router that sent the link state packet.
        """
        self.network_graph = nx.compose(self.network_graph, router.adjacents)  # Current graph is composed with graph received 

    def calculate_shortest_path(self):
        """
        This function calculates the shortest path. After the calculation ended,
        the routing table is compiled using the information obtained by Dijkstra
        algorithm.
        """
        dist, path = nx.single_source_dijkstra(self.network_graph, self.id)     # Dijkstra algorithm is used
        for node in self.network_graph.nodes:
            if node != self.id:
                next_hop = path[node][1]
                self.routing_table[node] = (dist[node], next_hop)

    def print_routing_table(self):
        print("----------------------------------------------")
        print(f"Routing table for router {self.id}:")
        for key in self.routing_table.keys():
            print(f"Node {key}\n\t Cost: {self.routing_table[key][0]}\t Next hop: {self.routing_table[key][1]}")
        print("----------------------------------------------")