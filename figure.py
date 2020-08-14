import xlrd
from node import Node
from border import Border
class Figure:
    def __init__(self):
        self.nodes=list()
        self.borders=list()
        xls = xlrd.open_workbook('节点距离与铺设费用.xls')
        distance_table=xls.sheet_by_index(0)
        cost_table=xls.sheet_by_index(1)
        
        for i in range(0,80):
            self.nodes.append(Node(i))
        
        for x in range(0,80):
            for y in range(x+1,80):
               border=Border(distance_table.cell(x+1,y).value*100,cost_table.cell(x+1,y).value,self.nodes[x],self.nodes[y])
               self.borders.append(border)
               self.nodes[x].addBorder(y,border)
               self.nodes[y].addBorder(x,border)
        


