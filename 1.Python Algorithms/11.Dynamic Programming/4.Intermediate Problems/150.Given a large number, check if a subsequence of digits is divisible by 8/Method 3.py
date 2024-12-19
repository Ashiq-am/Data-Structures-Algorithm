# Python3 program to check if given string
# has a subsequence divisible by 8
Str = "129365"

# map key will be tens place digit of number
# that is divisible by 8 and value will
# be units place digit
mp = {}

# For filling the map let start
# with initial value 8
no = 8

while (no < 100):
    no = no + 8

    # key is digit at tens place and value is
    # digit at units place mp.insert({key, value})
    mp[(no // 10) % 10] = no % 10

# Create a hash to check if we visited a number
visited = [False] * 10

# Iterate from last index to 0th index
for i in range(len(Str) - 1, -1, -1):

    # If 8 is present in string then
    # 8 divided 8 hence print yes
    if (Str[i] == '8'):
        print("Yes", end="")
        break

    # considering present character as the second
    # digit of two digits no we check if the value
    # of this key is marked in hash or not
    # If marked then we a have a number divisible by 8
    if visited[mp[ord(Str[i]) - ord('0')]]:
        print("Yes", end="")
        break

    visited[ord(Str[i]) - ord('0')] = True

# If no subsequence divisible by 8
if (i == -1):
    print("No")
