# Recursive function to find the n-th
# element of sequence
def sequence(n):
    if n == 1 or n == 2:
        return 1
    else:
        return sequence(sequence(n - 1)) + sequence(n - sequence(n - 1));


# Driver code
def main():
    n = 10
    print(sequence(n))


if __name__ == '__main__':
    main()
