#!/usr/bin/env python

import sys
import json

maxNodeID = 0

def putMessage(messageKey, dataType, data):
    data["data"] = dataType
    sys.stdout.write(str(messageKey) + "\t" + json.dumps(data) + "\n")

for line in sys.stdin:
    if line.startswith("FinalRank"):
        raise Exception("DONE")
    cmps = line.split("\t")
    arr = cmps[1].split(",")
    nodeID = int(cmps[0].split(":")[1])
    currRank = float(arr[0])
    prevRank = float(arr[1])
    outLinks = map(int, arr[2:])

    maxNodeID = max(maxNodeID, nodeID)


    for child in outLinks:
        putMessage(child, "inLink", {"rank": currRank, "numOut": len(outLinks)})
    if len(outLinks) == 0:
        putMessage(nodeID, "inLink", {"rank": currRank, "numOut": 1})

    putMessage(nodeID, "meta", {"outLinks": outLinks, "currRank": currRank})
