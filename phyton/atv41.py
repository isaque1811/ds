n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
o = input("Digite qual operação (+, -, * ou /) deseja realizar: ")
if o == "+":
    r = n1 + n2
elif o == "-":
    r= n1 - n2
elif o == "*":
    r = n1 * n2
elif op == "/":
    r= n1 / n2
else:
    r = 0

print("\nO resultado é: ")

if (r // 1) % 2 == 0:
    print("Par")
else:
    print("Ímpar")

if r >= 0:
    print("Positivo")
else:
    print("Negativo")

if r % 1 == 0:
    print("Inteiro")
else:
    print("Decimal")