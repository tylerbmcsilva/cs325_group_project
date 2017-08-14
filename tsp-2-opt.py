#Benjamin C. Rodarte CS 325 TSP Project Team 6

import math
import sys
import tspIO                #buildAdjacencyMatrix(inputFileName)
import tspNearestNeighbor   #approximate(Matrix), tourLength(tour, Matrix)
import timeit               #to stop improving approximation after 3 minutes

inputFileName = sys.argv[1];
outputFileName = inputFileName + ".tour";

#if inf flag is set, then run for unlimited time, otherwise run for 3 min
if len(sys.argv) == 3:
    if sys.argv[2] == "inf":
        timeLimit = float('inf');
else:
    timeLimit = 180;

start_time = timeit.default_timer()

#read input file and create a weighted adjacency matrix
Matrix = tspIO.buildAdjacencyMatrix(inputFileName);

#find first-guess solution using Nearest-Neighbor 
appxTour, minLength = tspNearestNeighbor.approximate(Matrix, outputFileName);

lastSolutionTime = timeit.default_timer() - start_time;
print "NN approximation completed and printed to file at: " + str(round(lastSolutionTime, 2)) + " seconds.";
#print first guess to solution file
#tspIO.printTour(appxTour, minLength, outputFileName);

#utility function used by 2-OPT to swap 2 edges and ensure tour remains valid
def optSwap(i, k, bestTour):
	newTour = [];
	
	for c in range (0, i):
		newTour.append(bestTour[c]);
	
	counter = 0;
	for c in range (i, k+1):
		newTour.append(bestTour[k-counter]);
		counter += 1;
	
	for c in range (k+1, len(bestTour)):
		newTour.append(bestTour[c]);
	return newTour;

#2-OPT Algorithm
#For this implementation only swaps which create a tour that is no worse than
#the current tour are performed. This greatly reduces the runtime of the 
#algorithm over the naive version which checks every possible swap.
numNodes = len(appxTour);
improvement = 0;
while improvement < 20:         #stop if 20 iterations pass with no improvement
	for i in range (0, numNodes):
		for k in range (i+1, numNodes):
		    #check to see if proposed swap will make tour shorter
			removedPathLength = Matrix[appxTour[(i-1)%(numNodes)]][appxTour[i]]+Matrix[appxTour[k]][appxTour[(k+1)%(numNodes)]];
			addedPathLength = Matrix[appxTour[(i-1)%numNodes]][appxTour[k]]+Matrix[appxTour[i]][appxTour[(k+1)%(numNodes)]];
			if addedPathLength <= removedPathLength:  #only swap if new path would be at least as good as current
				newTour = optSwap(i, k, appxTour);
				newLength = tspNearestNeighbor.tourLength(newTour, Matrix);
				if newLength <= minLength:
					if newLength < minLength:  #don't reset if path length is same
						improvement = 0;
					appxTour = newTour;
					minLength = newLength;
					#if time limit hasn't elapsed, print latest solution
					if timeit.default_timer() - start_time < timeLimit:
					    tspIO.printTour(appxTour, minLength, outputFileName);
					    lastSolutionTime = timeit.default_timer() - start_time;
					else:
					    sys.exit("Time limit reached. See " + outputFileName + " for best solution found at " + str(round(lastSolutionTime, 2)) + " seconds.");
	improvement += 1; 
	
elapsed = timeit.default_timer() - start_time
print "tsp-2-opt has successfully completed execution in " + str(round(elapsed,2)) + " seconds."; 
print "Please see " + str(outputFileName) + " for the results.";