# 105064506 鄭柏偉 HW3
# Rabin Public-Key Cryptosystem

import prime
import Rabin

# main()
if __name__ == '__main__':

    # p and q has 128 bits
    # p = prime.generate_a_prime_number(128)
    p = 0xdaaefe652cad1614f17e87f2cd80973f
    # q = prime.generate_a_prime_number(128)
    q = 0xf99988626723eef2a54ed484dfa735c7
    n = p*q

    # plaintext has 224 bits
    plaintext = 0xbe000badbebadbadbad00debdeadfacedeafbeefadd00addbed00bed

    # Rabin encryption
    ciphertext = Rabin.encryption(plaintext, n)

    # 256-bit prime number generation
    print('<Miller-Rabin>')
    print(format(prime.generate_a_prime_number(256), 'x'))
    # Show encryption information
    print('\n<Rabin Encryption>')
    print('p =', format(p, 'x'))
    print('q =', format(q, 'x'))
    print('n = pq =', format(n, 'x'))
    print('Plaintext =', format(plaintext, 'x'))
    print('Ciphertext =', format(ciphertext, 'x'))

    # Decryption
    ciphertext = 0x5452361adb4c34be04a5903ae00793bc1086e887ebed06e23ffba0b4a4348cc0
    p = 0xd5e68b2b5855059ad1a80dd6c5dc03eb
    q = 0xc96c6afc57ce0f53396d3b32049fe2d3
    plaintext = Rabin.decryption(ciphertext, n)
    print('\n<Rabin Decryption>')
    print('Ciphertext =', format(ciphertext, 'x'))
    print('p =', format(p, 'x'))
    print('q =', format(q, 'x'))
    print('Plaintext =', format(plaintext, 'x'))
