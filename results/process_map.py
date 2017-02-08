#!/usr/bin/env python

import heapq
import json
import sys

heap = []
lines = []
converged = True

for i in range(20):
    heapq.heappush(heap, (0.0, -1))

for line in sys.stdin:
    lines.append(line)
    cmps = line.split("\t")
    nodeID = int(cmps[0].split(":")[1])
    currRank = float(cmps[1].split(",")[0])
    prevRank = float(cmps[1].split(",")[1])
    if abs(currRank - prevRank) > 0.1:
        converged = False

    heapq.heappushpop(heap, (currRank, nodeID))

    #sys.stdout.write(line)
if converged:
    sys.stdout.write("R\t" + json.dumps(heap) + "\n")
else:
    for line in lines:
        sys.stdout.write(line)
