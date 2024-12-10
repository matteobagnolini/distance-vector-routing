from network import Network
from router import Router

if __name__ == "__main__":
    nw = Network()
    
    r1 = Router("A")
    r2 = Router("B")
    r3 = Router("C")
    
    nw.add_router(r1)
    nw.add_router(r2)
    nw.add_router(r3)

    nw.connect_routers(r1, r2, 3)
    nw.connect_routers(r2, r3, 7)
    
    nw.send_link_state_packets()       # After this call every router has the map of the network
    
    nw.calculate_shortest_paths()
    
    r1.print_routing_table()
    r2.print_routing_table()
    r3.print_routing_table()