# Python program to check if the binary String is divisible
# by 3.

# Function to check if the binary String is divisible by 3.
def CheckDivisibilty(A):
    oddbits = 0;
    evenbits = 0;
    for counter in range(len(A)):

        # checking if the bit is nonzero
        if (A[counter] == '1'):

            # checking if the nonzero bit is at even
            # position
            if (counter % 2 == 0):
                evenbits += 1;
            else:
                oddbits += 1;

    # Checking if the difference of non-zero oddbits and
    # evenbits is divisible by 3.
    if (abs(oddbits - evenbits) % 3 == 0):
        print("Yes" + "");
    else:
        print("No" + "");


# Driver Program
if __name__ == '__main__':
    A = "10101";
    CheckDivisibilty(A);

# This code is contributed by umadevi9616.
