
def inverse_mod(e, x):
    """
    python for:
    d * e mod x = 1
    """
    t = 0
    newt = 1
    r = x
    newr = e
    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    if r > 1:
        return None
    if t < 0:
        t += x
    return t


p, q, e = 67, 71, 37

n = p*q
x = (p - 1)*(q - 1)
d = inverse_mod(e, x)

message = 123
encrypted = pow(message, e, n)
decrypted = pow(encrypted, d, n)  # == message

print(encrypted)
print(decrypted)