#!/usr/bin/env python

import heapq
import json
import sys

heapId = "-1"
iterId = "-2"
epsilonId = "-3"

def parseInput(line):
    key, value = line.split("\t", 1)
    value = json.loads(value)
    return key, value

def printNode(nodeId, value):
    if "currRank" in value:
        currRank = value["currRank"]
    else:
        print(nodeId, value)
    prevRank = value["prevRank"]
    outLinks = value["outLinks"]
    outlinkString = ""
    if len(outLinks) > 0:
        outlinkString = "," + ",".join(outLinks)
    sys.stdout.write("NodeId:" + nodeId + "\t" + str(currRank) + "," + str(prevRank) + outlinkString + "\n")

def printIter(iterator):
    sys.stdout.write("NodeId:" + iterId + "\t" + str(iterator) + "\n")

def printEpsilon(epsilon, num_converges):
    sys.stdout.write("NodeId:" + epsilonId + "\t" + str(epsilon) + "," + str(num_converges) + "\n")

def printTop20(heap):
    for (rank, node) in heapq.nlargest(20, heap):
        sys.stdout.write("FinalRank:" + str(rank) + "\t" + node + "\n")

def processNode(nodeId, values):
    if len(values) == 1 and "converged" not in values[0]:
        printNode(nodeId, values[0])

lastKey = None
values = []

for line in sys.stdin:
    nodeId, value = parseInput(line)
    if nodeId == iterId:
        printIter(value["iteration"])
    elif nodeId == epsilonId:
        printEpsilon(value["epsilon"], value["num_converges"])
    elif nodeId == heapId:
        printTop20(value["heap"])
    else:
        if lastKey is None:
            lastKey = nodeId
        if nodeId != lastKey:
            processNode(lastKey, values)
            lastKey = nodeId
            values = []
        values.append(value)
if lastKey is not None and lastKey != iterId and lastKey != epsilonId and lastKey != heapId:
    processNode(lastKey, values)
