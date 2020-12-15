from model.graph import Graph
from model.chromosome import Chromosome
from model.paths import Paths
from model.path import Path
import logging
import logging.handlers
import os
 
handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", "logs/even_odd.log"))
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)


class EvenOddProgram:
    def __init__(self):
        self.complexity = 3
        self.numberOfInputVariables = 1
        self.range = 20
        self.cfg = self.createcfg()
        self.cfgRoot = self.cfg.getNode(1)
        self.cfgEndNode = self.cfg.getNode(8)

        self.dtree = self.createdtree()
        self.dtreeRoot = self.dtree.getNode(1)
        self.dtreePaths = self.dtreePathGeneration()
        self.leaves = self.getLeaves()


    def createcfg(self):
        cfg = Graph()
        for lineNumber in range(1, 9):
            cfg.newNode(lineNumber)

        cfg.getNode(1).add_true_cond_node(cfg.getNode(2))
        cfg.getNode(2).add_true_cond_node(cfg.getNode(3))
        cfg.getNode(2).add_false_cond_node(cfg.getNode(4))
        cfg.getNode(3).add_true_cond_node(cfg.getNode(8))
        cfg.getNode(4).add_true_cond_node(cfg.getNode(5))
        cfg.getNode(4).add_false_cond_node(cfg.getNode(6))
        cfg.getNode(5).add_true_cond_node(cfg.getNode(8))
        cfg.getNode(6).add_true_cond_node(cfg.getNode(7))
        cfg.getNode(7).add_true_cond_node(cfg.getNode(8))

        return cfg


    def program(self, paths, variables):
        a = variables[0]
        if a % 2 == 0:
            logging.info("{} is even".format(a))
            return (paths.getPathNumberHavingNode(3))
        elif(a == 1):
            logging.info("Number is 1")
            return (paths.getPathNumberHavingNode(5))
        else:
            logging.info("{} is odd".format(a))
            return (paths.getPathNumberHavingNode(7))


    def getLeafByEvaluation(self, chromosome):
        a = chromosome.realData[0].intValue()
        if a % 2 == 0:
            return 3
        elif a == 1:
            return 5
        else:
            return 7


    def createdtree(self):
        dtree = Graph()
        for i in range(1, 9):
            dtree.newNode(i)

        dtree.getNode(1).add_true_cond_node(dtree.getNode(2))
        dtree.getNode(2).add_true_cond_node(dtree.getNode(3))
        dtree.getNode(2).add_neutral_cond_node(dtree.getNode(8))
        dtree.getNode(2).add_false_cond_node(dtree.getNode(4))
        dtree.getNode(4).add_true_cond_node(dtree.getNode(5))
        dtree.getNode(4).add_false_cond_node(dtree.getNode(6))
        dtree.getNode(6).add_true_cond_node(dtree.getNode(7))
        print(dtree.edges, dtree.nodes)

        return dtree


    def dtreePathGeneration(self):
        dtreePaths = Paths()

        newPath = Path()
        newPath.addNode(self.dtree.getNode(1))
        newPath.addNode(self.dtree.getNode(2))
        newPath.addNode(self.dtree.getNode(3))
        dtreePaths.addPath(newPath)

        newPath = Path()
        newPath.addNode(self.dtree.getNode(1))
        newPath.addNode(self.dtree.getNode(2))
        newPath.addNode(self.dtree.getNode(8))
        dtreePaths.addPath(newPath)

        newPath = Path()
        newPath.addNode(self.dtree.getNode(1))
        newPath.addNode(self.dtree.getNode(2))
        newPath.addNode(self.dtree.getNode(4))
        newPath.addNode(self.dtree.getNode(5))
        dtreePaths.addPath(newPath)

        newPath = Path()
        newPath.addNode(self.dtree.getNode(1))
        newPath.addNode(self.dtree.getNode(2))
        newPath.addNode(self.dtree.getNode(3))
        newPath.addNode(self.dtree.getNode(4))
        newPath.addNode(self.dtree.getNode(6))
        newPath.addNode(self.dtree.getNode(7))
        dtreePaths.addPath(newPath)

        return dtreePaths


    def getLeaves(self):
        leaves = list()
        leaves.append(self.dtree.getNode(3))
        leaves.append(self.dtree.getNode(5))
        leaves.append(self.dtree.getNode(7))
        leaves.append(self.dtree.getNode(8))
        return leaves

