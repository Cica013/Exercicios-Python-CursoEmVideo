# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo.
print('-='*20)
print('Analisador de triângulos.')
print('-='*20)
r1 = int(input('Digite aqui o valor de r1: '))
r2 = int(input('Digite aqui o valor de r2: '))
r3 = int(input('Digite aqui o valor de r3: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('As retas PODEM formar um triângulo.')
else:
    print('As retas NÃO PODEM formar um triângulo.')
