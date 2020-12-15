from model.node import Node
from model.edge import Edge

class Graph(object):
    def __init__(self):
        self.nodes = list()
        self.edges = list()

    def newNode(self, lineNumber):
        self.nodes.append(Node(lineNumber));

    def getNode(self, index):
        return self.nodes[index-1]

    def addEdge(self, fr, to):
        self.edges.append(Edge(fr, to))

    def getEdge(self, fr, to):
        index = self.edges.index(Edge(fr, to))
        if index != -1:
            return self.edges[index]
        else: 
            return None
