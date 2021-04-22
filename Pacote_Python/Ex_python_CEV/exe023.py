# Faça um programa que leia de 0 até 9999 e mostre na tela cada um dos dígitos separados.
num = int(input('Digite aqui o número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analizando o número {num}')
print(f'A unidade é: {u}')
print(f'A dezena é: {d}')
print(f'A centena é: {c}')
print(f'O milhar é: {m}')
