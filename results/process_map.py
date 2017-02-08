#!/usr/bin/env python

import heapq
import json
import sys

heap = []
for i in range(20):
    heapq.heappush(heap, (0.0, -1))

for line in sys.stdin:
    cmps = line.split("\t")
    nodeID = int(cmps[0].split(":")[1])
    rank = float(cmps[1].split(",")[0])

    heapq.heappushpop(heap, (rank, nodeID))

    #sys.stdout.write(line)
sys.stdout.write("R\t" + json.dumps(heap) + "\n")
