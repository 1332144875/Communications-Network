#! /usr/bin/env python3
import numpy
from figure import Figure

def main():
    figure=Figure(80)
    V=[figure.nodes[0]]
    E=[]
    while len(V)<80:
        nodePair=None
        for node1 in V:
            for node2 in figure.nodes.values():
                if node1 != node2:
                    if nodePair == None or node1.weight(node2) < nodePair[0].weight(nodePair[1]):
                        if node1 not in V or node2 not in V:
                            nodePair=(node1,node2)
        if nodePair!=None:
            E.append(figure.connect(nodePair[0],nodePair[1]))
            if nodePair[0] not in V:
                V.append(nodePair[0])
            if nodePair[1] not in V:
                V.append(nodePair[1])


                    
if __name__=="__main__":
    main()

