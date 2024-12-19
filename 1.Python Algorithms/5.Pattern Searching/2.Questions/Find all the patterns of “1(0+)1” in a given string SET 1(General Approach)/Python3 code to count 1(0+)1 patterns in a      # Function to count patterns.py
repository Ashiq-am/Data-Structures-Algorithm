# Python3 code to count 1(0+)1 patterns in a

# Function to count patterns
def patternCount(str):
    # Variable to store the last character
    last = str[0]

    i = 1;
    counter = 0
    while (i < len(str)):

        # We found 0 and last character was '1',
        # state change
        if (str[i] == '0' and last == '1'):
            while (str[i] == '0'):
                i += 1

                # After the stream of 0's, we got a '1',
                # counter incremented
                if (str[i] == '1'):
                    counter += 1

        # Last character stored
        last = str[i]
        i += 1

    return counter


# Driver Code
str = "1001ab010abc01001"
ans = patternCount(str)
print(ans)
