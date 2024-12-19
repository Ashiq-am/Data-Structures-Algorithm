# Python3 program to find degree of a vertex.

# Structure of Graph
class Graph:

	# vertices and edges
	v = None
	e = None
	diri = []

	# Graph Constructor
	def __init__(self, v, e):
		self.v = v
		self.e = e
		self.diri = [[0 for i in range(v)]
						for j in range(v)]

def createGraph(v, e):
	G = Graph(v, e)

	# /* 0-----1
	# | \ |
	# | \ |
	# | \ |
	# 2-----3 */

	# direction from 0
	G.diri[0][1] = 1
	G.diri[0][2] = 1
	G.diri[0][3] = 1

	# direction from 1
	G.diri[1][0] = 1
	G.diri[1][3] = 1

	# direction from 2
	G.diri[2][0] = 1
	G.diri[2][3] = 1

	# direction from 3
	G.diri[3][0] = 1
	G.diri[3][1] = 1
	G.diri[3][2] = 1

	return G

def findDegree(G, ver):
	degree = 0
	for i in range(G.v):
		if G.diri[ver][i] == 1:
			degree += 1
	if G.diri[ver][ver] == 1:
		degree += 1
	return degree

# Driver Code
if __name__ == "__main__":

	vertices = 4
	edges = 5

	# Creating a Graph
	G = createGraph(vertices, edges)

	ver = 0

	# Function calling
	degree = findDegree(G, ver)
	print(degree)
