# Criem um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem
# de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
numeros = (randint(1, 20), randint(1, 30), randint(1, 10), randint(1, 25), randint(1, 22))
print(f'A listagem de números gerados é: {numeros}')
print(f'O maior valor da lista é: {max(numeros)}')
print(f'O menor valor da lista é: {min(numeros)}')
