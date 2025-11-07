stopnie = ("Szeregowy", "Kapral", "Sierżant", "Porucznik", "Kapitan", "Major", "Pułkownik")

ilość_stopni = len(stopnie)
print(f"Ilość stopni wojskowych: {ilość_stopni}")

major_index = stopnie.index("Major")
print(f"Indeks elementu 'Major': {major_index}")

pułkownik_występowanie = "Pułkownik" in stopnie
print(f"Czy 'Pułkownik' występuje w krotce: {pułkownik_występowanie}")