class Node:
    def __init__(self, id : str):
        self.id = id
        self.edges : list[tuple[str, int]] = []   # This list of tuple represent node <-> distance

    def add_edge(self, node_id : str, distance : int):
        self.edges.append((node_id, distance))
