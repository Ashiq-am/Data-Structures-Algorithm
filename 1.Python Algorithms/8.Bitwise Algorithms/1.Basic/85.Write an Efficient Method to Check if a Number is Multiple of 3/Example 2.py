# Python program to check if n is a multiple of 3
dp = [-1 for i in range(1001)];

''' Function to check if n is a multiple of 3 '''


def isMultipleOf3(n):
    odd_count = 0;
    even_count = 0;

    # Base Cases
    if (n < 0):
        n = -n;

    if (n == 0):
        return 1;

    if (n == 1):
        return 0;

    # If a value is already present
    # in dp, return it
    if (dp[n] != -1):
        return dp[n];

    while (n > 0):
        '''
        * If odd bit is set then increment odd counter
        '''
        if ((n & 1) != 0):
            odd_count += 1;

        '''
        * If even bit is set then increment even counter
        '''
        if ((n & 2) != 0):
            even_count += 1;
        n = n >> 2;

    dp[n] = isMultipleOf3(abs(odd_count - even_count));

    # return dp
    return dp[n];


''' Program to test function isMultipleOf3 '''
if __name__ == '__main__':
    num = 24;

    if (isMultipleOf3(num) == 1):
        print(num, "is multiple of 3");
    else:
        print(num, " is not a multiple of 3");

# This code is contributed by Rajput-Ji
