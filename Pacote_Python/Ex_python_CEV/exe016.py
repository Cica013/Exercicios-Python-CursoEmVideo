# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.156, o número 6.156 te a sua porção inteira 6.
from math import trunc
num = float(input('Digite um número real: '))

print(f'O número digitado foi {num} e a sua porção inteira é: {trunc(num)}')