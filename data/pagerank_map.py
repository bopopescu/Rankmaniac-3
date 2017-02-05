#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:
    cmps = line.split("\t")
    arr = cmps[1].split(",")
    nodeID = int(cmps[0].split(":")[1])
    currRank = float(arr[0])
    prevRank = float(arr[1])
    outLinks = map(int, arr[2:])

    # print "CurrRank: %d" %currRank
    # print "OutLinks: " + str(len(outLinks))
    # print "nodeID: %d" %nodeID
    # print "arr: " + str(arr)

    rankString = str(currRank)
    linkString = str(len(outLinks))
    parentIDString = str(nodeID)

    for child in outLinks:
        outLine = str(child) + "\t" + parentIDString + "," + rankString + "," + linkString + "\n"
        sys.stdout.write(outLine)
