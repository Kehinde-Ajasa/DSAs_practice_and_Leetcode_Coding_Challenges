from unittest import TestCase

from challenge_1 import two_sum


def test_two_sum():
    """Function to assert the return value of the subroutine"""
    assert two_sum([2, 3, 4], 6) == [0, 2]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([2, 7, 11, 13], 9) == [0, 1]
    assert two_sum([2, 11, 7, 15], 9) == [0, 2]
    assert two_sum([17, 9, 6, 13], 30) == [0, 3]


