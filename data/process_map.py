#!/usr/bin/env python

import heapq
import json
import sys

convergenceDiff = 0.1

iteration = 1

max_iter = 50

N = 0
heap = []
converged = True

heapId = -1
iterId = -2

def printOutput(messageKey, data):
    sys.stdout.write(str(messageKey) + "\t" + json.dumps(data) + "\n")

def parseInput(line):
    key, value = line.split("\t", 1)
    key = int(key)
    value = json.loads(value)
    return key, value["currRank"], value["prevRank"]

for i in range(20):
    heapq.heappush(heap, (0.0, -1))

for line in sys.stdin:
    nodeID, currRank, prevRank = parseInput(line)
    if nodeID >= 0:
        sys.stdout.write(line)
        N += 1
        if abs(currRank - prevRank) > convergenceDiff:
            converged = False
        heapq.heappushpop(heap, (currRank, nodeID))
    else:
        iteration = currRank




if converged or iteration >= max_iter:
    for i in range(N):
        printOutput(i, {})
    printOutput(heapId, {"heap": heap})
else:
    printOutput(iterId, {"currRank": iteration + 1, "prevRank": iteration, "outLinks": []})
