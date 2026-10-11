def frequency_analysis(ciphertext):
    frequency = {}
    total = 0

    for char in ciphertext:
        if char.isalpha():
            char = char.lower()
            frequency[char] = frequency.get(char, 0) + 1
            total += 1

    for char in frequency:
        frequency[char] = (frequency[char] / total) * 100

    sorted_frequency = sorted(
        frequency.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("Ciphertext frequencies:")

    for char, freq in sorted_frequency:
        print(f"{char}: {freq:.2f}%")

    return sorted_frequency


def vigenere_extract_key(ciphertext, key_length):

    # Remove spaces, punctuation and newlines first
    clean_ciphertext = ''.join(
        char.lower()
        for char in ciphertext
        if char.isalpha()
    )

    # Split into groups
    groups = ['' for _ in range(key_length)]

    for i, char in enumerate(clean_ciphertext):
        groups[i % key_length] += char

    # Frequency analysis
    for i, group in enumerate(groups):
        print(f"\nGroup {i + 1}:")
        frequency_analysis(group)

    # Assume most frequent plaintext letter is E
    key = ""

    for group in groups:

        most_frequent = max(group, key=group.count)

        # both are lowercase now
        shift = (ord(most_frequent) - ord('e')) % 26

        key += chr(shift + ord('a'))

    print(f"\nGuessed key: {key.upper()}")

    return key


def vigenere_decrypt(ciphertext, key_length):

    decrypted_text = ""

    key = vigenere_extract_key(ciphertext, key_length)

    key_index = 0

    for char in ciphertext:

        if char.isalpha():

            shift = ord(key[key_index % key_length]) - ord('a')

            if char.islower():

                decrypted_char = chr(
                    (ord(char) - ord('a') - shift) % 26
                    + ord('a')
                )

            else:

                decrypted_char = chr(
                    (ord(char) - ord('A') - shift) % 26
                    + ord('A')
                )

            decrypted_text += decrypted_char

            key_index += 1

        else:
            decrypted_text += char

    return decrypted_text


ciphertext = """VVHWGQUIVYHIRSUPGTWXJSVIPCWIUPHGCIVIVVHPGHWITSDTRSDVUSYITMZL
GFHIXSUCVSDQOSPFGFVLQIOHEVHGMSDGJQRPWAQWGSNXJSPSUHIVGEXIPHVC
OPRPCBGYUSLXVCUIECYITHKIMSBAJSQXJSPIUGDKGPHGQAHWEZHETSQXGFWL
GOFGGGVAQFGIEZLTUS"""


print(vigenere_decrypt(ciphertext, 4))