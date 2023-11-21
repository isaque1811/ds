n1=float (input('digite o valor de a: '))
a ==0:
    print('não e uma equação do segundo grau')
else:
    a =float(input('digite o valor de b: '))
    b= float(input('digite o  valor de c: '))
    c=(b**2) - (4 *a*c)
    if c<0:
        print('delta menor que zero, não a raizes reais')
    elif c==0:
        r=(-b)/(2*a)
        print('delta é zero, a raiz é',r)
    else:
        n2= (-b-(c**(1/2)))/(2*a)
        n3=(-b-(c**(1/2)))/(2*a)
        print("delta  maior que zero, a raiz 1 é",r1,',a raiz 2 é',r2)