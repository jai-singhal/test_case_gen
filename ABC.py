import math
import random

from model.graph import Graph
from model.path import Path
from model.paths import Paths
from model.test_case import TestCase
from model.test_suite import TestSuite


class ABC_Algorithm(object):
    def __init__(self):
        self.iteration = 0

    def get_cf_paths(self, program):
        complexity = program.complexity
        startNode = program.cfgRoot
        paths = Paths()

        for i in range(1, (2 * complexity + 1)):
            newPath = self.generate_new_path(startNode)
            if not paths.contains(newPath):
                paths.addPath(newPath)

        return paths

    def generate_new_path(self, startNode):
        newPath = Path()
        self.generate_path_for_node(startNode, newPath)
        return newPath

    def generate_path_for_node(self, node, newPath):
        newPath.loopOptimization(node)
        newPath.addNode(node)
        if node.trueConditionNode == None:
            return
        if node.falseConditionNode == None:
            node.trueConditionNode.incrementFitness()
            self.generate_path_for_node(node.trueConditionNode, newPath)
        else:
            if node.trueConditionNode.getFitness() < node.falseConditionNode.getFitness():
                node.trueConditionNode.incrementFitness()
                self.generate_path_for_node(node.trueConditionNode, newPath)
            else:
                node.falseConditionNode.incrementFitness()
                self.generate_path_for_node(node.falseConditionNode, newPath)


    def test_suite_gen(self, paths, program):
        testSuite = TestSuite()

        self.initialise_test_cases(testSuite, paths, program)
        self.evaluate_test_cases(testSuite, paths, program)
        numberOfSets = int(math.sqrt(paths.getSize()))
        self.divide_into_sets(paths, program)
        self.iteration = 0

        while not self.check_path_satisfaction(paths) and self.iteration < 50:
            for setValue in range(1, numberOfSets+1):
                totalFitness = self.fitness_calc(setValue, paths)
                averageProbability = self.probability_calc(setValue, totalFitness, paths)
                no_of_new_test_cases = self.no_of_new_test_cases(setValue, averageProbability, paths)
                self.new_test_data_generation(testSuite, no_of_new_test_cases, program)
                self.neighbour_test_data_generation(testSuite, program, paths)
            self.evaluate_test_cases(testSuite, paths, program)
            self.iteration+=1

        return testSuite

    def initialise_test_cases(self, testSuite, paths, program):
        for i in range(paths.getSize()):
            testCase = TestCase()
            for j in range(program.numberOfInputVariables):
                testValue = 1 + random.randint(0, program.range)
                testCase.addValue(testValue)

            if not testSuite.isTestCasePresent(testCase):
                testSuite.addTestCase(testCase)

    def evaluate_test_cases(self, testSuite, paths, program):
        for testCase in testSuite.getTestCases():
            variables = testCase.getVariableSet()
            pathNumber = program.program(paths, variables)
            testCase.satisfyingPath = pathNumber + 1
            if pathNumber != -1:
                paths.setPathVisited(pathNumber)

    def divide_into_sets(self, paths, program):
        root = program.cfgRoot

        while root.falseConditionNode == None:
            root = root.trueConditionNode

        # for set 1
        for path in paths.getPaths():
            if path.isNodePresent(root.trueConditionNode):
                path.setSetValue(1)

        # for set 2
        for path in paths.getPaths():
            if path.isNodePresent(root.falseConditionNode):
                path.setSetValue(2)


    def check_path_satisfaction(self, paths):
        for path in paths.getPaths():
            if not path.isVisited():
                return False
        return True


    def fitness_calc(self, setNo, paths):
        totalFitness = 0
        maxFitness = 0
        for firstPath in paths.getPaths():
            tempFitness = None
            if firstPath.isVisited() and firstPath.getSetValue() == setNo:
                for secondPath in paths.getPaths():
                    if not secondPath.isVisited() and secondPath.getSetValue() == setNo:
                        tempFitness = paths.fitnessOfPath(firstPath, secondPath)
                        secondPath.setTempFitness(tempFitness)
                        if maxFitness < tempFitness:
                            maxFitness = tempFitness 
                        else:
                            maxFitness = maxFitness

        for firstPath in paths.getPaths():
            if firstPath.isVisited() and firstPath.getSetValue() == setNo:
                for secondPath in paths.getPaths():
                    if not secondPath.isVisited() and secondPath.getSetValue() == setNo:
                        secondPath.setFitnessValue((secondPath.getTempFitness()) / maxFitness)
        for path in paths.getPaths():
            totalFitness += path.getFitnessValue()

        return totalFitness


    def probability_calc(self, setValue, totalFitness, paths):
        count = 1
        totalProbability = 0
        for path in paths.getPaths():
            if not path.isVisited() and path.getSetValue() == setValue and totalFitness > 0:
                probability = (path.getFitnessValue()) / totalFitness
                path.setProbability(probability)
                totalProbability += probability
                count+=1
        return totalProbability / count


    def no_of_new_test_cases(self, setValue, averageProbability, paths):
        newTestCases = 0
        for path in paths.getPaths():
            if not path.isVisited() and path.getSetValue() == setValue and path.getProbability() <= averageProbability:
                newTestCases += 1
        return newTestCases

    def new_test_data_generation(self, testSuite, newTestCases, program):
        for i in range(newTestCases):
            testCase = TestCase()

            for j in range(program.numberOfInputVariables):
                testValue = 1 + random.randint(0, program.range)
                testCase.addValue(testValue)

            if not testSuite.isTestCasePresent(testCase):
                testSuite.addTestCase(testCase)


    def neighbour_test_data_generation(self, testSuite, program, paths):
        numberOfUnsolvedPaths = self.get_no_of_unsolved_paths(paths)
    
        for i in range(numberOfUnsolvedPaths):
            testCase = TestCase()
            for j in range(program.numberOfInputVariables):
                number = random.randint(0, 1) - 1
                index = random.randint(0, testSuite.getSize()-1)
                testCase.addValue(testSuite.getTestCase(i).getVariable(j) +
                        number * (testSuite.getTestCase(i).getVariable(j) -
                                testSuite.getTestCase(index).getVariable(j)))

            if not testSuite.isTestCasePresent(testCase):
                testSuite.addTestCase(testCase)

    def get_no_of_unsolved_paths(self, paths):
        numberOfUnsolvedPaths = 0
        for path in paths.getPaths():
            if not path.isVisited():
                numberOfUnsolvedPaths += 1
        return numberOfUnsolvedPaths


    def get_path_coverage(self, paths):
        coveredPathCount = 0

        for path in paths.getPaths():
            if (path.isVisited()):
                coveredPathCount += 1

        return coveredPathCount

    def get_iterations(self):
        return self.iteration

