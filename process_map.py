#!/usr/bin/env python

import heapq
import json
import sys
import math

convergenceDiff = 0.05

sumDiff = 0

iteration = 1

max_iter = 50

N = 0
heap = []
converged = False

heapId = "-1"
iterId = "-2"

def printOutput(messageKey, data):
    sys.stdout.write(messageKey + "\t" + json.dumps(data) + "\n")

def parseInput(line):
    key, value = line.split("\t", 1)
    value = json.loads(value)
    return key, value["currRank"], value["prevRank"]

for i in range(20):
    heapq.heappush(heap, (0.0, -1))

for line in sys.stdin:
    nodeID, currRank, prevRank = parseInput(line)
    if nodeID != iterId:
        sys.stdout.write(line)
        N += 1
        sumDiff += (currRank - prevRank) ** 2
        heapq.heappushpop(heap, (currRank, nodeID))
    else:
        iteration = currRank

if math.sqrt(sumDiff) < convergenceDiff:
    converged = True

if converged or iteration >= max_iter:
    for i in range(N):
        printOutput(str(i), {})
    printOutput(heapId, {"heap": heap})
else:
    printOutput(iterId, {"currRank": iteration + 1, "prevRank": iteration, "outLinks": []})
