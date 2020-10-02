from tools import tools
import logging


class KeyGenerator:
    """Класс для вычисления ключей шифрования."""

    def __init__(self):
        self.bit_key = None
        self.k1 = self.k2 = None

    def __bit_key_compile(self, input_key):
        """Формирование 10-битной двоичной последовательности из входного ключа."""
        bin_key = list(bin(input_key))[2:]
        self.bit_key = ['0'] * (10 - len(bin_key)) + bin_key

    def __p_10(self):
        schema = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        self.bit_key = [self.bit_key[item - 1] for item in schema]

    def __cyclic_left_shift(self, times=1):
        """Циклический сдвиг на times позиций влево и соединение левой и провой частей."""
        left_part, right_part = tools.division_into_two_parts(self.bit_key)
        self.bit_key = (tools.left_shift(left_part, times=times) +
                        tools.left_shift(right_part, times=times))

    def __p_8(self):
        schema = [6, 3, 7, 4, 8, 5, 10, 9]
        return [self.bit_key[item - 1] for item in schema]

    def key_generate(self, input_key):
        """Генерация ключей."""
        self.__bit_key_compile(input_key)
        self.__p_10()
        self.__cyclic_left_shift()
        self.k1 = self.__p_8()
        self.__cyclic_left_shift(times=2)
        self.k2 = self.__p_8()
        logging.info('KEYS:\n\tK1 = {k1}\n\tK2 = {k2}'.format(k1=tools.format_to_str(self.k1),
                                                              k2=tools.format_to_str(self.k2)))
