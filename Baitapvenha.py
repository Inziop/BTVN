def encrypt_z26(plaintext, k):
    result = ""
    for ch in plaintext:
        if ch.isalpha():  # mã hóa chữ cái
            base = ord('A') if ch.isupper() else ord('a')
            p = ord(ch) - base
            c = (p + k) % 26
            result += chr(c + base)
        else:
            result += ch  
    return result

# Plaintext và khóa
P = "Nguyen Minh Hoang"
k = 26
C = encrypt_z26(P, k)

print("Plaintext :", P)
print("Key k     :", k)
print("Ciphertext:", C)
