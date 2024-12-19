# Python program to find total area of two
# overlapping Rectangles
# Returns Total Area of two overlap
# rectangles


def overlappingArea(l1, r1, l2, r2):
	x = 0
	y = 1

	# Area of 1st Rectangle
	area1 = abs(l1[x] - r1[x]) * abs(l1[y] - r1[y])

	# Area of 2nd Rectangle
	area2 = abs(l2[x] - r2[x]) * abs(l2[y] - r2[y])

	''' Length of intersecting part i.e 
		start from max(l1[x], l2[x]) of 
		x-coordinate and end at min(r1[x], 
		r2[x]) x-coordinate by subtracting 
		start from end we get required 
		lengths '''
	x_dist = (min(r1[x], r2[x]) -
			max(l1[x], l2[x]))

	y_dist = (min(r1[y], r2[y]) -
			max(l1[y], l2[y]))
	areaI = 0
	if x_dist > 0 and y_dist > 0:
		areaI = x_dist * y_dist

	return (area1 + area2 - areaI)


# Driver's Code
l1 = [2, 2]
r1 = [5, 7]
l2 = [3, 4]
r2 = [6, 9]

# Function call
print(overlappingArea(l1, r1, l2, r2))

# This code is contributed by Manisha_Ediga
