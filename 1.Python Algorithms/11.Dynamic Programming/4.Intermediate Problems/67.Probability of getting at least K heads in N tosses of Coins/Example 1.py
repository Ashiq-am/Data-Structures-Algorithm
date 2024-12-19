# Naive approach in Python3
# to find probability of
# at least k heads

MAX = 21

fact = [0] * MAX


# Returns probability of
# getting at least k
# heads in n tosses.
def probability(k, n):
    ans = 0
    for i in range(k, n + 1):
        # Probability of getting exactly i
        # heads out of n heads
        ans += fact[n] / (fact[i] * fact[n - i])

    # Note: 1 << n = pow(2, n)
    ans = ans / (1 << n)
    return ans


def precompute():
    # Preprocess all factorial
    # only upto 19,
    # as after that it
    # will overflow
    fact[0] = 1
    fact[1] = 1

    for i in range(2, 20):
        fact[i] = fact[i - 1] * i


# Driver code
if __name__ == '__main__':
    precompute()

    # Probability of getting 2
    # head out of 3 coins
    print(probability(2, 3))

    # Probability of getting
    # 3 head out of 6 coins
    print(probability(3, 6))

    # Probability of getting
    # 12 head out of 18 coins
    print(probability(12, 18))


