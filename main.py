from tools.cipher import Cipher
from tools.key_generator import KeyGenerator
import logging


def main():
    logging.basicConfig(filename='log.log', level=logging.DEBUG,
                        filemode='w', format='%(asctime)s: %(message)s',
                        datefmt='%I:%M:%S %p')
    key_generator = KeyGenerator()
    cipher = Cipher()
    cipher_text = []
    reverse = int(input(' [0] Encrypt;\n [1] Decrypt;\nChoice functionality: '))
    key = int(input('Enter the key: '))
    key_generator.key_generate(key)
    input_text = input('Enter your text: ')
    letter_sequence = list(input_text)

    while letter_sequence:
        letter = letter_sequence.pop(0)
        cipher_text.append(cipher.encrypt_text(letter,
                                               key_generator.k1,
                                               key_generator.k2,
                                               reverse=reverse))

    print('Result: {}'.format(''.join(cipher_text)))


if __name__ == '__main__':
    main()

# (\/)
# (o_o)
# c(")(")
