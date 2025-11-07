moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
lista_2 = [34, 76, 9]
print(f"Lista przed zmianami: {moja_lista}")

moja_lista.append(25) #dodanie elementu na koniec listy
print(moja_lista)

moja_lista.insert(3, 11) #dodanie elementu na podanym indeksie
print(moja_lista)

moja_lista.extend(lista_2) #dodaje do listy elementy z podanej innej listy
print(moja_lista)

moja_lista.remove(3) #usunięcie pierwszego znalezionego elementu o podanej wartości
print(moja_lista)
 
print(moja_lista.pop(5)) #zwraca i usuwa element z podanego indeksu

print(moja_lista[0]) #zwraca pierwszy element listy

print(moja_lista[-1]) #zwraca ostatni element listy

print(moja_lista[8]) #zwraca element o podanym indeksie

print(len(moja_lista)) #zwraca długość listy, czyli ilość jej elementów

print(min(moja_lista)) #zwraca najmniejszą wartość z listy

print(max(moja_lista)) #zwraca największą wartość z listy

print(sum(moja_lista)) #zwraca sumę elementów listy

lista_3 = moja_lista * 2 #dwukrotne powtórzenie wszystkich elemenów z moja_lista
print(lista_3)

print(moja_lista[:3]) #zwraca elementy listy od początku do elementu o indeksie 3

print(moja_lista[3:]) #zwraca elementy listy od elementu o indeksie 3 do końca

print(moja_lista[::-1]) #zwraca listę w odwróconej kolejności

print(moja_lista[0:9:2]) #zwraca podlistę zawierającą elementy z listy od start do stop co step

moja_lista.sort() #sortuje listę
print(moja_lista)

moja_lista.reverse() #odwraca kolejność elementów listy
print(moja_lista)

moja_lista.clear() #usuwa wszystkie elementy z listy
print(moja_lista)