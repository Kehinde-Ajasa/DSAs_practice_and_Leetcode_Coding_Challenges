from challenge_258 import add_digits




def test_add_digits():
    """testing the return value of the function add_digit()"""
    for i in range(1, 100):
        assert len(str(add_digits(i))) == 1
