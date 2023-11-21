n = float(input("Digite quantos litros você quer abastecer: "))
m= input("Digite A para álcool ou G para gasolina: ")
b = 0
if m == "A" or m == "a":
    b = n* 1.9
    if n <= 20:
        b -= 1.9 * n * 3 / 100
    else:
        b -= 1.9 * n * 5 / 100
elif m == "G" or m == "g":
    b = n * 2.5
    if n <= 20:
        b -= 2.5 * n * 4 / 100
    else:
        b -= 2.5 * n  * 6 / 100
print("O preço a pagar é {} R$".format(b))