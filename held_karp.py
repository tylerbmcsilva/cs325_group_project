import math
import sys
import timeit  # to stop improving approximation after 3 minutes

import tspIO  # buildAdjacencyMatrix(inputFileName)

inputFileName = sys.argv[1]
outputFileName = inputFileName + ".tour"

#read input file and create a weighted adjacency matrix
Matrix = tspIO.buildAdjacencyMatrix(inputFileName)

"""
Implementation of Held Karp algorithm based off pseudocode from Wikipedia

When initializing, you must pass a distance matrix
To run: [variable].main()
"""
class HeldKarp:
	# Initializes setup, sets optimal distance to infinity 
	def __init__(self, input_matrix):
		# Set optimal distance equal to infinity
		self.optimal_distance = float("inf")
		# Set optimal path equal to an empty array
		# self.optimal_path = []
		# Set distances equal to the input matrix
		self.distances = input_matrix

	# Start of algorithm, once it completes run, then prints the result to the console
	def main(self):
		# Create an array of indices
		vertices = list(range(1, len(self.distances)-1))
		# Call the inital recursive function
		self.__held_karp(0, vertices, 0)

		# Print the results
		# print self.optimal_path
		print self.optimal_distance

		# Print to file
		# tspIO.printTour(self.optimal_path, self.optimal_distance, outputFileName)

	# Main part of algorithm, recursive, checks every vertice and all subchildren for shortest paths
	def __held_karp(self, initial, vertices, cost_until_here): # Removed `path` argument as it was not working as intended
		# Put the initial index in the path array
		# path.append(initial)
		# Calculate the length_vertices of the vertices array
		length_vertices = len(vertices)
		# Set new variable to find the new cost
		new_cost_until_here = float("inf")
		# If there is no vertices
		if (length_vertices == 0):
			# Set new cost til here equal to costToHere + distance of initial
			new_cost_until_here = cost_until_here + self.distances[initial][0]
			# If it's lower, than store it!
			if (new_cost_until_here < self.optimal_distance):
				# Store distance
				self.optimal_distance = new_cost_until_here
				# Store path
				# self.optimal_path = path
			# Return distance from index
			return self.distances[initial][0]
		# If it's too high, don't move forward
		elif (cost_until_here > self.optimal_distance):
			return 0
		# All other cases
		else:
			# Create new matrix of vertices
			new_vertices = [[None for x in range(length_vertices - 1)] for y in range(length_vertices)]
			# Initialize variables
			cost_current_node = float("inf")
			cost_child = float("inf")
			best_cost = float("inf")
			# For each node in vertices array
			for i in range(0, length_vertices):
				k = 0
				for j in range(0, length_vertices):
					# The current child is not stored in the new vertices array
					if (j == i):
						continue
					new_vertices[i][k] = vertices[j]
					k += 1
				# If the vertex is None, pass it
				if(vertices[i] is None):
					continue
				# Find current cost
				cost_current_node = self.distances[initial][vertices[i]]
				# Calculate new cost
				new_cost_until_here = cost_current_node + cost_until_here
				# Find cost of all children of vertice
				cost_child = self.__held_karp(vertices[i], new_vertices[i], new_cost_until_here)
				# Calculate total cost
				total_cost = cost_child + cost_current_node
				# Store the cost if it's the best
				if (total_cost < best_cost):
					best_cost = total_cost
			# Return best cost
			return best_cost


Test = HeldKarp(Matrix)
Test.main()