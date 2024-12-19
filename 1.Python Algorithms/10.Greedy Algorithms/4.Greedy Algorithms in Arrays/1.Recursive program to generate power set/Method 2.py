# Python3 program to generate power set
def powerSet(string, index, curr):
    # string : Stores input string
    # curr : Stores current subset
    # index : Index in current subset, curr
    if index == len(string):
        print(curr)
        return

    powerSet(string, index + 1,
             curr + string[index])
    powerSet(string, index + 1, curr)


# Driver Code
if __name__ == "__main__":
    s1 = "abc"
    index = 0
    curr = ""
    powerSet(s1, index, curr)
