# Python program to find Area of a Sector

def SectorArea(radius, angle):
    pi = 22 / 7

    # Constraint or Limit
    if angle >= 360:
        print("Angle not possible")
        return

    # Calculating area of the sector
    else:
        sector = (pi * radius ** 2) * (angle / 360)
        print(sector)
        return


# Driver code
radius = 9
angle = 60
SectorArea(radius, angle)
