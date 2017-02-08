#!/usr/bin/env python

import heapq
import json
import sys

heaps = []

for line in sys.stdin:
    heaps.append(json.loads(line.split("\t")[1]))

heap = heapq.merge(*heaps)
for (rank, node) in heapq.nlargest(20, heap):
    sys.stdout.write("FinalRank:" + str(rank) + " " + str(node) + "\n")
