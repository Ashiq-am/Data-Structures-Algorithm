# Implementation in Python 3

# Hex String variable
hex_s = '653cae8da8edb426052'

# Plain text variable
plain = ''

# variable to store the XOR
# of previous digits
x = 0

l = len(hex_s)

# Loop for loop from the end to
# the mid section of the string
for i in range(l - 1, int(l / 2) - 1, -1):
    # calculation of the plaintext digit
    y = x ^ int(hex_s[i], 16)

    # calculation of XOR chain
    x = x ^ y
    plain = hex(y)[-1] + plain

print(plain)
