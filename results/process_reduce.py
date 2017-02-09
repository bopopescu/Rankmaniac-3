#!/usr/bin/env python

import heapq
import json
import sys

prevNode = -1
mode = "normal"

def parseInput(line):
    key, value = line.split("\t", 1)
    node = key.split(":")[1]
    return node, value

def processNode(node, values):
    if len(values) == 1 and node != "R":
        sys.stdout.write("NodeId:" + node + "\t" + values[0])
    elif node == "R":
        heap = json.loads(values[0])
        for (rank, node) in heapq.nlargest(20, heap):
            sys.stdout.write("FinalRank:" + str(rank) + "\t" + str(node) + "\n")


lastKey = -1
values = []

for line in sys.stdin:
    node, value = parseInput(line)
    if lastKey == -1:
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
