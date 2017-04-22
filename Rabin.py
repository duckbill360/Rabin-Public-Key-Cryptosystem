# Rabin.py
import prime

# encryption function
# plaintext is a 224-bit number
def encryption(plaintext, n):
    # c = m^2 mod n
    plaintext = padding(plaintext)
    return plaintext ** 2 % n


# padding 16 bits to the end of a number
def padding(plaintext):
    binary_str = bin(plaintext)     # convert to a bit string
    output = binary_str + binary_str[-16:]      # pad the last 16 bits to the end
    return int(output, 2)       # convert back to integer


# encryption function
def decryption(ciphertext, n):
    plaintext = 0
    # find sqrt

    return plaintext
