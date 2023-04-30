"""This code helps in infinitely adding the individual digits of an integer till the length of the final digit is 1
it uses the concept of recursive functions"""


def add_digits(num: int) -> int:
    string_val = str(num)
    print(string_val)
    addition = 0
    for i in string_val:
        addition += int(i)
    if len(str(addition)) != 1:
        return add_digits(addition)
    return addition
