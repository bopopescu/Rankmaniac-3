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
    
    sys.stdout.write(line)
