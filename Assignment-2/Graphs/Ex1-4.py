from collections import deque


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

    def getAdjNodes(self, key: GraphNode):
        return self.adjNodes[key]

    # Ex2
    def dfs(self, key):
        visited = set()
        self.dfs_helper(key, visited)

    def dfs_helper(self, key, visited):
        visited.add(key)
        print(key, end=" ")

        for node in self.adjNodes(key):
            if node not in visited:
                self.dfs_helper(node, visited)

    # Ex3
    def bfs(self, key):
        queue = deque()
        visited = set()
        queue.append(visited)

        while queue:
            node = self.adjNodes.pop(0)
            print(s, end=" ")

            for node_adj in self.adjNodes[node]:
                if node_adj not in visited:
                    visited.add(node_adj)
                    queue.append(node_adj)

    def minNumberOfEdges(self, node1: GraphNode, node2: GraphNode):
        queue = deque()
        visited = set(node1)
        queue.append(visited)

        while queue:
            numberEdges = queue.pop(0)
            node = queue.pop(0)
            if node in visited:
                return numberEdges

            for node_adj in self.adjNodes[node]:
                if node_adj not in visited:
                    visited.add(node_adj)
                    queue.append(node_adj)

            

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
    
    # graph.addEdge(GraphNode(7), GraphNode(2))
    # graph.addEdge(GraphNode(7), GraphNode(4))
    # graph.addEdge(GraphNode(2), GraphNode(4))
    # graph.addEdge(GraphNode(2), GraphNode(0))
    # graph.addEdge(GraphNode(6), GraphNode(4))
    # graph.addEdge(GraphNode(6), GraphNode(0))

    # print(graph.getAdjNodes(GraphNode(7)))
