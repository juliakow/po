num = input("Podaj liczbę całkowitą dodatnią: ")
if num.isdigit():
    num = int(num)
    if num >= 0:
        hex_num = hex(num)[2:].upper()
        print(hex_num)
    else:
        print("Błąd: Podana liczba musi być dodatnia.")
else:
    print("Błąd: Podana wartość nie jest liczbą całkowitą.")
