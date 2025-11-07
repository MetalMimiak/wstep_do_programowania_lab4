zakupy = {
    "zeszyt": 2.50,
    "długopis": 1.50,
    "książka": 35.00,
    "koszulka": 40.00,
    "kalendarz": 24.50
}

print("Lista zakupów:")
for artykuł, kwota in zakupy.items():
    print(f"{artykuł}: {kwota:.2f} zł")

zakupy_kwota = sum(zakupy.values())
print(f"\nWydatki za zakupy: {zakupy_kwota:.2f} zł")