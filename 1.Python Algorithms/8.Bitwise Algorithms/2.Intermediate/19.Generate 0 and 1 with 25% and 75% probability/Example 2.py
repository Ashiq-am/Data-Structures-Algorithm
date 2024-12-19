from random import randrange

# Random Function to that returns 0 or 1 with
# equal probability
def rand50():
    return ((int)(randrange(0, 2)) & 1)


def rand75():
    return (rand50() & rand50())^1


for i in range(0, 50):
    print(rand75(), end="")
