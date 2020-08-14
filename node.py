from border import Border
class Node:
    #index:int,borders:list
    #index is the index of the node,borders show that the borders link to the node
    def __init__(self,index):
        self.index=index
        self.borders=dict()
    def addBorder(self,indexOfanother,border):
        self.borders[indexOfanother]=border

