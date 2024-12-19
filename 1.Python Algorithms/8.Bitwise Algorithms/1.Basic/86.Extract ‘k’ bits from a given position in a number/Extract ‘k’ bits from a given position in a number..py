# Python program to extract k bits from a given
# position.

# Function to extract k bits from p position
# and returns the extracted value as integer
def bitExtracted(number, k, p):
	return ( ((1 << k) - 1) & (number >> (p-1) ) );

# number is from where 'k' bits are extracted
# from p position
number = 171
k = 5
p = 2
print ("The extracted number is ", bitExtracted(number, k, p))
