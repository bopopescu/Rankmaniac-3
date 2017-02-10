#!/usr/bin/env python

import heapq
import json
import sys

heapId = "-1"
iterId = "-2"

def parseInput(line):
    key, value = line.split("\t", 1)
    value = json.loads(value)
    return key, value

def printNode(nodeId, value):
    currRank = value["currRank"]
    prevRank = value["prevRank"]
    outLinks = value["outLinks"]
    outlinkString = ""
    if len(outLinks) > 0:
        outlinkString = "," + ",".join(outLinks)
    sys.stdout.write("NodeId:" + nodeId + "\t" + str(currRank) + "," + str(prevRank) + outlinkString + "\n")

def processNode(nodeId, values):
    if len(values) == 1 and nodeId != heapId and nodeId != iterId:
        printNode(nodeId, values[0])
    elif nodeId == heapId:
        heap = values[0]["heap"]
        for (rank, node) in heapq.nlargest(20, heap):
            sys.stdout.write("FinalRank:" + str(rank) + "\t" + node + "\n")
    elif nodeId == iterId:
        printNode(nodeId, values[0])

lastKey = None
values = []

for line in sys.stdin:
    nodeId, value = parseInput(line)
    if lastKey is None:
        lastKey = nodeId
    if nodeId != lastKey:
        processNode(lastKey, values)
        lastKey = nodeId
        values = []
    values.append(value)
processNode(lastKey, values)
