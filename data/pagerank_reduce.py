#!/usr/bin/env python

import sys
import json

alpha = 0.85

def parseInput(line):
    key, value = line.split("\t", 1)
    key = int(key)
    value = json.loads(value)
    return key, value

def printOutput(nodeID, newRank):
    sys.stdout.write("FinalRank:" + str(newRank) + " " + str(nodeID) + "\n")

def computeRank(nodeID, values):
    N = 0
    outLinks = []
    prevRank = 0.0
    summation = 0
    for v in values:
        if v["data"] == "maxNodeID":
            N = max(N, v["maxNodeID"])
        elif v["data"] == "meta":
            outLinks = v["outLinks"]
            prevRank = v["currRank"]
        elif v["data"] == "inLink":
            summation += v["rank"] / v["numOut"]
    newRank = (1 - alpha) / N + alpha * summation
    outLinksStr = ""
    if len(outLinks) > 0:
        outLinksStr = "," + ",".join(map(str, outLinks))
    sys.stdout.write("NodeId:" + str(nodeID) + "\t" + str(newRank) + "," +
                     str(prevRank) + outLinksStr + "\n")

lastKey = -1
values = []

for line in sys.stdin:
    nodeID, value = parseInput(line)
    if lastKey == -1:
        lastKey = nodeID
    if nodeID != lastKey:
        computeRank(lastKey, values)
        lastKey = nodeID
        values = []
    values.append(value)
computeRank(lastKey, values)
