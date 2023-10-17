num1 = float(input("Digite o tamanho do arquivo em MB: "))
num2 = float(input("Digite a velocidade da conexão em Mbps: "))
num3 = num1 / num2
num4 = num3 / 60
print("{} Minutos e {} Segundos".format(num4,num3))