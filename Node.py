class Node:
    #distance:list,cost:list
    def __init__(self,distance,cost):
        self.distance=distance[:]
        self.cost=cost[:]
    #index:int
    def getWeight(index):
        return self.cost[index]*self.distance[index]
