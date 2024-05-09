import math
alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5',
            '6', '7', '8', '9', '.']

def is_coprime(a, b):
    if math.gcd(a, b) == 1:
        return True
    else:
        return False

def is_prime_two_digit(number):
    for i in range(10,int(math.sqrt(number)+1)):
        if number % i == 0:
            return False
    return True
def decrypt(cipher_text, m):
    message = list(cipher_text)
    a_good = []
    for a in range(10,100):
        if is_prime_two_digit(a):
            if is_coprime(a,m):
                a_good.append(a)
    a_good_inv = list([pow(a,-1,m) for a in a_good])
    encrypted_text = ''
    for a_inv in a_good_inv:
        for j in [2,4,6,8]:
            for i in range(len(message)):
                if message[i] in alphabet:
                    new_id = (a_inv * (alphabet.index(message[i]) - j)) % m
                    encrypted_text = encrypted_text + alphabet[new_id]
            print(encrypted_text + f" j = {j} | a_inv = {a_inv}"+"\n" )
            encrypted_text = ' '


decrypt(".6ehq8.h2jv2mph8fh2j2 mw02h0wqw18 hp6h2js3h6fhp72hp20phwfhq8.", 38)

