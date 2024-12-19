# Python3 code to find area
# and total surface area of cube

# utility function
def areaCube( a ):
	return (a * a * a)

def surfaceCube( a ):
	return (6 * a * a)

# driver function
a = 5
print("Area =", areaCube(a))
print("Total surface area =", surfaceCube(a))

