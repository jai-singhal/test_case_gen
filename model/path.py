from model.node import Node

class Path(object):
    def __init__(self):
        self.nodes = list()
        self.visited = False
        self.set_values = 0
        self.temp_fitness = 0
        self.fitness_value = 0
        self.probability = 0
        self.strength = 0

    def loopOptimization(self, startNode):
        for node in self.nodes:
            if (startNode.lineNumber == node.lineNumber):
                node.incrementFitness()

    def addNode(self, node):
        self.nodes.append(node)

    def equals(self, obj):
        if self == obj:
            return True
        
        if obj == None or not isinstance(obj, self):
            return False

        if self.nodes is not None:
            return self.nodes == obj.nodes
        else:
            return obj.nodes == None

    def hashCode(self):
        if self.nodes != None:
            return nodes.hashCode() 
        return 0


    def contains(self, nodeNumber):
        newNode = Node(nodeNumber)
        return newNode in self.nodes

    def setVisited(self, visited):
        self.visited = visited

    def isNodePresent(self, node):
        return node in self.nodes

    def setSetValue(self, setValue):
        self.setValue = setValue

    def isVisited(self):
        return self.visited

    def getSetValue(self):
        return self.setValue

    def setTempFitness(self, tempFitness):
        self.tempFitness = tempFitness

    def getTempFitness(self):
        return self.tempFitness

    def setFitnessValue(self, fitnessValue):
        self.fitness_value = fitnessValue

    def getFitnessValue(self):
        return self.fitness_value

    def getNodes(self):
        return self.nodes

    def setProbability(self, probability):
        self.probability = probability

    def getProbability(self):
        return self.probability

    def getNode(self, index):
        if index > len(self.nodes):
            return -1
        return self.nodes[index]

