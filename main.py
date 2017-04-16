# 105064506 鄭柏偉 HW3
# Rabin Public-Key Cryptosystem

import prime

# main()
if __name__ == '__main__':
    # 128 bits = 16 bytes
    p = prime.generate_a_prime_number(16)
    q = prime.generate_a_prime_number(16)
    n = p * q
    print('p =', p)
    print('q =', q)
    print('n = pq =', n)
