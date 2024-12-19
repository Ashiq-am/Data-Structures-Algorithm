# An example of tail recursive function
def print(n):
    if (n < 0):
        return

    print(" ", n)

    # The last executed statement is recursive call
    print(n - 1)
