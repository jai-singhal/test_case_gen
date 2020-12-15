from model.path import Path

class Paths(object):
    def __init__(self):
        self.paths = list()

    def contains(self, newPath):
        return newPath in self.paths

    def addPath(self, newPath):
        self.paths.append(newPath)

    def getSize(self):
        return len(self.paths)

    def getPathHavingPathNumber(self, pathNumber):
        if pathNumber > len(self.paths):
            return -1
        return self.paths[pathNumber]

    def getPathNumberHavingNode(self, nodeNumber):
        pathNumber = 0
        for path in self.paths:
            if path.contains(nodeNumber):
                break
            pathNumber+=1

        if pathNumber == 7:
            return -1
        return pathNumber

    def setPathVisited(self, pathNumber):
        # print("Pth number: ", pathNumber)
        # print("Paths", self.paths)
        self.paths[pathNumber-1].setVisited(True)

    def getPaths(self):
        return self.paths

    def fitnessOfPath(self, solved, unsolved):
        fitness = 0
        for nodeFromUnsolved in unsolved.getNodes():
            for nodeFromSolved in solved.getNodes():
                if nodeFromSolved.equals(nodeFromUnsolved):
                    fitness += 1
        return fitness

