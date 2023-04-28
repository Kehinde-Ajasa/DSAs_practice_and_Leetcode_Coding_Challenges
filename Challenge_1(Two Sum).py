"""This code solves the challenge of selecting the indices of two numbers that
adds up to a particular target."""
"""Algorithm pattern: Create a variable V to hold the difference between individual items and the target
create a dynamic empty dictionary and allow individual items be the key and the index as the value
if V appears in the dictionary, return, loop value for V and the value of the key of V that appeared"""


def get_input():
    """Subroutine to accept all user's Input."""
    numbers = input("Enter all the values in the array, \
separated with a ',' : ")
    target = int(input("Please enter the target: "))
    numbers_array = numbers.split(',')
    return [target, numbers_array]


def two_sum(array_of_numbers):
    """Main codebase for two sum challenge"""
    dictionary = {}

    for i in range(len(array_of_numbers[1])):
        difference = array_of_numbers[0] - int(array_of_numbers[1][i])
        if difference in dictionary:
            return [dictionary[difference], i]
        dictionary[int(array_of_numbers[1][i])] = i


print(two_sum(get_input()))
