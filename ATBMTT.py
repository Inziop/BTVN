def caesar_encrypt(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        else:
            result += char
    return result

# Dữ liệu
k = 27
plaintext = "Nguyen Minh Hoang"

# Mã hóa
ciphertext = caesar_encrypt(plaintext, k)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Note: k=27 = 1 (mod 26) nen moi chu cai dich 1 vi tri")