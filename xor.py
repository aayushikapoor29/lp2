text = "Hello World"

print("Original Text:", text)

print("\nOR with 127:")
for char in text:
    or_result = ord(char) | 127
    print(f"{char} -> {or_result}")

print("\nAND with 127:")
for char in text:
    and_result = ord(char) & 127
    print(f"{char} -> {and_result}")

print("\nXOR with 127:")
for char in text:
    xor_result = ord(char) ^ 127
    print(f"{char} -> {xor_result}")
