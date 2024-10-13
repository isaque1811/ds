metros = float( input("Digite quantos metros quadrados você vai pintar: "))
latas = metros / 54
preco = latas * 80
print("Você precisa comprar {} lata(s), custando R${}".format(latas,preco))