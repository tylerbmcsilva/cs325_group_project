#Benjamin C. Rodarte CS 325 TSP Project Team 6

import tspIO


#tour should NOT contain the start vertex as the last vertex.
#tourLength() will add the distance from final vertex back to start.
def tourLength(tour, Matrix):
	numNodes = len(tour)
	sum = 0
	for i in range(0, numNodes - 1):
		sum += Matrix[tour[i]][tour[i + 1]]
	sum += Matrix[tour[-1]][tour[0]]
	#add edge that returns to start
	return sum


#Nearest Neighbor approximation of TSP
def approximate(Matrix, outputFileName):
	numNodes = len(Matrix)
	if numNodes > 1000:
		iterations = 10
		#for large graphs, just try first 10 in list
	else:
		iterations = numNodes
		#for small graphs, try starting from every node

	minDistPath = float('inf')
	bestTour = []
	for start in range(0, iterations):
		#start with empty tour and all vertices as "unvisited"
		tour = []
		unvisited = range(0, numNodes)
		current = start
		tour.append(current)
		#add start vertex to tour
		unvisited.remove(current)

		#keep adding next closest unvisited vertex to tour
		while unvisited:
			low = float('inf')
			for i in unvisited:
				if Matrix[current][i] < low:
					low = Matrix[current][i]
					nextMove = i
			current = nextMove
			unvisited.remove(nextMove)
			tour.append(nextMove)

		tourDist = tourLength(tour, Matrix)

		if tourDist < minDistPath:
			minDistPath = tourDist
			bestTour = tour
			tspIO.printTour(bestTour, minDistPath, outputFileName)

	return bestTour, minDistPath
