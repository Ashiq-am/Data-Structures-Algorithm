# Python3 program to evaluate 7n/8
# without using * and /

def multiplyBySevenByEight(n):
    # Step 1) First multiply number
    # by 7 i.e. 7n = (n << 3) -n
    # Step 2) Divide result by 8
    return ((n << 3) - n) >> 3;


# Driver code
n = 15;
print(multiplyBySevenByEight(n));

# this code is contributed by sam007.
