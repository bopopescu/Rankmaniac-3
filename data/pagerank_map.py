#!/usr/bin/env python

import sys
import json

iterId = "-2"
epsilonId = "-3"

def printOutput(messageKey, data):
    sys.stdout.write(messageKey + "\t" + json.dumps(data) + "\n")

for line in sys.stdin:
    cmps = line.split("\t")
    nodeId = cmps[0].split(":")[1]
    arr = cmps[1].split("\n")[0].split(",")

    if nodeId == iterId:
        iteration = int(arr[0])
        printOutput(nodeId, {"iteration": iteration})
    elif nodeId == epsilonId:
        epsilon = float(arr[0])
        printOutput(nodeId, {"epsilon": epsilon})
    else:
        currRank = float(arr[0])
        outLinks = arr[2:]
        if len(outLinks) == 0:
            printOutput(nodeId, {"dataType": "inLink", "parentRank": currRank, "parentOutCount": 1})
        else:
            for child in outLinks:
                printOutput(child, {"dataType": "inLink", "parentRank": currRank, "parentOutCount": len(outLinks)})

        printOutput(nodeId, {"dataType": "meta", "outLinks": outLinks, "currRank": currRank})
