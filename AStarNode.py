# Author: Matthew Thompson
# IdentiKey: math1906
# Date: September 16, 2015
# Assignment 3
# Implements a node to used in an A* Search
# Inspired by assignment description

class AStarNode():
	def __init__ (self, x, y, distanceToStart, heuristicDistance, f, parent=None):
		self.x = x
		self.y = y
		self.distanceToStart = distanceToStart
		self.heuristicDistance = heuristicDistance
		self.f = f
		self.parent = parent



