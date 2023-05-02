"""This code is used to convert a number from an integer to a roman numeral."""


def convert_to_roman_numerals(a):
    pass

def get_to_checkpoint():
    pass


def standards(entry: int):
    """Dictionary containing integer and corresponding roman numeral value to set as standards."""
    roman_numerals_dictionary = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }
    return roman_numerals_dictionary[entry]


def move_upward_or_downward(item):
    """Determine how user's input would approach a standard, by adding or subtracting."""
    roman_numerals_dictionary = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }
