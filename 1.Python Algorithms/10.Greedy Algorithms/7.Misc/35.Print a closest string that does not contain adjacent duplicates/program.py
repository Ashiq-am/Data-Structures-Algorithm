# Python program to print a string with
# no adjacent duplicates by doing minimum
# changes to original string

# Function to print simple string
def noAdjacentDup(s):
    n = len(s)
    for i in range(1, n):

        # If any two adjacent characters are equal
        if (s[i] == s[i - 1]):

            s[i] = "a"  # Initialize it to 'a'

            # Traverse the loop until it is different
            # from the left and right letter.
            while (s[i] == s[i - 1] or
                   (i + 1 < n and s[i] == s[i + 1])):
                s[i] += 1

            i += 1

    return s


# Driver Function
s = list("geeksforgeeks")
print("".join(noAdjacentDup(s)))
