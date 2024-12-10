from router import Router

class Network:
    def __init__(self):
        self.routers = []

    def add_router(self, router):
        self.routers.append(router)

    def connect_routers(self, router1 : Router, router2 : Router, distance : int):
        if router1 not in self.routers or router2 not in self.routers:
            raise Exception
        router1.add_edge(router2.id, distance)
        router2.add_edge(router1.id, distance)
    
    # Here each router sends his informations to other routers
    def send_link_state_packets(self):
        for source_router in self.routers:
            for dest_router in self.routers:
                dest_router.receive_link_state_packet(source_router)

    def calculate_shortest_paths(self):
        for router in self.routers:
            router.calculate_shortest_path()
    
    def print_routing_tables(self):
        for router in self.routers:
            print("Router " + router.id + ": " + router.print_routing_table())