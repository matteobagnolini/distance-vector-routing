from network import Network
from router import Router

if __name__ == "__main__":
    nw = Network()
    
    rA = Router("A")
    rB = Router("B")
    rC = Router("C")
    rD = Router("D")
    rE = Router("E")
    rF = Router("F")
    
    nw.add_router(rA)
    nw.add_router(rB)
    nw.add_router(rC)
    nw.add_router(rD)
    nw.add_router(rE)
    nw.add_router(rF)

    nw.connect_routers(rA, rC, 5)
    nw.connect_routers(rA, rB, 2)
    nw.connect_routers(rA, rD, 1)
    nw.connect_routers(rB, rD, 2)
    nw.connect_routers(rB, rC, 3)
    nw.connect_routers(rC, rF, 5)
    nw.connect_routers(rC, rD, 3)
    nw.connect_routers(rC, rE, 1)
    nw.connect_routers(rD, rE, 1)
    nw.connect_routers(rE, rF, 2)
    
        
    nw.send_link_state_packets()       # After this call every router has the map of the network
    
    nw.calculate_shortest_paths()
    
    nw.print_routing_tables()