from router import Router

class Network:
    def __init__(self):
        self.routers : list[Router] = []

    def add_router(self, router):
        """Add a router to the network."""
        self.routers.append(router)

    def connect_routers(self, router1 : Router, router2 : Router, distance : int):
        """Connect two routers."""
        if router1 not in self.routers or router2 not in self.routers:
            raise Exception

        router1.add_edge(router2.id, distance)
        router2.add_edge(router1.id, distance)
    
    # Here each router sends his informations to other routers
    def send_link_state_packets(self):
        """
            This function simulates the sending of link state packets from all routers, to make the
            other routers know their connections.
            Once this function terminates, each router has created a graph of the network.
            
                Note: this function does not use sequence number to enumerate the link state packets.
        """
        for source_router in self.routers:
            for dest_router in self.routers:
                dest_router.receive_link_state_packet(source_router)

    def calculate_shortest_paths(self):
        """
        This function calculates the shortest path for each router of the network.
        Once this function terminates, each router's routing table has been compiled.
        """
        for router in self.routers:
            router.calculate_shortest_path()
    
    def print_routing_tables(self):
        """Print routing tables for each router of the network."""
        for router in self.routers:
            router.print_routing_table()