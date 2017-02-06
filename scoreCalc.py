import math
import numpy

def scoreCalculator(outputFile, answerFile):

# input: file names of our ranks, correct ranks as strings
# output: (sum of square differences, pentalty time)

	# reads in the rank and node columns
	rank, node = numpy.genfromtxt(outputFile, unpack = True)
	correctRank, correctNode = numpy.genfromtxt(answerFile, unpack = True)
	
	index = 0
	incorrectNodes = []
	error = 0

	# creates a list of incorrectly ordered nodes
	while index < len(node):
		if node[index] != correctNode[index]:
			incorrectNodes.append(node[index])
		index += 1

	# gets our rank vs. the correct rank 
	for element in incorrectNodes:
		node = list(node)
		correctNode = list(correctNode)

		ourRank = node.index(element) + 1
		try:
			correctRank = correctNode.index(element) + 1
		except:
			print "We got issues, this isn't in the answer file."

		# calculates error
		error += (correctRank - ourRank) ** 2
		
	penaltySeconds = error * 30

	return (error, penaltySeconds)