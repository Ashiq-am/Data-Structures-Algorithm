# Python3 program to check divisibility in a stream

''' A very simple implementation of the logic,
	without error handling. just to demonstrate
	the above theory. This simple version not
	restricting user from typing 000, 00 , 000.. ,
	because this all will be same as 0 for integer
	same is true for 1, 01, 001, 000...001 is same
	as 1, so ignore this type of error handling
	while reading just see the main logic is correct. '''


def CheckDivisibility(n):
    remainder = 0
    print("press any key other than 0"
          " and 1 to terminate")
    while (True):

        # Read next incoming bit via standard
        # input. 0, 00, 000.. are same as int 0
        # ans 1, 01, 001, 00..001 is same as 1.
        incomingBit = int(input())

        # Update remainder
        if (incomingBit == 1):
            remainder = (remainder * 2 + 1) % n
        elif (incomingBit == 0):
            remainder = (remainder * 2) % n
        else:
            break

        # If remainder is 0.
        if (remainder % n == 0):
            print("yes")
        else:
            print("no")


# Driver code
CheckDivisibility(3)

# this code is contributed by phasing17
