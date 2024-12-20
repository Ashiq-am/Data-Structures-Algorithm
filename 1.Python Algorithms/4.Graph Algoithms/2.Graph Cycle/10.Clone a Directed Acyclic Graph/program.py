# Python program to clon a directed acyclic graph.

# Class to create a new graph node
class Node():

	# key is the value of the node
	# adj will be holding a dynamic
	# list of all Node type neighboring
	# nodes
	def __init__(self, key = None, adj = None):
		self.key = key
		self.adj = adj

# Function to print a graph, depth-wise, recursively
def printGraph(startNode, visited):

	# Visit only those nodes who have any
	# neighboring nodes to be traversed
	if startNode.adj is not None:

		# Loop through the neighboring nodes
		# of this node. If source node not already
		# visited, print edge from source to
		# neighboring nodes. After visiting all
		# neighbors of source node, mark its visited
		# flag to true
		for i in startNode.adj:
			if visited[startNode.key] == False :
				print("edge %s-%s:%s-%s"%(hex(id(startNode)), hex(id(i)), startNode.key, i.key))
				if visited[i.key] == False:
					printGraph(i, visited)
					visited[i.key] = True

# Function to clone a graph. To do this, we start
# reading the original graph depth-wise, recursively
# If we encounter an unvisited node in original graph,
# we initialize a new instance of Node for
# cloned graph with key of original node
def cloneGraph(oldSource, newSource, visited):
	clone = None
	if visited[oldSource.key] is False and oldSource.adj is not None:
		for old in oldSource.adj:

			# Below check is for backtracking, so new
			# nodes don't get initialized everytime
			if clone is None or(clone is not None and clone.key != old.key):
				clone = Node(old.key, [])
			newSource.adj.append(clone)
			cloneGraph(old, clone, visited)

			# Once, all neighbors for that particular node
			# are created in cloned graph, code backtracks
			# and exits from that node, mark the node as
			# visited in original graph, and traverse the
			# next unvisited
			visited[old.key] = True
	return newSource

# Creating DAG to be cloned
# In Python, we can do as many assignments of
# variables in one single line by using commas
n0, n1, n2 = Node(0, []), Node(1, []), Node(2, [])
n3, n4 = Node(3, []), Node(4)
n0.adj.append(n1)
n0.adj.append(n2)
n1.adj.append(n2)
n1.adj.append(n3)
n1.adj.append(n4)
n2.adj.append(n3)
n3.adj.append(n4)

# flag to check if a node is already visited.
# Stops indefinite looping during recursion
visited = [False]* (5)
print("Graph Before Cloning:-")
printGraph(n0, visited)

visited = [False]* (5)
print("\nCloning Process Starts")
clonedGraphHead = cloneGraph(n0, Node(n0.key, []), visited)
print("Cloning Process Completes.")

visited = [False]*(5)
print("\nGraph After Cloning:-")
printGraph(clonedGraphHead, visited)
