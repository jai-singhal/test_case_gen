import random
import math

class Node(object):
    def __init__(self, lineNumber):
        self.lineNumber = lineNumber
        self.trueConditionNode = None
        self.neutralConditionNode = None
        self.falseConditionNode = None
        self.fitness = self.generate_fitness()
        self.visited = False
        self.feasibleSet = list()
        self.even = True

    @staticmethod
    def generate_fitness():
        return random.randint(0, 1)
     
    def incrementFitness(self):
        self.fitness += 1

    def getFitness(self):
        return self.fitness

    def add_true_cond_node(self, node):
        self.trueConditionNode = node

    def add_neutral_cond_node(self, node):
        self.neutralConditionNode = node

    def add_false_cond_node(self, node):
        self.falseConditionNode = node


    def equals(self, obj):
        if self == obj:
            return True
        
        if obj == None or not isinstance(obj, Node):
            return False

        return self.lineNumber == obj.lineNumber


    def hashCode(self):
        return self.lineNumber

    def add_in_feasible_set(self, node):
        if self.even:
            self.feasibleSet.insert(0, node)
            self.even = False
        else:
            self.feasibleSet.insert(1, node)
            self.even = False
