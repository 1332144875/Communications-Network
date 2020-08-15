from border import Border

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
        return distance_table.cell(self.index+1,node.index).value*100

    def cost(self,node):
        distance_table = self.figure.xls.sheet_by_index(1)
        return distance_table.cell(self.index + 1, node.index).value

    def weight(self,node):
        return self.distance(node)*self.cost(node)
