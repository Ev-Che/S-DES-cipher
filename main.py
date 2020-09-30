from key_generator import KeyGenerator
from cipher import Cipher
import tools

if __name__ == '__main__':
    key_generator = KeyGenerator(412)
    key_generator.key_generate()
    print('KEYS:')
    print(key_generator.k1)
    print(key_generator.k2)

    cipher = Cipher()
    cipher.encrypt_text('a', key_generator.k1, key_generator.k2)
