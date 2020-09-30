import tools


class Cipher:
    def __init__(self):
        self.left_part = self.right_part = None

    def __text_to_bin(self, text):
        bin_text = bin(ord(text))[2:]
        return ['0'] * (8 - len(bin_text)) + list(bin_text)

    def __ip(self, input_sequence):
        schema = [2, 6, 3, 1, 4, 8, 5, 7]
        return [input_sequence[item - 1] for item in schema]

    def ep(self, input_sequence):
        self.left_part, self.right_part = tools.division_into_two_parts(input_sequence)
        schema = [4, 1, 2, 3, 2, 3, 4, 1]
        return [self.right_part[item - 1] for item in schema]

    def __solve_matrix(self, input_sequence):
        left_part, right_part = tools.division_into_two_parts(input_sequence)
        left_row, left_col = self.__find_coordinates(left_part)
        right_row, right_col = self.__find_coordinates(right_part)
        return list(self.__take_sequence_from_table(tools.LEFT_TABLE, left_row, left_col) +
                    self.__take_sequence_from_table(tools.RIGHT_TABLE, right_row, right_col))

    def __find_coordinates(self, sequence):
        return (int(sequence[0] + sequence[-1], 2),
                int(sequence[1] + sequence[2], 2))

    def __take_sequence_from_table(self, table, row, col):
        return table[row][col]

    def __p4(self, sequence):
        schema = [2, 4, 3, 1]
        return [sequence[item - 1] for item in schema]

    def __reversed_ip(self, sequence):
        schema = [4, 1, 3, 5, 7, 2, 8, 6]
        return [sequence[item - 1] for item in schema]

    def loop(self, plain_text, key):
        ep_text = self.ep(plain_text)
        print('After EP: ', ep_text)

        text_after_xor = tools.xor(ep_text, key)
        print('After xor: ', text_after_xor)

        res_seq_after_matrix = self.__solve_matrix(text_after_xor)
        print('After tables: ', res_seq_after_matrix)

        text_after_p4 = self.__p4(res_seq_after_matrix)
        print('After p4: ', text_after_p4)

        xor_l_and_p4 = tools.xor(self.left_part, text_after_p4)
        print('After XOR L and P4: ', xor_l_and_p4)
        return xor_l_and_p4

    def encrypt_text(self, plain_text, k1, k2):
        plain_text = self.__text_to_bin(plain_text)
        print('Plain text: ', plain_text)

        plain_text = self.__ip(plain_text)
        print('After IP:', plain_text)

        xor_l_and_p4 = self.loop(plain_text, k1)

        sw = self.right_part + xor_l_and_p4
        print('SW: ', sw)

        xor_l_and_p4 = self.loop(sw, k2)

        res_seq = xor_l_and_p4 + self.right_part
        print('Res: ', res_seq)

        res_seq = self.__reversed_ip(res_seq)
        print('Result: ', res_seq)
