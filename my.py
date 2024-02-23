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

def main():
    try:
        number = int(input("Podaj liczbę całkowitą dodatnią: "))
    except ValueError:
        print("To nie jest prawidłowa liczba całkowita.")
    hexadecimal_representation = liczba_szesnastkowa(number)
    print(hexadecimal_representation)

if __name__ == "__main__":
    main()
