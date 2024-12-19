# Python code to find number whose set
# bits are maximum among 'l' and 'r'

def countMaxSetBits(left, right):
    max_count = -1
    for i in range(left, right + 1):
        temp = i
        cnt = 0

        # Traverse for every bit of 'i'
        # number
        while temp:
            if temp & 1:
                cnt += 1
            temp = temp >> 1

        # If count is greater than previous
        # calculated max_count, update it
        if cnt > max_count:
            max_count = cnt
            num = i
    return num


# driver code
l = 1
r = 5
print(countMaxSetBits(l, r))
l = 1
r = 10
print(countMaxSetBits(l, r))

# This code is contributed by "Abhishek Sharma 44"
