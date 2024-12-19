# Python3 Program to print 0, 1 or 2 with equal
# Probability

import random


# Random Function to that returns 0 or 1 with
# equal probability

def rand2():
    # randint(0,100) function will generate odd or even
    # number [1,100] with equal probability. If rand()
    # generates odd number, the function will
    # return 1 else it will return 0
    tmp = random.randint(1, 100)
    return tmp % 2


# Random Function to that returns 0, 1 or 2 with
# equal probability 1 with 75%
def rand3():
    # returns 0, 1, 2 or 3 with 25% probability
    r = 2 * rand2() + rand2()
    if r < 3:
        return r
    return rand3()


# Driver code to test above functions
if __name__ == '__main__':
    for i in range(100):
        print(rand3(), end="")
