# Python3 code to approximate number
# of people in Birthday Paradox problem
import math

# Returns approximate number of
# people for a given probability
def find( p ):
	return math.ceil(math.sqrt(2 * 365 * math.log(1/(1-p))))

# Driver Code
print(find(0.70))
