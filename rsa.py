import math

def generate_keypair(p, q):
    n = p*q
    phi = (p-1)*(q-1)
    e = 2

    while math.gcd(e, phi) != 1: e+=1
    d = pow(e, -1, phi)
    return (e,n), (d, n)

def encrypt(msg, e, n):
    return [pow(ord(char), e, n) for char in msg]

def decrpyt(msg, d, n):
    return ''.join([chr(pow(char, d, n)) for char in msg])

p = 61
q = 53

public_key, private_key = generate_keypair(p, q)
encrypted = encrypt('aayushikapoor', public_key[0], private_key[1])
decrpyted = decrpyt(encrypted, private_key[0], public_key[1])

print(encrypted, decrpyted)
