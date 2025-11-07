zdanie = input("Napisz zdanie: ")
litery = ''.join([litera.lower() for litera in zdanie if litera.isalpha()])
litery_sort = ''.join(sorted(litery))
print(f"Litery ze zdania w kolejności alfabetycznej {litery_sort}")
alfabet = set("aąbcćdeęfghijklłmnoópqrsśtuvwxyzźż")
litery_zdania = set(litery)
litery_brak = alfabet - litery_zdania
litery_brak_sort = ''.join(sorted(litery_brak))
print(f"Litery alfabetu, których nie ma w zdaniu: {litery_brak_sort}")