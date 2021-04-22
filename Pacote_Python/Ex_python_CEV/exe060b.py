# Faça um programa que leia um número qualquer e mostre seu fatorial.
num = int(input('Digite aqui um número qualquer para calcular seu fatorial: '))
cont = num
fac = 1
while cont > 0:
    print(f'{cont} ', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fac *= cont
    cont -= 1
print(fac)
