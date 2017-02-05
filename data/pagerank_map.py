#!/usr/bin/env python

import sys
import json

maxNodeID = 0

for line in sys.stdin:
    cmps = line.split("\t")
    arr = cmps[1].split(",")
    nodeID = int(cmps[0].split(":")[1])
    currRank = float(arr[0])
    prevRank = float(arr[1])
    outLinks = map(int, arr[2:])

    maxNodeID = max(maxNodeID, nodeID)

    linkValue = json.dumps({
        "data": "inLink",
        "rank": currRank,
        "numOut": len(outLinks)
    })

    metaValue = json.dumps({
        "data": "meta",
        "outLinks": outLinks,
        "currRank": currRank
    })

    for child in outLinks:
        sys.stdout.write(str(child) + "\t" + linkValue + "\n")

    sys.stdout.write(str(nodeID) + "\t" + metaValue + "\n")

maxNodeValue = json.dumps({
    "data": "maxNodeID",
    "maxNodeID": maxNodeID
})

for i in range(maxNodeID + 1):
    sys.stdout.write(str(i) + "\t" + maxNodeValue + "\n")
