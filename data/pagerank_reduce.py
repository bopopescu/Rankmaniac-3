#!/usr/bin/env python

import sys

N = 1000
alpha = 0.85


def parseInput(line):
    cmps = line.split("\t")
    arr = cmps[1].split(",")
    nodeID = int(cmps[0])
    parentID = int(arr[0])
    rank = float(arr[1])
    numLinks = int(arr[2])
    return nodeID, parentID, rank, numLinks


def printOutput(nodeID, newRank):
    # print nodeID
    sys.stdout.write("FinalRank:" + str(newRank) + " " + str(nodeID) + "\n")

def computeRank(nodeID, values):
    summation = 0
    for (_, rank, numLinks) in values:
        summation += rank / numLinks
    newRank = (1 - alpha) / N + alpha * summation
    return nodeID, newRank

# nodeid\t parentid,rank,numberoflinks
lastKey = -1
values = []

for line in sys.stdin:
    nodeID, parentID, rank, numLinks = parseInput(line)
    if lastKey == -1:
        lastKey = nodeID
    if nodeID != lastKey:
        (oldNodeID, newRank) = computeRank(lastKey, values)
        printOutput(oldNodeID, newRank)
        lastKey = nodeID
        values = []
    values.append((parentID, rank, numLinks))
