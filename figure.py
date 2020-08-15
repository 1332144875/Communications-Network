import xlrd
from node import Node
from border import Border

import numpy

class Figure:
    def __init__(self,nNodes):
        self.xls = xlrd.open_workbook("节点距离与铺设费用.xls")
        self.nodes=dict()
        self.borders=list()
        
        for i in range(0,nNodes):
            self.nodes[i]=Node(self,i)
    def connect(self,node1,node2):
        #if node1 and node2 is the same,return None
        if node1 == node2:
            return None
        #if node1 connects node2,return None
        if node1 in node2.borders.keys() or node2 in node1.borders.keys():
            return None
        #if node1 or node2 is nont in self.nodes,return None
        if node1 not in self.nodes.values() or node2 not in self.nodes.values():
            return None
        border=Border(node1,node2)#create new border
        #add the new border to nodes
        node1.addBorder(border)
        node2.addBorder(border)
        #add the new border to the list of figure
        self.borders.append(border)
        return border
    def disconnect(self,node1,node2):
        border = None
        if node1 in node2.borders.keys():
            border = node2.borders[node1]
            del node2.borders[node1]
        if node2 in node1.borders.keys():
            border=node1.borders[node2]
            del node1.borders[node2]
        if border != None:
            for i in range(0,len(self.borders)):
                if self.borders[i] == border:
                    del self.borders[i]
                    break
        return border

    def addNode(self,node):
        if node.index not in self.nodes:
            self.nodes[node.index]=node

    def delNode(self,node):
        if node in self.nodes.copy().values():
            for node1 in node.borders.copy().keys():
                self.disconnect(node,node1)
            del self.nodes[node.index]
    #the average distance
    def average_distance(self):
        total_distance=[]
        for node1 in self.nodes.values():
            for node2 in self.nodes.values():
                if node1 != node2:
                    total_distance.append(node1.distance(node2))
        if len(total_distance)==0:
            return 0
        return numpy.mean(total_distance)

    def nNodes(self):
        return len(self.nodes)

    def nBorders(self):
        return len(self.borders)

    def deepcopy(self):
        new_figure=Figure(0)
        for node in self.nodes.values():
            new_node=Node(new_figure,node.index)
            new_figure.addNode(new_node)
        for border in self.borders:
            new_figure.connect(new_figure.nodes[border.node1.index],new_figure.nodes[border.node2.index])
        return new_figure


