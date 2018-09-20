# RSA Example in Python

This is an example of how to calculate RSA key pairs. It's intended for educational purposes and is NOT for use in Real Code.

## Dependencies

[gmpy](https://pypi.org/project/gmpy/) - General MultiPrecision arithmetic for Python.

```
pip install gmpy
```

## Running

Choose two prime numbers for your 'p' & 'q':

```
python rsa.py 67 71
```

Example output:

```
Here's what's happening:

p = 67
q = 71

n = p * q
n = 67 * 71
n = 4757

x = lcm(p - 1, q - 1)
x = lcm(67 - 1, 71 - 1)
x = lcm(66, 70)
x = 2310

e = number coprime and less than n, this script randomly chooses for you.
e = 23

d * e mod x = 1
d * 23 mod 2310 = 1
d = 1607

Now we use these for our keys:
Public Key  = (n, e) = (4757, 23)
Private Key = (n, d) = (4757, 1607)

And we can encrypt and decrypt a simple message
message:   123

encrypted = (message**e) % n
encrypted = (123**23) % 4757
encrypted = 418

decrypted = (encrypted**d) % n
decrypted = (418**1607) % 4757
decrypted = 123

🤯
```
