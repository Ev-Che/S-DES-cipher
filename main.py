from tools.cipher import Cipher
from tools.key_generator import KeyGenerator
import logging


def main():
    logging.basicConfig(filename='log.log', level=logging.DEBUG,
                        filemode='w', format='%(asctime)s: %(message)s',
                        datefmt='%I:%M:%S %p')
    key_generator = KeyGenerator()
    cipher = Cipher()
    reverse = int(input(' [0] Encrypt;\n [1] Decrypt;\nChoice functionality: '))
    key = int(input('Enter the key: '))
    key_generator.key_generate(key)
    input_text = input('Enter your text: ')
    result = cipher.encrypt_text(input_text, key_generator.k1, key_generator.k2, reverse=reverse)
    print('Result: {}'.format(result))


if __name__ == '__main__':
    main()

# (\/)
# (o_o)
# c(")(")
