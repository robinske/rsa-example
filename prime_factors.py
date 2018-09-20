import argparse

# run: python prime_factors.py 39203

def find_primes(n=300):
    """
    find all prime numbers under 300
    https://howchoo.com/g/ztk0mzq0mdy/generate-a-list-of-primes-numbers-in-python
    """
    noprimes = set(j for i in range(2, 8) for j in range(i*2, 300, i))
    primes = [x for x in range(2, 300) if x not in noprimes]
    return primes


def find_factors(primes, target):
    factors = None

    for prime in primes:
        remainder = target % prime
        if remainder == 0:
            factors = (prime, int(target / prime))
            break

    if factors is None:
        print("No prime factors found!")
    else:
        print("Prime factors of {} are {} and {}".format(
            target, factors[0], factors[1]))


parser = argparse.ArgumentParser(
    description='Find the prime factors for a number.')
parser.add_argument('target', type=int,
                    help='the target number')

args = parser.parse_args()

primes = find_primes()
target = args.target
find_factors(primes, target)
