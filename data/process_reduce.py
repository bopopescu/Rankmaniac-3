#!/usr/bin/env python

import heapq
import json
import sys

heapId = -1
iterId = -2

def parseInput(line):
    key, value = line.split("\t", 1)
    key = int(key)
    value = json.loads(value)
    return key, value

def printNode(nodeId, value):
    currRank = value["currRank"]
    prevRank = value["prevRank"]
    outLinks = value["outLinks"]
    outlinkString = reduce(lambda x, y: x + y, map(lambda link: "," + str(link), outLinks), "")
    sys.stdout.write("NodeId:" + str(nodeId) + "\t" + str(currRank) + "," + str(prevRank) + outlinkString + "\n")

def processNode(nodeId, values):
    if len(values) == 1 and nodeId >= 0:
        printNode(nodeId, values[0])
    elif nodeId == heapId:
        heap = values[0]["heap"]
        for (rank, node) in heapq.nlargest(20, heap):
            sys.stdout.write("FinalRank:" + str(rank) + "\t" + str(node) + "\n")
    elif nodeId == iterId:
        printNode(nodeId, values[0])



lastKey = None
values = []

for line in sys.stdin:
    node, value = parseInput(line)
    if lastKey is None:
        lastKey = node
    if node != lastKey:
        processNode(lastKey, values)
        lastKey = node
        values = []
    values.append(value)
processNode(lastKey, values)


#
# heaps = []
# done = False
#
# for line in sys.stdin:
#     if line.startswith("R"):
#         done = True
#         heaps.append(json.loads(line.split("\t")[1]))
#     else:
#         sys.stdout.write(line)
#
# if done:
#     heap = heapq.merge(*heaps)
#     for (rank, node) in heapq.nlargest(20, heap):
#         sys.stdout.write("FinalRank:" + str(rank) + "\t" + str(node) + "\n")
