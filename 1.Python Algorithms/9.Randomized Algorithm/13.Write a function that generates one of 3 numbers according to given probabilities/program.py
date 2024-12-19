import random


# This function generates 'x' with probability px/100, 'y' with
# probability py/100 and 'z' with probability pz/100:
# Assumption: px + py + pz = 100 where px, py and pz lie
# between 0 to 100
def random(x, y, z, px, py, pz):
    # Generate a number from 1 to 100
    r = random.randint(1, 100)

    # r is smaller than px with probability px/100
    if (r <= px):
        return x

    # r is greater than px and smaller than
    # or equal to px+py with probability py/100
    if (r <= (px + py)):
        return y

    # r is greater than px+py and smaller than
    # or equal to 100 with probability pz/100
    else:
        return z
