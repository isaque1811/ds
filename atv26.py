p1=float(input('digite o preço de um produto'))
p2=float(input('digite o preço do segundo produto'))
p3=float(input('digite o preço de outro produto'))
if p1<p2 and p3:
    print('compre esse produto de {}'.format(p1))
elif p2<p1 and p3:
    print('compre esse produto de {}'.format(p2))
else:
    print('compre o produto que custa {p3}')