# 105064506 鄭柏偉 HW3
# Rabin Public-Key Cryptosystem

import prime

# main()
if __name__ == '__main__':

    # p = prime.generate_a_prime_number(128)
    p = 0xdaaefe652cad1614f17e87f2cd80973f
    # q = prime.generate_a_prime_number(128)
    q = 0xf99988626723eef2a54ed484dfa735c7
    n = p*q
    plaintext = 0xbe000badbebadbadbad00debdeadfacedeafbeefadd00addbed00bed
    ciphertext = plaintext ** 2 % n

    # 256-bit prime number generation
    print('<Miller-Rabin>')
    print(format(prime.generate_a_prime_number(256), 'x'))
    # Encryption
    print('<Rabin Encryption>')
    print('p =', format(p, 'x'))
    print('q =', format(q, 'x'))
    print('n = pq =', format(n, 'x'))
    print('Plaintext =', format(plaintext, 'x'))
    print('Ciphertext =', format(ciphertext, 'x'))

    # Decryption
