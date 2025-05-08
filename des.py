from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'8bytekey'  # Key must be exactly 8 bytes for DES
data = b'HelloDES'  # Data must be a multiple of 8 bytes

# Encrypt
cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(pad(data, 8))
print("Encrypted:", ciphertext)

# Decrypt
decipher = DES.new(key, DES.MODE_ECB)
plaintext = unpad(decipher.decrypt(ciphertext), 8)
print("Decrypted:", plaintext)
