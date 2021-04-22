# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.
num = int(input('Digite um número inteiro: '))
calc = num % 2
if calc == 1:
    print('O número é impar.')
else:
    print('O número é par.')