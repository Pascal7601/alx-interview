#!/usr/bin/python3
"""
handle prime game
"""


def sieve_of_eratosthenes(limit):
    """ Helper function to generate prime numbers up to a given limit using the Sieve of Eratosthenes. """
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False  # 0 and 1 are not primes

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False

    return primes

def isWinner(x, nums):
    """ Function to determine who wins the most rounds. """
    if x <= 0 or not nums:
        return None

    # Step 1: Precompute prime numbers up to the maximum possible value of n in nums
    max_n = max(nums) if nums else 0
    primes = sieve_of_eratosthenes(max_n)

    # Step 2: Track wins for both players
    maria_wins = 0
    ben_wins = 0

    # Step 3: Simulate each round
    for n in nums:
        # Count how many prime numbers exist between 1 and n
        prime_count = sum(primes[2:n+1])

        # If prime_count is odd, Maria wins (since she goes first); if even, Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example test case
if __name__ == "__main__":
    print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))  # Expected output: Ben

