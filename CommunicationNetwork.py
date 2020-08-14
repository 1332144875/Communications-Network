#! /usr/bin/env python3
import numpy
from figure import Figure

def main():
    figure=Figure()
    V=[figure.nodes[0]]
    E=[]
    while len(V)<80:
        borderWeightMin=None
        for node in V:
            for border in node.borders.values():
                if border.node1 not in V or border.node2 not in V:
                    if borderWeightMin==None or border.weight < borderWeightMin.weight:
                        borderWeightMin=border

        if borderWeightMin!=None:
            E.append(borderWeightMin)
            if borderWeightMin.node1 not in V:
                V.append(borderWeightMin.node1)
            if borderWeightMin.node2 not in V:
                V.append(borderWeightMin.node2)

    cost=0

    for border in E:
        cost+=border.weight
        print(str(border.node1.index+1)+"-"+str(border.node2.index+1))
    print(str(cost))
                    
if __name__=="__main__":
    main()

