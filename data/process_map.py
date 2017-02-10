#!/usr/bin/env python

import heapq
import json
import sys

convergenceThresh = 3

iteration = 1
prev_epsilon = -1

max_iter = 50

N = 0
heap = []
converged = False

heapId = "-1"
iterId = "-2"
epsilonId = "-3"

def printOutput(messageKey, data):
    sys.stdout.write(messageKey + "\t" + json.dumps(data) + "\n")

def getEpsilon(heap):
    t = heapq.nlargest(20, heap)
    return min([t[i][0] - t[i + 1][0] for i in range(len(t) - 1)])

def parseInput(line):
    key, value = line.split("\t", 1)
    value = json.loads(value)
    return key, value

for i in range(20):
    heapq.heappush(heap, (0.0, -1))

for line in sys.stdin:
    nodeId, value = parseInput(line)
    if nodeId == iterId:
        iteration = value["iteration"] + 1
    elif nodeId == epsilonId:
        prev_epsilon = value["epsilon"]
    else:
        currRank = value["currRank"]
        prevRank = value["prevRank"]
        sys.stdout.write(line)
        N += 1
        heapq.heappushpop(heap, (currRank, nodeId))

new_epsilon = getEpsilon(heap)
if new_epsilon <= (prev_epsilon / convergenceThresh) or iteration >= max_iter:
    for i in range(N):
        printOutput(str(i), {"converged": True})
    printOutput(heapId, {"heap": heap})
else:
    printOutput(iterId, {"iteration": iteration})
    printOutput(epsilonId, {"epsilon": new_epsilon})
