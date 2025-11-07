#a.
imie = str(input("Podaj imię: "))
print(f"Witaj {imie}")

#b.
wiek = int(input("Podaj wiek: "))
print(f"Twój wiek to: {wiek}")

#c.
nazwisko = str(input("Podaj nazwisko: "))
inicjaly = imie[0].upper() + "." + nazwisko[0].upper() + "."
print(f"Inicjały: {inicjaly}")

#d.
lancuch_d = input("Podaj łańcuch tekstowy: ")
print(f"{lancuch_d} " * 5)

#e.
lancuch_e1 = input("Podaj pierwszy łańcuch: ")
lancuch_e2 = input("Podaj drugi łańcuch: ")
polaczone_lancuchy = lancuch_e1 + lancuch_e2
print(f"Połączone łańcuchy: {polaczone_lancuchy}")

#f.
lancuch_d1 = input("Podaj pierwszy łańcuch: ")
lancuch_d2 = input("Podaj drugi łańcuch:")
polowa1 = lancuch_d1[:len(lancuch_d1)//2]
polowa2 = lancuch_d2[len(lancuch_d2)//2:]
lancuch_d3 = polowa1 + polowa2
print(f"Pierwsza połowa pierwszego łańcucha połączona z drugą drugiego: {lancuch_d3}")