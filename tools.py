LEFT_TABLE = [
    ['01', '00', '11', '10'],
    ['11', '10', '01', '00'],
    ['00', '10', '01', '11'],
    ['11', '01', '11', '01'],
]

RIGHT_TABLE = [
    ['01', '01', '10', '11'],
    ['10', '00', '01', '11'],
    ['11', '00', '01', '00'],
    ['10', '01', '00', '11'],
]


def division_into_two_parts(sequence):
    """Раазделение битовой последовательности на две части."""
    center = int(len(sequence) / 2)
    return sequence[:center], sequence[center:]


def xor(first: list, second: list):
    first = list(map(int, first))
    second = list(map(int, second))
    return [str(int((f and not s or not f and s))) for f, s in zip(first, second)]
