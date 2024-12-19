# Python3 program to check if a number
# is power of 8

# function to check if power of 8
def checkPowerof8(n):
    return (n and not (n & (n - 1)) and
            not (n & 0xB6DB6DB6))


# Driver Code
if __name__ == "__main__":
    n = 65

if checkPowerof8(n):
    print("Yes")
else:
    print("No")

# This code is contributed by ita_c
