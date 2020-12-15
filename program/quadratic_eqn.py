from model.graph import Graph
from model.chromosome import Chromosome
from model.paths import Paths
from model.path import Path
from math import sqrt
import logging
import logging.handlers
import os
 
handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", "logs/quadratic.log"))
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)


class QuadraticEquationProgram:

    def __init__(self):
        self.complexity = 4
        self.numberOfInputVariables = 3
        self.range = 30
        self.cfg = self.create_cfg()
        self.cfgRoot = self.cfg.getNode(1)
        self.cfg_end_node = self.cfg .getNode(15)

        self.decisionTree = self.createDecisionTree()
        self.decisionTreeRoot = self.decisionTree.getNode(1)
        self.decisionTreePaths = self.decisionTreePathGeneration()
        self.leaves = self.getLeaves()

    def create_cfg(self):
        cfg = Graph()

        for lineNumber in range(1, 16):
            cfg.newNode(lineNumber)

        cfg.getNode(1).add_true_cond_node(cfg.getNode(2))
        cfg.getNode(2).add_true_cond_node(cfg.getNode(3))
        cfg.getNode(2).add_false_cond_node(cfg.getNode(4))
        cfg.getNode(3).add_true_cond_node(cfg.getNode(15))
        cfg.getNode(4).add_true_cond_node(cfg.getNode(5))
        cfg.getNode(5).add_true_cond_node(cfg.getNode(6))
        cfg.getNode(6).add_true_cond_node(cfg.getNode(7))
        cfg.getNode(6).add_false_cond_node(cfg.getNode(8))
        cfg.getNode(7).add_true_cond_node(cfg.getNode(14))
        cfg.getNode(8).add_true_cond_node(cfg.getNode(9))
        cfg.getNode(9).add_true_cond_node(cfg.getNode(10))
        cfg.getNode(9).add_false_cond_node(cfg.getNode(11))
        cfg.getNode(10).add_true_cond_node(cfg.getNode(13))
        cfg.getNode(11).add_true_cond_node(cfg.getNode(12))
        cfg.getNode(12).add_true_cond_node(cfg.getNode(13))
        cfg.getNode(13).add_true_cond_node(cfg.getNode(14))
        cfg.getNode(14).add_true_cond_node(cfg.getNode(15))

        return cfg

    def program(self, paths, variables):
        A, B, C = variables[0], variables[1], variables[2] 
        discrimator = B**2 - 4*A*C
        denominator = 2*A
        if (A == 0):
            return (paths.getPathNumberHavingNode(3))
        else:
            if (discrimator == 0):
                logging.info("THE ROOTS ARE REPEATED ROOTS")
                root1 = ((-1)*B)/denominator
                logging.info("roots of given equation are: {} {}".format(root1, root1))
                return (paths.getPathNumberHavingNode(7))
            else:
                if (discrimator > 0):
                    logging.info("THE ROOTS ARE REAL ROOTS")
                    root1 = ((-1)*B)/denominator + sqrt(discrimator)/denominator
                    root2 = ((-1)*B)/denominator - sqrt(discrimator)/denominator
                    logging.info("roots of given equation are: {} {}".format(root1, root2))
                    return (paths.getPathNumberHavingNode(10))
                else:
                    logging.info("THE ROOTS ARE IMAGINARY ROOTS")
                    return (paths.getPathNumberHavingNode(12))

    def getLeafByEvaluation(self, chromosome):
        a = chromosome.realData.get(0).intValue()
        b = chromosome.realData.get(1).intValue()
        c = chromosome.realData.get(2).intValue()
        d = 0
        d = (b * b) - (4 * a * c)
        if (a == 0):
            return 3
        else:
            if (d == 0):
                return 7
            else:
                if (d > 0):
                    return 10
                else:
                    return 12

    def createDecisionTree(self):
        dtree = Graph()

        for i in range(1, 16):
            dtree.newNode(i)

        dtree.getNode(1).add_true_cond_node(dtree.getNode(2))
        dtree.getNode(2).add_true_cond_node(dtree.getNode(3))
        dtree.getNode(2).add_neutral_cond_node(dtree.getNode(15))
        dtree.getNode(2).add_false_cond_node(dtree.getNode(4))
        dtree.getNode(4).add_true_cond_node(dtree.getNode(5))
        dtree.getNode(5).add_true_cond_node(dtree.getNode(6))
        dtree.getNode(6).add_true_cond_node(dtree.getNode(7))
        dtree.getNode(6).add_neutral_cond_node(dtree.getNode(14))
        dtree.getNode(6).add_false_cond_node(dtree.getNode(8))
        dtree.getNode(8).add_true_cond_node(dtree.getNode(9))
        dtree.getNode(9).add_true_cond_node(dtree.getNode(10))
        dtree.getNode(9).add_neutral_cond_node(dtree.getNode(13))
        dtree.getNode(9).add_false_cond_node(dtree.getNode(11))
        dtree.getNode(11).add_true_cond_node(dtree.getNode(12))

        return dtree

    def decisionTreePathGeneration(self):
        decisionTreePaths = Paths()

        newPath = Path()
        newPath.addNode(self.decisionTree.getNode(1))
        newPath.addNode(self.decisionTree.getNode(2))
        newPath.addNode(self.decisionTree.getNode(3))
        decisionTreePaths.addPath(newPath)

        newPath = Path()
        newPath.addNode(self.decisionTree.getNode(1))
        newPath.addNode(self.decisionTree.getNode(2))
        newPath.addNode(self.decisionTree.getNode(15))
        decisionTreePaths.addPath(newPath)

        newPath = Path()
        newPath.addNode(self.decisionTree.getNode(1))
        newPath.addNode(self.decisionTree.getNode(2))
        newPath.addNode(self.decisionTree.getNode(3))
        newPath.addNode(self.decisionTree.getNode(4))
        newPath.addNode(self.decisionTree.getNode(5))
        newPath.addNode(self.decisionTree.getNode(6))
        newPath.addNode(self.decisionTree.getNode(7))
        decisionTreePaths.addPath(newPath)

        newPath = Path()
        newPath.addNode(self.decisionTree.getNode(1))
        newPath.addNode(self.decisionTree.getNode(2))
        newPath.addNode(self.decisionTree.getNode(3))
        newPath.addNode(self.decisionTree.getNode(4))
        newPath.addNode(self.decisionTree.getNode(5))
        newPath.addNode(self.decisionTree.getNode(6))
        newPath.addNode(self.decisionTree.getNode(14))
        decisionTreePaths.addPath(newPath)

        newPath = Path()
        newPath.addNode(self.decisionTree.getNode(1))
        newPath.addNode(self.decisionTree.getNode(2))
        newPath.addNode(self.decisionTree.getNode(3))
        newPath.addNode(self.decisionTree.getNode(4))
        newPath.addNode(self.decisionTree.getNode(5))
        newPath.addNode(self.decisionTree.getNode(6))
        newPath.addNode(self.decisionTree.getNode(8))
        newPath.addNode(self.decisionTree.getNode(9))
        newPath.addNode(self.decisionTree.getNode(10))
        decisionTreePaths.addPath(newPath)

        newPath = Path()
        newPath.addNode(self.decisionTree.getNode(1))
        newPath.addNode(self.decisionTree.getNode(2))
        newPath.addNode(self.decisionTree.getNode(3))
        newPath.addNode(self.decisionTree.getNode(4))
        newPath.addNode(self.decisionTree.getNode(5))
        newPath.addNode(self.decisionTree.getNode(6))
        newPath.addNode(self.decisionTree.getNode(8))
        newPath.addNode(self.decisionTree.getNode(9))
        newPath.addNode(self.decisionTree.getNode(13))
        decisionTreePaths.addPath(newPath)

        newPath = Path()
        newPath.addNode(self.decisionTree.getNode(1))
        newPath.addNode(self.decisionTree.getNode(2))
        newPath.addNode(self.decisionTree.getNode(3))
        newPath.addNode(self.decisionTree.getNode(4))
        newPath.addNode(self.decisionTree.getNode(5))
        newPath.addNode(self.decisionTree.getNode(6))
        newPath.addNode(self.decisionTree.getNode(8))
        newPath.addNode(self.decisionTree.getNode(9))
        newPath.addNode(self.decisionTree.getNode(11))
        newPath.addNode(self.decisionTree.getNode(12))
        decisionTreePaths.addPath(newPath)

        return decisionTreePaths


    def getLeaves(self):
        leaves = list()
        leaves.append(self.decisionTree.getNode(3))
        leaves.append(self.decisionTree.getNode(7))
        leaves.append(self.decisionTree.getNode(10))
        leaves.append(self.decisionTree.getNode(12))
        leaves.append(self.decisionTree.getNode(13))
        leaves.append(self.decisionTree.getNode(14))
        leaves.append(self.decisionTree.getNode(15))
        return leaves
