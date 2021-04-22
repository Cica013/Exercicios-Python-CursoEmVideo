from math import hypot
co = float(input('Digite aqui o valor do cateto oposto: '))
ca = float(input('Digite aqui o valor do cateto adjacente: '))
hy = hypot(ca, co)
print(f'O valor da hypotenusa é: {hy:.2f}')