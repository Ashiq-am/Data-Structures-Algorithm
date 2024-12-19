''' Python program to find the n-th element of
	Newman-Conway Sequence'''

# To declare array import module array
import array


def sequence(n):
    f = array.array('i', [0, 1, 1])

    # To store values of sequence in array
    for i in range(3, n + 1):
        r = f[f[i - 1]] + f[i - f[i - 1]]
        f.append(r)

    return r


# Driver code
def main():
    n = 10
    print(sequence(n))


if __name__ == '__main__':
    main()
