def caesar_cipher(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            shift = k % 26
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result
print(caesar_cipher("crypto is fun until the professor says quiz", 4))

def caesar_decipher(text, k):
    return caesar_cipher(text, -k)

print(caesar_decipher("GWCL JMBBMZ VWB JM CAQVO BWWTA BW AWTDM BPQA", 8))

for i in range(1, 26):
    print(f"Shift {i}: {caesar_decipher('ESP VPJ TD FYVYZHY ECJ MCFEP QZCNP', i)}")