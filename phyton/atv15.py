prec = float(input("Digite quanto você ganha por hora: "))
horas = float(  input("Digite quantas horas você trabalhou esse mês: "))
sa = prec * horas
IR = sa * (11 / 100)
INSS = sa * (8 / 100)
sindicato = sa * (5 / 100)
liquido = sa - IR - INSS - sindicato
print(    "+ Salário Bruto : R$ {} \n"
    "- IR (11%) : R$ {} \n"
    "- INSS (8%) : R$ {} \n"
    "- Sindicato (5%) : R$ {} \n"
    "= Salário Liquido : R$ {}".format(sa,IR,INSS,sindicato,liquido))
