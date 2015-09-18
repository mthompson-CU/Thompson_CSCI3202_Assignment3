# Author: Matthew Thompson
# IdentiKey: math1906
# Date: September 15, 2015
# Assignment 3

import sys
import AStarNode

def discoverNeighbors(node, world):
	return

# inspired by http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html
def calculateManhattan(node, goalNode):
	distance = 0
	currentNode = node
	while (currentNode != neighborNode):
		dx = abs(currentNode.x - neighborNode.x)
    	dy = abs(currentNode.y - neighborNode.y)

def main(argv):
	# Ensure the proper number of arguments is provided

	if (len(argv) != 3):
		print 'Usage: Thompson_CSCI3202_Assignment3.py [-m: Manhattan heuristic] [-o: Euclidean heuristic] filename'
		return

	# Determine the heuristic to use

	if (argv[1] == '-m'):
		heuristic = 'm'
		chosenWorldFile = argv[2]
	elif (argv[1] == '-e'):
		heuristic = 'e'
		chosenWorldFile = argv[2]
	else:
		print 'You must specify a valid heueristic to use'
		print 'Use "-m" for the Manhattan heueristic and "-e" for the Euclidean heuristic'
		return
	
	# Read world file into program

	world = []

	worldFile = open(chosenWorldFile, 'r')

	for line in worldFile:
		lineArray = line.split()
		if (len(lineArray) != 0):
			world.append(lineArray)

	print 'World: ' + argv[2]
	print world

	# Use A* Search

	# a_star(start, goal, world)

	return

if __name__ == '__main__':
	main(sys.argv)