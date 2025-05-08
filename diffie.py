# Global public parameters (should be prime and primitive root)
p = 23  # Prime number
g = 5   # Primitive root

# Alice chooses a secret key
alice_private = int(input("Enter your secret key (Alice): "))

# Bob's secret key (manually specified, no randomness)
bob_private = int(input("Enter Bob's secret key (Bob): "))

# Public keys
alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

print("\nPublic Parameters:")
print("Prime (p):", p)
print("Generator (g):", g)

print("\nPublic Keys:")
print("Alice's Public Key:", alice_public)
print("Bob's Public Key:", bob_public)

# Shared keys (should be equal)
alice_shared = pow(bob_public, alice_private, p)
bob_shared = pow(alice_public, bob_private, p)

print("\nShared Secret Key:")
print("Alice's Computed Shared Key:", alice_shared)
print("Bob's Computed Shared Key:", bob_shared)
