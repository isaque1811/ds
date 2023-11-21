n1= float(input("Digite quantos quilos de morango foram comprados: "))
n2 = float(input("Digite quantos quilos de maçã foram comprados: "))
n3 = 0

if n1 <= 5:
    n3 += n1 * 2.5
else:
    n3 += n1 * 2.2
if n2 <= 5:
    n3 += n2 * 1.8
else:
    n3 +=n2 * 1.5

if (n1 + n2) > 8 or n3 > 25:
    n3 -= n3 * 10 / 100

print("O valor a ser pago é R$ {}".format(n3))