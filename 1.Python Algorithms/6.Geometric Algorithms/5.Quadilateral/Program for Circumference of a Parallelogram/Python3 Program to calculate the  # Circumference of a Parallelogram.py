# Python3 Program to calculate the
# Circumference of a Parallelogram

# Utility Function
def circumferenceparallelogram(a,b):
	return ((2 * a) + (2 * b))

# Driver Function
a = 10
b = 8

print("Circumference of a given Parallelogram is :",
		round(circumferenceparallelogram(a, b),4)) 
