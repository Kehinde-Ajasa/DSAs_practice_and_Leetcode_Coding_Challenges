"""This code solves the challenge of selecting the indices of two numbers that
adds up to a particular target."""
target = int(input("What is the target: "))


def get_input():
    """Subroutine to accept all user's Input."""
    numbers = input("Enter all the values in the array, \
separated with a ',' : ")
    numbers_array = numbers.split(',')
    return numbers_array


def two_sum(subtractor, array_of_numbers):
    """Main codebase for two sum challenge"""
    for any_number in array_of_numbers:
        if subtractor - int(any_number) in array_of_numbers:
            return \
                [array_of_numbers.index(any_number), array_of_numbers.index(subtractor - int(any_number))]
        else:
            return f"No two numbers in the array can add up to {subtractor}"


print(two_sum(target, get_input()))
