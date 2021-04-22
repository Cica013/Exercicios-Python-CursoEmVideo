# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa
# progressão.
primeiro = int(input('Digite aqui o primeiro termo: '))
razao = int(input('Qual a razão? '))
for c in range(primeiro, 11, razao):
    print(c, end= ' -> ')
print('ACABOU')