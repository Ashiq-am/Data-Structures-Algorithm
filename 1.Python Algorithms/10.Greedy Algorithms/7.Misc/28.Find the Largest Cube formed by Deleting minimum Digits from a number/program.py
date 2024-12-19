# Python3 code to implement maximum perfect
# cube formed after deleting minimum digits
import math as mt


# Returns vector of Pre Processed
# perfect cubes
def preProcess(n):
    preProcessedCubes = list()
    for i in range(1, mt.ceil(n ** (1. / 3.))):
        iThCube = i ** 3

        # convert the cube to string and
        # push into preProcessedCubes vector
        cubeString = str(iThCube)
        preProcessedCubes.append(cubeString)

    return preProcessedCubes


# Utility function for findLargestCube().
# Returns the Largest cube number that
# can be formed
def findLargestCubeUtil(num, preProcessedCubes):
    # reverse the preProcessed cubes so
    # that we have the largest cube in
    # the beginning of the vector
    preProcessedCubes = preProcessedCubes[::-1]

    totalCubes = len(preProcessedCubes)

    # iterate over all cubes
    for i in range(totalCubes):
        currCube = preProcessedCubes[i]

        digitsInCube = len(currCube)
        index = 0
        digitsInNumber = len(num)
        for j in range(digitsInNumber):

            # check if the current digit of the cube
            # matches with that of the number num
            if (num[j] == currCube[index]):
                index += 1

            if (digitsInCube == index):
                return currCube

    # if control reaches here, the its
    # not possible to form a perfect cube
    return "Not Possible"


# wrapper for findLargestCubeUtil()
def findLargestCube(n):
    # pre process perfect cubes
    preProcessedCubes = preProcess(n)

    num = str(n)

    ans = findLargestCubeUtil(num, preProcessedCubes)

    print("Largest Cube that can be formed from",
          n, "is", ans)


# Driver Code
n = 4125
findLargestCube(n)

n = 876
findLargestCube(n)
