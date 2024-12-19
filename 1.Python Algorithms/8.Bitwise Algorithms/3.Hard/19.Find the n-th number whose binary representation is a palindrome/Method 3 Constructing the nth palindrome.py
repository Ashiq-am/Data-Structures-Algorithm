# Efficient Python3 program to find n-th palindrome
INT_SIZE = 32


# Construct the nth binary palindrome with the
# given group number, aux_number and operation type


def constructNthNumber(group_no, aux_num, op):
    a = [0] * INT_SIZE
    num, i = 0, 0

    # No need to insert any bit in the middle
    if op == 2:

        # Length of the final binary representation
        len_f = 2 * group_no

        # Fill first and last bit as 1
        a[len_f - 1] = a[0] = 1

        # Start filling the a[] from middle,
        # with the aux_num binary representation
        while aux_num:
            # Get the auxiliary number's ith
            # bit and fill around middle
            a[group_no + i] = a[group_no - 1 - i] = \
                aux_num & 1
            aux_num = aux_num >> 1
            i += 1

    # Insert bit 0 in the middle
    elif op == 0:

        # Length of the final binary representation
        len_f = 2 * group_no + 1

        # Fill first and last bit as 1
        a[len_f - 1] = a[0] = 1
        a[group_no] = 0

        # Start filling the a[] from middle, with
        # the aux_num binary representation
        while aux_num:
            # Get the auxiliary number's ith
            # bit and fill around middle
            a[group_no + 1 + i] = a[group_no - 1 - i] = \
                aux_num & 1
            aux_num = aux_num >> 1
            i += 1

    else:

        # Insert bit 1 in the middle

        # Length of the final binary representation
        len_f = 2 * group_no + 1

        # Fill first and last bit as 1
        a[len_f - 1] = a[0] = 1

        a[group_no] = 1

        # Start filling the a[] from middle, with
        # the aux_num binary representation
        while aux_num:
            # Get the auxiliary number's ith
            # bit and fill around middle
            a[group_no + 1 + i] = a[group_no - 1 - i] = \
                aux_num & 1
            aux_num = aux_num >> 1

            i += 1

    # Convert the number to decimal from binary
    for i in range(0, len_f):
        num += (1 << i) * a[i]
    return num


# Will return the nth binary palindrome number


def getNthNumber(n):
    group_no = 0
    count_upto_group, count_temp = 0, 1

    # Add number of elements in all the groups,
    # until the group of the nth number is found
    while count_temp < n:
        group_no += 1

        # Total number of elements until this group
        count_upto_group = count_temp
        count_temp += 3 * (1 << (group_no - 1))

    # Element's offset position in the group
    group_offset = n - count_upto_group - 1

    # Finding which bit to be placed in the
    # middle and finding the number, which we
    # will fill from the middle in both directions
    if (group_offset + 1) <= (1 << (group_no - 1)):

        op = 2  # No need to put extra bit in middle

        # We need to fill this auxiliary number
        # in binary form the middle in both directions
        aux_num = group_offset

    else:

        if (((group_offset + 1) -
             (1 << (group_no - 1))) % 2):
            op = 0  # Need to Insert 0 at middle
        else:
            op = 1  # Need to Insert 1 at middle
        aux_num = (((group_offset) -
                    (1 << (group_no - 1))) // 2)

    return constructNthNumber(group_no, aux_num, op)


# Driver code
if __name__ == "__main__":
    n = 9

    # Function Call
    print(getNthNumber(n))
