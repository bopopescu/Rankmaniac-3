#!/usr/bin/env python

import heapq
import json
import sys

convergenceDiff = 0.1

N = 0
heap = []
converged = True

for i in range(20):
    heapq.heappush(heap, (0.0, -1))

for line in sys.stdin:
    sys.stdout.write(line)
    N += 1
    cmps = line.split("\t")
    nodeID = int(cmps[0].split(":")[1])
    currRank = float(cmps[1].split(",")[0])
    prevRank = float(cmps[1].split(",")[1])
    if abs(currRank - prevRank) > convergenceDiff:
        converged = False

    heapq.heappushpop(heap, (currRank, nodeID))

    #sys.stdout.write(line)
if converged:
    for i in range(N):
        sys.stdout.write("NodeId:" + str(i) + "\tCONVERGED\n")
    sys.stdout.write("Result:R\t" + json.dumps(heap) + "\n")
