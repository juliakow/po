def liczba_szesnastkowa(number):
    if number < 0:
        return "Wprowadzona liczba nie jest dodatnia."

    liczba_w_systemie_szesnatkowym = hex(number)[2:].upper()
    return liczba_w_systemie_szesnatkowym

try:
    user_input = int(input("Podaj liczbę całkowitą dodatnią: "))
    result = liczba_szesnastkowa(user_input)
    print(result)
except ValueError:
    print("Wprowadzona wartość nie jest liczbą całkowitą.")
