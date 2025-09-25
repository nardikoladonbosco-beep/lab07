a = float(input("Jep a: "))
b = float(input("Jep b: "))

print("Shuma:", round(a + b, 2))
print("Diferenca:", round(a - b, 2))
print("Produkti:", round(a * b, 2))

if b == 0:
    print("Pjesetimi: Nuk lejohet ndarja me zero")
else:
    print("Pjesetimi:", round(a / b, 2))

print("Pjesetimi_i_plote:", int(a // b) if b != 0 else "Nuk lejohet")
print("Mbetja:", round(a % b, 2) if b != 0 else "Nuk lejohet")
print("Fuqi a^2:", round(a ** 2, 2))
print("Fuqi b^3:", round(b ** 3, 2))
