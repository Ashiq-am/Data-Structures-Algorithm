# Python3 program to count of acute, obtuse and right
# triangles in an array

# Find the number of acute, right, obtuse triangle
# that can be formed from given array.
def findTriangle(a, n):
    b = []
    # Finding the square of each element of array
    for i in range(n):
        b.append(a[i] * a[i])

    # Sort the sides of array and their squares.
    a.sort()
    b.sort()

    # x for acute triangles
    # y for right triangles
    # z for obtuse triangles
    x, y, z = 0, 0, 0

    for i in range(n):
        p = i + 1
        q = i + 1
        for j in range(i + 1, n):
            # Finding the farthest point p where
            # a^2 + b^2 >= c^2.
            while (p < n - 1 and b[i] + b[j] >= b[p + 1]):
                p += 1
            q = max(q, p)
            # Finding the farthest point q where
            # a + b > c.
            while (q < n - 1 and a[i] + a[j] > a[q + 1]):
                q += 1

            # If point p make right triangle.
            if (b[i] + b[j] == b[p]):
                # All triangle between j and p are acute
                # triangles. So add p - j - 1 in x.
                x += max(p - j - 1, 0)
                # Increment y by 1.
                y += 1
                # All triangle between q and p are acute
                # triangles. So add q - p in z.
                z += q - p
            # If no right triangle
            else:
                # All triangle between j and p are acute
                # triangles. So add p - j in x.
                x += max(p - j, 0)
                # All triangle between q and p are acute
                # triangles. So add q - p in z.
                z += q - p

    print("Acute Triangle:", x)
    print("Right Triangle:", y)
    print("Obtuse Triangle:", z)


# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 9, 10, 12, 15]
    n = len(arr)
    findTriangle(arr, n)

# This code is contributed by Ryuga
