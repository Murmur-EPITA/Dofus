from networkx import Graph, shortest_path

class GraphMap:
    def __init__(self, maps: dict):
        print("Initializing graph.")
        self.graph: Graph = Graph()
        self.graph.add_nodes_from(maps['Amaknien'].keys())
        for id, square in maps['Amaknien'].items():
            self.graph.add_edges_from([id, adj] for adj in square.adjs if adj is not None)
        print("Graph initialized.")

    def shortest_path(self, idSource: str, idDestination: str):
        return shortest_path(self.graph, idSource, idDestination)[1:]
