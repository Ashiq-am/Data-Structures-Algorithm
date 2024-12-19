def get_left_most_set_bit(n):
    left_most_set_bit_indx = 0

    while n > 0:
        left_most_set_bit_indx += 1
        n >>= 1

    return left_most_set_bit_indx


def total_set_bits_from_1_to_n(n):
    left_most_set_bit_indx = get_left_most_set_bit(n)
    total_rep = 0
    mod = 0
    nearest_pow = 0
    total_set_bit_count = 0
    add_remaining = 0
    curr = 0  # denotes the number of set bits at index i

    for i in range(1, left_most_set_bit_indx + 1):
        nearest_pow = pow(2, i)
        if nearest_pow > n:
            last_pow = pow(2, i - 1)
            mod = n % last_pow
            total_set_bit_count += mod + 1

        else:
            if i == 1 and n % 2 == 1:
                total_rep = (n + 1) / nearest_pow
                mod = nearest_pow % 2
                add_remaining = 0
            else:
                total_rep = int(n / nearest_pow)
                mod = n % nearest_pow
                add_remaining = int(mod - (nearest_pow / 2) + 1) if mod >= nearest_pow / 2 else 0

            curr = int(total_rep * (nearest_pow / 2) + add_remaining)
            total_set_bit_count += curr

    return total_set_bit_count


# Driver code
if __name__ == "__main__":
    print(total_set_bits_from_1_to_n(4))
    print(total_set_bits_from_1_to_n(17))
    print(total_set_bits_from_1_to_n(30))

# This code is contributed by tssovi.
