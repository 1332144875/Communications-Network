from border import Border
import xlrd
class Node:
    #index:int,borders:list
    #index is the index of the node,borders show that the borders link to the node
    def __init__(self,index):
        self.index=index
        self.borders=dict()
    #border:Border
    def addBorder(self,border):
        if border.node1 == self and border.node2 != self:
            self.borders[node2]=border
        elif border.node2 == self and border.node1 != self:
            self.borders[node1]=border
    #node:Node
    def distance(self,node):
        xls=xlrd.open_workbook("节点距离与铺设费用.xls")
        distance_table=xls.sheet_by_id(0)
        return distance_table.cell(self.index+1,node.index).value*100

    def cost(self,node):
        xls = xlrd.open_workbook("节点距离与铺设费用.xls")
        distance_table = xls.sheet_by_id(1)
        return distance_table.cell(self.index + 1, node.index).value

    def weight(self,node):
        return self.distance(node)*self.cost(node)
