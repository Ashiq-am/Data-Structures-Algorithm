# Python3 code to check if Tank will
# overflow or not in given time

# function to calculate the volume of tank
def volume(radius, height):
    return ((22 / 7) * radius * radius * height)


# function to print overflow / filled /
# underflow accordingly
def check_and_print(required_time, given_time):
    if required_time < given_time:
        print("Overflow")
    elif required_time > given_time:
        print("Underflow")
    else:
        print("Filled")

    # driver code


radius = 5  # radius of the tank
height = 10  # height of the tank
rate_of_flow = 10  # rate of flow of water

given_time = 70.0  # time given

# calculate the required time
required_time = volume(radius, height) / rate_of_flow

# printing the result
check_and_print(required_time, given_time)

# This code is contributed by "Sharad_Bhardwaj".
