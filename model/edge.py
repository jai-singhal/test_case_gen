import random
import math

class Edge(object):
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        self.pheromoneLevel = 1
        self.heuristicValue = 2
        self.probability = 0

    def equals(self, obj):
        if self == obj:
            return True
        
        if obj == None or not isinstance(obj, self):
            return False

        if self.head != None:
            return head.equals(obj.head)
        else:
            return obj.head == None

        if self.tail != None:
            return self.tail.equals(obj.tail)
        else:
            return obj.tail == None       

    def hashCode(self):
        result = None
        if self.head != None:
            result = self.head.hashCode()
        else:
            result = 0
        if self.tail != None:
            result = 31 * result + self.tail.hashCode()
        else:
            result = 31 * result
        
        return result;

    def updatePheromoneLevel(self, alpha, beta):
        self.pheromoneLevel = math.pow(self.pheromoneLevel, alpha) + math.pow(self.heuristicValue, -beta);

    def updateHeuristicValue(self):
        self.heuristicValue *= 2;

