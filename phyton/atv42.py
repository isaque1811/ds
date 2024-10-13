p = 0
r = input("Telefonou para a vítima? (S ou N): ")
if r.upper() == "S":
    p += 1
r = input("Esteve no local do crime? (S ou N): ")
if r.upper() == "S":
    p+= 1
r= input("Mora perto da vítima? (S ou N): ")
if r.upper() == "S":
    p += 1
r = input("Devia para a vítima? (S ou N): ")
if r.upper() == "S":
    p += 1
r= input("Já trabalhou com a vítima? (S ou N): ")
if r.upper() == "S":
    p += 1

if p< 2:
    print("Inocente")
elif p == 2:
    print("Suspeita")
elif p < 5:
    print("Cúmplice")
else:
    print("Assassino")