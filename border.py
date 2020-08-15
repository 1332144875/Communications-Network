import numpy
class Border:
    def __init__(self,node1,node2):
        self.node1=node1
        self.node2=node2
        self.distance=node1.distance(node2)
        self.cost=node1.cost(node2)
        self.weight=numpy.multiply(self.distance,self.cost)

