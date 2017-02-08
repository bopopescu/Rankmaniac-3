#!/usr/bin/env python

import heapq
import json
import sys

heaps = []
done = False

for line in sys.stdin:
    if line.startswith("R"):
        done = True
        heaps.append(json.loads(line.split("\t")[1]))
    else:
        sys.stdout.write(line)

if done:
    heap = heapq.merge(*heaps)
    for (rank, node) in heapq.nlargest(20, heap):
        sys.stdout.write("FinalRank:" + str(rank) + "\t" + str(node) + "\n")
