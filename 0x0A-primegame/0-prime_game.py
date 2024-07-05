#!/usr/bin/python3
"""Prime Game"""


def play_game(n):
    """play_game function"""
    if n < 2:
        return 1
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [num for num, prime in enumerate(is_prime) if prime]
    turn = 0
    while primes:
        turn += 1
        primes = [prime for prime in primes if prime % primes[0] != 0]
        primes = primes[1:]
    return turn % 2


def isWinner(x, nums):
    """isWinner function"""
    maria_wins = 0
    ben_wins = 0
    
    if x > 10000:
        return None

    for i in range(x):
        n = nums[i]
        if play_game(n) == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
