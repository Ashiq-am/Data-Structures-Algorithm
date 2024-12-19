def isPossible(index, sum):
    # Base case
    if (index == n):

        # check if sum is divisible by M
        if ((sum % M) == 0):
            return True;
        return False;

    # recursively call by considering '+'
    # or '-' between index and index+1

    # 1.Try placing '+'
    placeAdd = isPossible(index + 1, sum + arr[index]);

    # 2. Try placing '-'
    placeMinus = isPossible(index + 1, sum - arr[index]);

    if (placeAdd or placeMinus):
        return True;

    return False
