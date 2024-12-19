# Function to calculate Vertex,
# Focus and Directrix
def parabola(a, b, c):
    print("Vertex: (", (-b / (2 * a)),
          ", ", (((4 * a * c) - (b * b))
                 / (4 * a)), ")", sep="")

    print("Focus: (", (-b / (2 * a)),
          ", ", (((4 * a * c) - (b * b) + 1)
                 / (4 * a)), ")", sep="")

    print("Directrix: y=", c - ((b * b)
                                + 1) * 4 * a, sep="")


# Driver Function
a = 5
b = 3
c = 2
parabola(a, b, c)

# This code is contributed by Smitha.
