class TestCase(object):
    def __init__(self):
        self.variable_set = list()
        self.satisfyingNode = None
        self.satisfyingPath = None

    def addValue(self, testValue):
        self.variable_set.append(testValue)

    def equals(self, obj):
        if self == obj:
            return True
        
        if obj == None or not isinstance(obj, TestCase):
            return False
        if self.variable_set != None:
            return self.variable_set == obj.variable_set
        else:
            return obj.variable_set == None

    def hashCode(self):
        if self.variable_set != None:
            return self.variable_set.hashCode()
        return  0

    def getVariable(self, variableIndex):
        return self.variable_set[variableIndex]

    def getVariableSet(self):
        return self.variable_set;

