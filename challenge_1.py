"""This code solves the challenge of selecting the indices of two numbers that
adds up to a particular target."""
"""Algorithm pattern: Create a variable V to hold the difference between individual items and the target
create a dynamic empty dictionary and allow individual items be the key and the index as the value
if V appears in the dictionary, return, loop value for V and the value of the key of V that appeared"""

try:

    def two_sum(array_of_numbers: list[int], target: int) -> list:
        """Function to help solve the challenge."""
        dictionary = {}
        for i in range(len(array_of_numbers)):
            difference = target - array_of_numbers[i]
            if difference in dictionary:
                return [dictionary[difference], i]
            dictionary[array_of_numbers[i]] = i


except TypeError:
    print("Dear User, Ensure you only have integers in the array and as the target")
