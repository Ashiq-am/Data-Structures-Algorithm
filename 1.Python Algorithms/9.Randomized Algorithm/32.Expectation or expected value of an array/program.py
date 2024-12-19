# python code to calculate expected
# value of an array

# Function to calculate expectation
def calc_Expectation(a, n):
    # variable prb is for probability
    # of each element which is same for
    # each element
    prb = 1 / n

    # calculating expectation overall
    sum = 0
    for i in range(0, n):
        sum += (a[i] * prb)

    # returning expectation as sum
    return float(sum)


# Driver program
n = 6;
a = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

# Function for calculating expectation
expect = calc_Expectation(a, n)

# Display expectation of given array
print("Expectation of array E(X) is : ",expect)
