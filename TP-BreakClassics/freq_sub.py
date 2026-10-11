# Room 1 - Frequency substitution decipher

def frequency_substitution_decipher(text):

    # keep original text for final decryption
    original_text = text

    # clean text only for frequency analysis
    clean_text = ''.join(filter(str.isalpha, text)).lower()

    # count frequency of each ciphertext letter
    frequency = {}

    for char in clean_text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # calculate percentages
    total = sum(frequency.values())

    for char in frequency:
        frequency[char] = (frequency[char] / total) * 100

    # sort ciphertext letters from most frequent to least frequent
    sorted_frequency = sorted( frequency.items(), key=lambda x: x[1], reverse=True )

    print("Ciphertext frequencies:")
    for char, freq in sorted_frequency:
        print(f"{char}: {freq:.2f}%")

    # Hint given in the TP
    plaintext_frequency_order = [
        'e',
        't',
        'r',
        's',
        'o',
        'a',
        'h',
        'n',
        'd',
        'i',
        'g',
        'l'
    ]

    # first automatic frequency-based guess
    substitution = {}

    for i in range(min(len(sorted_frequency), len(plaintext_frequency_order))):
        cipher_char = sorted_frequency[i][0]
        plain_char = plaintext_frequency_order[i]

        substitution[cipher_char] = plain_char

    print("\nInitial substitution guess:")
    print(substitution)

    # apply initial guess
    result = ""

    for char in original_text:
        if char.isalpha():
            lower_char = char.lower()

            if lower_char in substitution:
                replacement = substitution[lower_char]

                if char.isupper():
                    result += replacement.upper()
                else:
                    result += replacement
            else:
                result += char
        else:
            result += char

    print("\nInitial decrypted guess:")
    print(result)

    # Improve mapping using word patterns and context

    #EKT -> THE
    substitution['e'] = 't'
    substitution['k'] = 'h'
    substitution['t'] = 'e'
    # EKT YTJRTE BTYYQFT -> THE SECRET MESSAGE
    substitution['y'] = 's'
    substitution['j'] = 'c'
    substitution['r'] = 'r'
    substitution['b'] = 'm'
    substitution['q'] = 'a'
    substitution['f'] = 'g'
    # PY -> IS
    substitution['p'] = 'i'
    # KPZZTO -> HIDDEN
    substitution['z'] = 'd'
    substitution['o'] = 'n'
    # NQRQFRQNK -> PARAGRAPH
    substitution['n'] = 'p'
    # ZXTY -> DOES
    substitution['x'] = 'o'
    # FPHTY -> GIVES
    substitution['h'] = 'v'
    # MVE -> BUT
    substitution['m'] = 'b'
    substitution['v'] = 'u'
    #STEETR -> LETTER
    substitution['s'] = 'l'
    # GRTCVTOJD -> FREQUENCY
    substitution['c'] = 'q'
    substitution['d'] = 'y'
    #SXXL GXR JXBBXO IXRZY -> LOOK FOR COMMON WORDS
    substitution['l'] = 'k'
    substitution['g'] = 'f'
    substitution['i'] = 'w'


    # decrypt again using confirmed mappings
    result = ""

    for char in original_text:
        if char.isalpha():

            lower_char = char.lower()

            if lower_char in substitution:
                replacement = substitution[lower_char]

                if char.isupper():
                    result += replacement.upper()
                else:
                    result += replacement

            else:
                # leave unknown ciphertext letters unchanged
                result += char

        else:
            result += char

    print("\nAfter using word patterns:")
    print(result)

    return frequency, substitution


ciphertext = """
EKT YTJRTE BTYYQFT PY KPZZTO PO EKPY NQRQFRQNK.
STEETR GRTCVTOJD ZXTY OXE RTHTQS EKT IKXST LTD,
MVE PE FPHTY Q FXXZ YEQRE.
SXXL GXR JXBBXO IXRZY, RTNTQETZ NQEETROY,
QOZ YKXRE IXRZY.
IKTO DXV RTJXHTR EKT BTYYQFT,
EKT HPFTOTRT LTD KQY GXVR STEETRY.
"""

frequency_substitution_decipher(ciphertext)