class Border:
    def __init__(self,distance,cost,node1,node2):
        self.distance=distance
        self.cost=cost
        self.node1=node1
        self.node2=node2
        self.weight=distance*cost

