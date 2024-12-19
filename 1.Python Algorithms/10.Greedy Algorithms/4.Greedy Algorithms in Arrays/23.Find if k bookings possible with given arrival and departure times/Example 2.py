# Python Code Implementation of the above approach
def areBookingsPossible(A, B, K):
		A.sort()
		B.sort()
		for i in range(len(A)):
			if i+K < len(A) and A[i+K] < B[i] :
				return "No"
		return "Yes"

if __name__ == "__main__":
	arrival = [1, 2, 3]
	departure = [2, 3, 4]
	K = 1
	print(areBookingsPossible(arrival,departure,K))


