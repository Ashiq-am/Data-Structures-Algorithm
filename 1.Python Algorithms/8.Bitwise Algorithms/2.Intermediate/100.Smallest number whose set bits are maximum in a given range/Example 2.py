# Python code to find number whose set
# bits are maximum among 'l' and 'r'

def countMaxSetBits(left, right):
    while (left | (left + 1)) <= right:
        left |= left + 1
    return left


# driver code
l = 1
r = 5
print(countMaxSetBits(l, r))
l = 1
r = 10
print(countMaxSetBits(l, r))

# This code is contributed by "Abhishek Sharma 44"
