imiona = ["Ala", "Ewa", "Kuba", "Oliwia"]

#a.
print(sorted(imiona))

#b.
imiona.append("Magdalena")
imiona.append("Nikodem")
print(imiona)
print(imiona.pop())

#c.
imiona.insert(3, "Jan")
print(imiona)

#d.
imiona.reverse() #odwrócona kolejność elementów listy
print(imiona)
print(imiona * 2) #zdublowana lista