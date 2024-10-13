s1 = float(input("Digite o seu salário  "))
if s1 <= 280:
    n1= 20
elif s1 <= 750:
    n1 = 15
elif s1 <= 1500:
    n1= 10
else:
    n1 = 5

diferença = s1 * (aumento/100)
n2= s1+s1
print("Seu salário antes era de R$",{s1})
print("Seu salário aumentol em ",{n1},"%")
print("Seu salário aumentol em R$",{s2})
print("Seu salário  é de R$",{n2})