from border import Border
import numpy

class Node:
    #index:int,borders:list
    #index is the index of the node,borders show that the borders link to the node
    def __init__(self,figure,index):
        self.figure=figure
        self.index=index
        self.borders=dict()
    #border:Border
    def addBorder(self,border):
        if border.node1 == self and border.node2 != self:
            self.borders[border.node2]=border
        elif border.node2 == self and border.node1 != self:
            self.borders[border.node1]=border
    #node:Node
    def distance(self,node):
        distance_table=self.figure.xls.sheet_by_index(0)
        return numpy.multiply(distance_table.cell(self.index+1,node.index).value,100)

    def cost(self,node):
        distance_table = self.figure.xls.sheet_by_index(1)
        return distance_table.cell(self.index + 1, node.index).value

    def weight(self,node):
        return self.distance(node)*self.cost(node)

    def shrink(self):
        #Traverse the nodes connected to self
        for node1 in self.borders.copy().keys():
            #Traverse the nodes connected to node1
            for node2 in node1.borders.copy().keys():
                #connect self and node2
                self.figure.connect(self,node2)
            # delete the node
            self.figure.delNode(node1)

    def imc(self):
        #copy the figure
        shrinkFigure = self.figure.deepcopy()
        #shrink the node
        shrinkFigure.nodes[self.index].shrink()
        imc1 = numpy.multiply(self.figure.nNodes(),self.figure.average_distance())
        imc2 = numpy.multiply(shrinkFigure.nNodes(),shrinkFigure.average_distance())
        imc = numpy.subtract(imc1,imc2)
        imc=numpy.divide(imc,imc1)
        return imc
    def __lt__(self,other):
        return self.imc()<other.imc()
