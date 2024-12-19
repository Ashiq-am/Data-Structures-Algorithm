# Python3 program to find all possible points
# of a parallelogram

ax = 5
ay = 0 #coordinates of A
bx = 1
by = 1 #coordinates of B
cx = 2
cy = 5 #coordinates of C
print(ax + bx - cx, ", ", ay + by - cy)
print(ax + cx - bx, ", ", ay + cy - by)
print(cx + bx - ax, ", ", cy + by - ax)
