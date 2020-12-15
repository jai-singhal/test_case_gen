
class TestSuite(object):
    def __init__(self):
        self.testCases = list()

    def isTestCasePresent(self, testCase):
        return testCase in self.testCases

    def addTestCase(self, testCase):
        self.testCases.append(testCase)

    def getTestCases(self):
        return self.testCases

    def getTestCase(self, index):
        return self.testCases[index]

    def getSize(self):
        return len(self.testCases)
