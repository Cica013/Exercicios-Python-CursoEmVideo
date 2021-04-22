# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite aqui o primeiro número: '))
b = int(input('Digite aqui o segundo número: '))
c = int(input('Digite aqui o terceiro número: '))
menor = a
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

maior = c
if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
print(f'O número {maior} é o maior, e o número {menor} é o menor.')