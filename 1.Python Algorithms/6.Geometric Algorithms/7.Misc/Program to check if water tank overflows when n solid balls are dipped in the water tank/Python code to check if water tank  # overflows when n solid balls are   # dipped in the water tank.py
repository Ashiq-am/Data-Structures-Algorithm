# Python code to check if water tank
# overflows when n solid balls are
# dipped in the water tank

# function to find if tak will
# overflow or not
def overflow(H, r, h, N, R):
    # cylinder capacity
    tank_cap = 3.14 * r * r * H

    # volume of water in tank
    water_vol = 3.14 * r * r * h

    # volume of n balls
    balls_vol = N * (4 / 3) * 3.14 * R * R * R

    # total volume of water
    # and n dipped balls
    vol = water_vol + balls_vol

    # condition to check if tank is in
    # overflow state or not
    if vol > tank_cap:
        print("Overflow")
    else:
        print("Not in overflow state")

    # Driver code


# giving dimensions
H = 10
r = 5
h = 5
N = 2
R = 2

# calling function
overflow(H, r, h, N, R)

# This code is contributed by "Sharad_Bhardwaj".
