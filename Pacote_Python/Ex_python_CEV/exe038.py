# Escreva um programa que leia dois números inteiros e compare-os
n1 = int(input('Digite aqui o valor de n1: '))
n2 = int(input('Digite aqui o valor de n2: '))
maior = 'O primeiro valor é maior.'
if n2 > n1:
    maior = 'O segundo valor é maior.'
elif n1 == n2:
    maior = 'Ambos os valores são iguais.'
print(maior)