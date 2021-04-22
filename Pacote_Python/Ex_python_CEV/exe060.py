# Faça um programa que leia um número qualquer e mostre seu fatorial.
from math import factorial
num = int(input('Digite um número para calcular o fatorial: '))
fac = factorial(num)
print(f'O factorial de {num} é: {fac}')
