from network import Network
from router import Router

if __name__ == "__main__":
    nw = Network()
    
    r1 = Router(10)
    r2 = Router(20)
    r3 = Router(30)
    
    nw.add_router(r1)
    nw.add_router(r2)
    nw.add_router(r3)

    nw.connect_routers(r1, r2, 3)
    nw.connect_routers(r2, r3, 7)
    
    nw.send_link_state_packets()
    
    print(r3.network_graph)