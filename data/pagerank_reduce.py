#!/usr/bin/env python

import sys
import json

alpha = 0.85
iterId = -2

def parseInput(line):
    key, value = line.split("\t", 1)
    key = int(key)
    value = json.loads(value)
    return key, value

def printOutput(messageKey, data):
    sys.stdout.write(str(messageKey) + "\t" + json.dumps(data) + "\n")

def computeRank(nodeId, values):
    outLinks = []
    prevRank = 0.0
    summation = 0
    for v in values:
        if v["dataType"] == "meta":
            outLinks = v["outLinks"]
            prevRank = v["currRank"]
        elif v["dataType"] == "inLink":
            summation += v["parentRank"] / v["parentOutCount"]
    if nodeId == iterId:
        currRank = v["currRank"]
    else:
        currRank = (1 - alpha) + alpha * summation
    printOutput(nodeId, {"prevRank": prevRank, "currRank": currRank, "outLinks": outLinks})

lastKey = None
values = []

for line in sys.stdin:
    nodeId, value = parseInput(line)
    if lastKey is None:
        lastKey = nodeId
    if nodeId != lastKey:
        computeRank(lastKey, values)
        lastKey = nodeId
        values = []
    values.append(value)
computeRank(lastKey, values)
