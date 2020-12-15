from model.graph import Graph
from model.chromosome import Chromosome
from model.paths import Paths
from model.path import Path
from math import sqrt

import logging
import logging.handlers
import os
 
handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", "logs/remainder.log"))
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)

class RemainderProgram:
    def __init__(self):
        self.complexity = 2
        self.numberOfInputVariables = 2
        self.range = 20
        self.cfg = self.create_cfg()
        self.cfgRoot = self.cfg.getNode(1)
        self.cfg_end_node = self.cfg .getNode(6)

        self.decisionTree = self.createDecisionTree()
        self.decisionTreeRoot = self.decisionTree.getNode(1)
        self.decisionTreePaths = self.decisionTreePathGeneration()
        self.leaves = self.getLeaves()

    def create_cfg(self):
        cfg = Graph()

        for lineNumber in range(1, 7):
            cfg.newNode(lineNumber)

        cfg.getNode(1).add_true_cond_node(cfg.getNode(2));
        cfg.getNode(2).add_true_cond_node(cfg.getNode(3));
        cfg.getNode(2).add_false_cond_node(cfg.getNode(4));
        cfg.getNode(3).add_true_cond_node(cfg.getNode(6));
        cfg.getNode(4).add_true_cond_node(cfg.getNode(5));
        cfg.getNode(5).add_true_cond_node(cfg.getNode(6));
        return cfg

    def program(self, paths, variables):
        A, B = variables[0], variables[1]
        if (B != 0):
            r = A % B;
            if (r == 0):
                logging.info("Remainder of {} and {} is {}".format(A, B, 0))
                return (paths.getPathNumberHavingNode(3));
            else:
                logging.info("Remainder of {} and {} is {}".format(A, B, r))
                return (paths.getPathNumberHavingNode(4));
        return 0

    def getLeafByEvaluation(self, chromosome):
        a = chromosome.realData[0].intValue();
        b = chromosome.realData[1].intValue();
        r = a % b;
        if (r == 0):
            return 3
        else:
            return 5


    def createDecisionTree(self):
        dtree = Graph()

        for i in range(1, 7):
            dtree.newNode(i)

        dtree.getNode(1).add_true_cond_node(dtree.getNode(2));
        dtree.getNode(2).add_true_cond_node(dtree.getNode(3));
        dtree.getNode(2).add_neutral_cond_node(dtree.getNode(6));
        dtree.getNode(2).add_false_cond_node(dtree.getNode(4));
        dtree.getNode(4).add_true_cond_node(dtree.getNode(5));
        return dtree;


    def decisionTreePathGeneration(self):
        decisionTreePaths = Paths()

        newPath = Path()
        newPath.addNode(self.decisionTree.getNode(1))
        newPath.addNode(self.decisionTree.getNode(2))
        newPath.addNode(self.decisionTree.getNode(3))
        decisionTreePaths.addPath(newPath)


        newPath = Path();
        newPath.addNode(self.decisionTree.getNode(1));
        newPath.addNode(self.decisionTree.getNode(2));
        newPath.addNode(self.decisionTree.getNode(6));
        decisionTreePaths.addPath(newPath);

        newPath = Path();
        newPath.addNode(self.decisionTree.getNode(1));
        newPath.addNode(self.decisionTree.getNode(2));
        newPath.addNode(self.decisionTree.getNode(4));
        newPath.addNode(self.decisionTree.getNode(5));
        decisionTreePaths.addPath(newPath);

        return decisionTreePaths;

    def getLeaves(self):
        leaves = list()
        leaves.append(self.decisionTree.getNode(3))
        leaves.append(self.decisionTree.getNode(5))
        leaves.append(self.decisionTree.getNode(6))
        return leaves

