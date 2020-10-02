import logging
from tools import tools


class Cipher:
    """Класс, выполняющий шифрование по алгоритму S-DES."""

    def __init__(self):
        self.plain_text = None
        self.left_part = self.right_part = None

    def __text_to_bin(self, text):
        """Перевод буквы 8-битный двоичный код."""
        bin_text = bin(ord(text))[2:]
        self.plain_text = ['0'] * (8 - len(bin_text)) + list(bin_text)
        logging.info('Text to bin: {}'.format(tools.format_to_str(self.plain_text)))

    def __bin_to_text(self):
        logging.info('Bin to text: {}'.format(int(''.join(self.plain_text), 2)))
        return chr(int(''.join(self.plain_text), 2))

    def __ip(self):
        schema = [2, 6, 3, 1, 4, 8, 5, 7]
        self.plain_text = [self.plain_text[item - 1] for item in schema]

    def __divide_into_two_parts(self):
        """Разделение последовательности на правую и левую части."""
        self.left_part, self.right_part = tools.division_into_two_parts(self.plain_text)

    def __ep(self):
        self.__divide_into_two_parts()
        schema = [4, 1, 2, 3, 2, 3, 4, 1]
        self.plain_text = [self.right_part[item - 1] for item in schema]

    def __solve_matrix(self):
        """Нахождение выходной последовательности после применения S-матриц."""
        left_part, right_part = tools.division_into_two_parts(self.plain_text)
        left_row, left_col = tools.find_coordinates(left_part)
        right_row, right_col = tools.find_coordinates(right_part)
        self.plain_text = list(tools.take_sequence_from_table(tools.LEFT_TABLE,
                                                              left_row, left_col) +
                               tools.take_sequence_from_table(tools.RIGHT_TABLE,
                                                              right_row, right_col))

    def __p4(self):
        schema = [2, 4, 3, 1]
        self.plain_text = [self.plain_text[item - 1] for item in schema]

    def __reversed_ip(self):
        """Перестановка IP(-1)."""
        schema = [4, 1, 3, 5, 7, 2, 8, 6]
        self.plain_text = [self.plain_text[item - 1] for item in schema]

    def loop(self, key):
        """Отображение F."""
        self.__ep()
        logging.info('After EP: {}'.format(tools.format_to_str(self.plain_text)))
        self.plain_text = tools.xor(self.plain_text, key)
        logging.info('After XOR(E/P, key): {}'.format(tools.format_to_str(self.plain_text)))
        self.__solve_matrix()
        logging.info('After tables: {}'.format(tools.format_to_str(self.plain_text)))
        self.__p4()
        logging.info('After p4: {}'.format(tools.format_to_str(self.plain_text)))
        self.plain_text = tools.xor(self.left_part, self.plain_text)
        logging.info('After XOR(L, P4): {}'.format(tools.format_to_str(self.plain_text)))

    def encrypt_text(self, input_text, k1, k2, reverse=False):
        """Алгоритм шифрования."""
        self.__text_to_bin(input_text)
        logging.info('Plain text: {}'.format(tools.format_to_str(self.plain_text)))
        self.__ip()
        logging.info('After IP: {}'.format(tools.format_to_str(self.plain_text)))
        self.loop(k1) if not reverse else self.loop(k2)
        self.plain_text = self.right_part + self.plain_text
        logging.info('SW: {}'.format(tools.format_to_str(self.plain_text)))
        self.loop(k2) if not reverse else self.loop(k1)
        self.plain_text = self.plain_text + self.right_part
        logging.info('After second loop: {}'.format(tools.format_to_str(self.plain_text)))
        self.__reversed_ip()
        logging.info('Result: {}'.format(self.__bin_to_text()))
        return self.__bin_to_text()
