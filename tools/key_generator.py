from tools import tools

GEN_SCHEMA_8 = [6, 3, 7, 4, 8, 5, 10, 9]
GEN_SCHEMA_10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]

BIT_ORDER = 10


class KeyGenerator:
    """Class that allows calculating key for encrypting"""

    def __init__(self, input_key):
        self.bit_key = self.bit_key_compile(input_key)
        self.k1 = None
        self.k2 = None

    @staticmethod
    def bit_key_compile(input_key: int) -> list:
        """This function creates 10-bit sequence from user key"""
        bin_key = list(bin(input_key))[2:]
        return ['0'] * (BIT_ORDER - len(bin_key)) + bin_key

    @staticmethod
    def replacement_elements(gen_schema: list, bit_key: list) -> list:
        """This function replacements order according to the schema"""
        return [bit_key[item - 1] for item in gen_schema]

    def __cyclic_left_shift(self, times: int) -> None:
        """This function shifts elements with times period and concatenates left and right part in one"""
        left_part, right_part = tools.division_into_two_parts(self.bit_key)
        self.bit_key = tools.left_shift(left_part, times=times) + tools.left_shift(right_part, times=times)

    def key_generate(self):
        self.bit_key = self.replacement_elements(GEN_SCHEMA_10, self.bit_key)

        self.__cyclic_left_shift(times=1)

        self.k1 = self.replacement_elements(GEN_SCHEMA_8, self.bit_key)

        self.__cyclic_left_shift(times=2)

        self.k2 = self.replacement_elements(GEN_SCHEMA_8, self.bit_key)
