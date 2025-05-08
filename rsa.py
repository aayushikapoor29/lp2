def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_e(phi):
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            return e

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d

def encrypt(msg, e, n):
    return [((ord(c) - ord('A')) ** e) % n for c in msg]

def decrypt(cipher, d, n):
    return ''.join([chr((c ** d) % n + ord('A')) for c in cipher])

# Small primes for demo (not secure)
p, q = 5, 11
n = p * q         # 55
phi = (p-1)*(q-1) # 40

e = find_e(phi)
d = mod_inverse(e, phi)

message = "aayushi kapoor"  # Uppercase letters only
cipher = encrypt(message, e, n)
decrypted = decrypt(cipher, d, n)

print("Original  :", message)
print("Encrypted :", cipher)
print("Decrypted :", decrypted)
