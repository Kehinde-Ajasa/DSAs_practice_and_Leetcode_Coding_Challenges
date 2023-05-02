from number_to_roman_numerals import standards


def test_roman_standards():
    assert standards(1) == "I"
    assert standards(5) == "V"
    assert standards(10) == "X"
    assert standards(50) == "L"
    assert standards(100) == "C"
    assert standards(500) == "D"
    assert standards(1000) == "M"
