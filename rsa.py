import argparse
import gmpy
import random
import sys

########################################################
#####
# This is an example of how to calculate RSA key pairs.
# It's intended for educational purposes.
# It's NOT for use in Real Code.
# Thank you for coming to my Ted Talk.
#####
########################################################


def find_primes(n=200):
    """
    find all prime numbers under 200
    https://howchoo.com/g/ztk0mzq0mdy/generate-a-list-of-primes-numbers-in-python
    """
    noprimes = set(j for i in range(2, 8) for j in range(i*2, n, i))
    primes = [x for x in range(2, n) if x not in noprimes]
    return primes


def is_prime(i):
    primes = find_primes()
    return i in primes


parser = argparse.ArgumentParser()
parser.add_argument(
    'p', type=int, help="Prime number greater than 5 and less than 200. Try 53.")
parser.add_argument(
    'q', type=int, help="Prime number greater than 5 and less than 200. Try 71.")
args = parser.parse_args()

p = args.p
q = args.q

if not (p > 5 and
        p < 200 and
        q > 5 and
        q < 200 and
        is_prime(p) and
        is_prime(q)):
    print("error: p and q must be greater than 5, less than 200, and prime. Try 53 and 71.")
    sys.exit(1)


n = p*q
x = gmpy.lcm(p - 1, q - 1)

dontuse = [p, q]
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

# e must be coprime to n and less than n
e = random.choice([pr for pr in primes if pr < n and not pr in dontuse])

# modular multiplicative inverse
d = gmpy.invert(e, x)
if d == 0:
    print("No modular multiplicative inverse found for exponent {}. That's randomly chosen so run the script again or choose different p & q.".format(e))
    sys.exit(1)

message = 123

encrypted = (message**e) % n
decrypted = (encrypted**d) % n  # == message

print("Here's what's happening:\n")
print("p = {}".format(p))
print("q = {}\n".format(q))
print("n = p * q")
print("n = {} * {}".format(p, q))
print("n = {}\n".format(n))
print("x = lcm(p - 1, q - 1)")
print("x = lcm({} - 1, {} - 1)".format(p, q))
print("x = lcm({}, {})".format(p-1, q-1))
print("x = {}\n".format(x))
print("e = number coprime and less than n, this script randomly chooses for you.")
print("e = {}\n".format(e))
print("d * e mod x = 1")
print("d * {} mod {} = 1".format(e, x))
print("d = {}\n".format(d))
print("Now we use these for our keys:")
print("Public Key  = (n, e) = ({}, {})".format(n, e))
print("Private Key = (n, d) = ({}, {})\n".format(n, d))
print("And we can encrypt and decrypt a simple message")
print("message:   {}\n".format(message))
print("encrypted = (message**e) % n")
print("encrypted = ({}**{}) % {}".format(message, e, n))
print("encrypted = {}\n".format(encrypted))
print("decrypted = (encrypted**d) % n")
print("decrypted = ({}**{}) % {}".format(encrypted, d, n))
print("decrypted = {}\n".format(decrypted))
print("🤯")
