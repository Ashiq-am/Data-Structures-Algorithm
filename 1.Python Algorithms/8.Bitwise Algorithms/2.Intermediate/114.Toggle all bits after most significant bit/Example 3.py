# Python3 program to toggle set
# bits starting from MSB
from math import log

# Returns a number which has all set bits
# starting from MSB of n
def toggle(num):

	# the number of bits is equal to log2num + 1
	n = int(log(num, 2)) + 1

	# calculating mask
	mask = pow(2, n) - 1

	# toggling bits using xor with mask
	return num ^ mask

# Driver code
num = 10
print(toggle(num))

# This code is contributed by phasing17
