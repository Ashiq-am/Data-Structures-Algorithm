# function to count the number of bits in a number n
def count_bits(n):
    # bin(n) returns a binary string representation of n preceded by '0b' in python
    binary = bin(n)

    # we did -2 from length of binary string to ignore '0b'
    return len(binary) - 2

a = 65
b = 183

print(f"Total bits in {a}: {count_bits(a)}")
print(f"Total bits in {b}: {count_bits(b)}")

# This code is contributed by udit
