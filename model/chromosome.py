import random
import math

class Chromosome(object):
    def __init__(self):
        self.binary_data = list()
        self.decimal_data = list()
        self.reat_data = list()
        self.fitness = None
        self.nodeCovered = None
        self.rft = None
        self.cft = None

    def initialize_binary_data(self, m):
        for i in range(0, m):
            self.binary_data.append(random.randint())

    def binary_to_decimal(self, inputVariables):
        for j in range(0, inputVariables):
            for i in range((5 * j), (5 * (j + 1))):
                if self.binary_data[i] == 1:
                    self.decimal_data.insert(j, self.decimal_data[j] + int(math.pow(2, 5 - 1 - (i % 5))))
   
    def decimal_to_real(self, inputVars, m):
        intermediate = 19.0 / (math.pow(2, m) - 1)
        for i in range(0, inputVars):
            self.reat_data.insert(i, 1 + (self.decimal_data[i] * intermediate));

