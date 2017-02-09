#!/usr/bin/env python

import sys
import json

def printOutput(messageKey, data):
    sys.stdout.write(str(messageKey) + "\t" + json.dumps(data) + "\n")

for line in sys.stdin:
    cmps = line.split("\t")
    arr = cmps[1].split(",")
    nodeID = int(cmps[0].split(":")[1])
    currRank = float(arr[0])
    prevRank = float(arr[1])
    outLinks = map(int, arr[2:])

    for child in outLinks:
        printOutput(child, {"dataType": "inLink", "parentRank": currRank, "parentOutCount": len(outLinks)})
    if len(outLinks) == 0:
        printOutput(nodeID, {"dataType": "inLink", "parentRank": currRank, "parentOutCount": 1})

    printOutput(nodeID, {"dataType": "meta", "outLinks": outLinks, "currRank": currRank})
