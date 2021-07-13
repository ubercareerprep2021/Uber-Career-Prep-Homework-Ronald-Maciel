class GraphNode:
    def __init__(self, data):
        self.data = data

class GraphWithAdjacencyList:
    def __init__(self):
        self.adjNodes = {}
        
    def addNode(self, key: GraphNode):
        self.adjNodes[key] = []

    def removeNode(self, key: GraphNode):
        self.adjNodes.pop(key)

    def addEdge(self, node1: GraphNode, node2: GraphNode):
        self.adjNodes[node1].append(node2)
        self.adjNodes[node2].append(node1)

    def removeEdge(self, node1: GraphNode, node2: GraphNode):
        self.adjNodes[node1].remove(node2)
        self.adjNodes[node2].remove(node1)


if __name__ == "__main__":
    graph = GraphWithAdjacencyList()

    node_7 = GraphNode(7)
    node_2 = GraphNode(2)
    node_4 = GraphNode(4)
    node_6 = GraphNode(6)
    node_0 = GraphNode(0)
    
    graph.addNode(GraphNode(7))
    graph.addNode(GraphNode(2))
    graph.addNode(GraphNode(4))
    graph.addNode(GraphNode(6))
    graph.addNode(GraphNode(0))
    
    graph.addEdge(GraphNode(7), GraphNode(2))
    graph.addEdge(GraphNode(7), GraphNode(4))
    graph.addEdge(GraphNode(2), GraphNode(4))
    graph.addEdge(GraphNode(2), GraphNode(0))
    graph.addEdge(GraphNode(6), GraphNode(4))
    graph.addEdge(GraphNode(6), GraphNode(0))
