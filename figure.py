import xlrd
from node import Node
from border import Border
class Figure:
    def __init__(self):
        self.nodes=list()
        self.borders=list()
        
        for i in range(0,80):
            self.nodes.append(Node(i))
    def connect(self,node1,node2):
        if node1 in node2.borders.keys() or node2 in node1.borders.keys():
            return None
        if node1 not in self.nodes or node2 not in self.nodes:
            return None
        border=Border(node1,node2)
        node1.addBorder(border)
        node2.addBorder(border)
        self.borders.append(border)
        return border
    def disconnect(self,node1,node2):
        border = None
        if node1 in node2.borders.keys():
            border = node2[node1]
            del node2[node1]
        if node2 in node1.borders.keys():
            border=node1[node2]
            del node1[node2]
        if border != None:
            for i in range(0,len(self.borders)):
                if self.borders[i] == border:
                    del self.borders[i]
        return border
        


