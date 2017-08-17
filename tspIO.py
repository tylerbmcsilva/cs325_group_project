# Benjamin C. Rodarte CS 325 TSP Project Team 6

import math

# reads input file where each line is: vertex# x-coord y-coord


def buildAdjacencyMatrix(inputFileName):
	with open(inputFileName) as f:
		nodes = [tuple(map(int, i.split())) for i in f]

	print "done reading from file"

	numNodes = len(nodes)

	# create a weighted adjacency matrix from input graph
	# using Euclidean distance as edge weights
	w, h = numNodes, numNodes
	Matrix = [[-1 for x in range(w)] for y in range(h)]

	for i in range(0, numNodes):
		for j in range(0, numNodes):
			if i == j:
				Matrix[i][j] = 0
			elif Matrix[i][j] == -1:
				dx = nodes[j][1] - nodes[i][1]
				dy = nodes[j][2] - nodes[i][2]
				Matrix[i][j] = int(round(math.sqrt(dx * dx + dy * dy)))
				Matrix[j][i] = Matrix[i][j]

	print "done calculating adjacency matrix"
	return Matrix


# writes a solution (tour and tour length) to a specified output file


def printTour(tour, length, outputFileName):
	with open(outputFileName, 'w') as o:
		print >> o, length
		for vertex in tour:
			print >> o, vertex
