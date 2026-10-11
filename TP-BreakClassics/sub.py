#substition cipher
def substitution_cipher(text, cipher_alphabet):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                index = ord(char) - ord('a')
                result += cipher_alphabet[index].lower()
            else:
                index = ord(char) - ord('A')
                result += cipher_alphabet[index].upper()
        else:
            result += char
    return result
def substitution_decipher(text, cipher_alphabet):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                index = cipher_alphabet.lower().index(char)
                result += chr(index + ord('a'))
            else:
                index = cipher_alphabet.upper().index(char)
                result += chr(index + ord('A'))
        else:
            result += char
    return result
example_cipher_alphabet = "QMJZTGFKPWLSBOXNCRYEVHIADU"
print(substitution_cipher("KEEP THE SECRET SAFE", example_cipher_alphabet))
print(substitution_decipher("ERVYE DXVR SXFPJ", example_cipher_alphabet))