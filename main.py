# 105064506 鄭柏偉 HW3
# Rabin Public-Key Cryptosystem

import prime
import Rabin


def delete_space(string):
    lst = string.split(' ')
    output = ''
    for i in lst:
        output += i
    return output


def add_space(string):
    string = string[::-1]
    string = ' '.join(string[i:i + 8] for i in range(0, len(string), 8))
    return string[::-1]


# main()
if __name__ == '__main__':

    # 256-bit prime number generation
    print('<Miller-Rabin>')
    print(format(prime.generate_a_prime_number(256), 'x'))

    ###########################################################
    # Encryption
    print('\n<Rabin Encryption>')

    # p and q has 128 bits
    p = int(delete_space(input('p = ')), 16)   # p = daaefe652cad1614f17e87f2cd80973f
    q = int(delete_space(input('q = ')), 16)   # q = f99988626723eef2a54ed484dfa735c7
    n = p*q
    print('n = pq =', add_space(format(n, 'x')))

    # plaintext has 224 bits
    # Rabin encryption
    plaintext = int(delete_space(input('Plaintext = ')), 16)   # plaintext = be000badbebadbadbad00debdeadfacedeafbeefadd00addbed00bed
    ciphertext = Rabin.encryption(plaintext, n)
    print('Ciphertext =', add_space(format(ciphertext, 'x')))

    ###########################################################
    # Decryption
    print('\n<Rabin Decryption>')
    ciphertext = int(delete_space(input('Ciphertext = ')), 16)    # 0x5452361adb4c34be04a5903ae00793bc1086e887ebed06e23ffba0b4a4348cc0
    print('Private Keys :')
    p = int(delete_space(input('p = ')), 16)  # 0xd5e68b2b5855059ad1a80dd6c5dc03eb
    q = int(delete_space(input('q = ')), 16)  # 0xc96c6afc57ce0f53396d3b32049fe2d3
    plaintext = Rabin.decryption(ciphertext, p, q)
    print('Plaintext =', add_space(format(plaintext, 'x').zfill(226 // 4)))
