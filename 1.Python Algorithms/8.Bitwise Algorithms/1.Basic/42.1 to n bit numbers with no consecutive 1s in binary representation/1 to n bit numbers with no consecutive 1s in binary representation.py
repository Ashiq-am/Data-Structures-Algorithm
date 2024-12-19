# Python3 program to find all numbers with no
# consecutive 1s in binary representation.
h = {}


def numberWithNoConsecutiveOnes(n, sol):
    global h

    # If it is in limit i.e. of n lengths in binary
    if len(sol) <= n:
        ans = 0
        for i in range(len(sol)):
            ans += pow(2, i) * sol[len(sol) - 1 - i]
        h[ans] = 1
        h[4] = 1
        h[8] = 1
        h[9] = 1

        # Last element in binary
        last_element = sol[len(sol) - 1]

        # if element is 1 add 0 after it else
        # If 0 you can add either 0 or 1 after that
        if last_element == 1:
            sol.append(0)
            numberWithNoConsecutiveOnes(n, sol)
        else:
            sol.append(1)
            numberWithNoConsecutiveOnes(n, sol)
            sol.pop()
            sol.append(0)
            numberWithNoConsecutiveOnes(n, sol)


n = 4
sol = []

# Push first number
sol.append(1)

# Generate all other numbers
numberWithNoConsecutiveOnes(n, sol)

for i in sorted(h.keys()):
    print(i, end=" ")

# This code is contributed by divyesh072019.
