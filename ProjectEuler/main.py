import math as mt

# getting factors of number
def get_factors(number):
    factors = []
    for potentialFactor in range(1, int(mt.sqrt(number))+1):
        if number % potentialFactor == 0:
            factors.append(potentialFactor)
            factors.append(number/potentialFactor)
    return factors

# determine if a number is prime
def is_prime(number, factors):
    isprime = False
    if len(factors) == 2:
        isprime = True
        return isprime


# find the highest number out of those primes
def highest_prime_factor(large_number):
    for i in get_factors(large_number):
        if is_prime(i, get_factors(i)):
            highest_factor = i
    print(highest_factor)

highest_prime_factor(600851475143)
