def liczba_szesnastkowa(number):
    if number < 0:
        return "Liczba musi być dodatnia"
    elif number == 0:
        return "0"

    hexadecimal_digits = "0123456789ABCDEF"
    result = ""
    
    while number > 0:
        remainder = number % 16
        result = hexadecimal_digits[remainder] + result
        number = number // 16

    return result

def test_positive_integer():
    assert liczba_szesnastkowa(10) == "A"

def test_zero():
    assert liczba_szesnastkowa(0) == "0"

def test_negative_integer():
    assert liczba_szesnastkowa(-5) == "Liczba musi być dodatnia"

def test_large_integer():
    assert liczba_szesnastkowa(255) == "FF"
