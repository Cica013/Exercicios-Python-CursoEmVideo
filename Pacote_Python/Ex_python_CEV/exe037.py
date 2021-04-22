# Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversão:
# 1- Para binário. 2- para octa 3- Para hexadecimal
num = int(input('Digite aqui um número: '))
opção = int(input('Agora digite. (1) Para conversão binária. (2) Para conversão octadecimal. (3) Para Hexadecimal: '))
conversão = 0
if opção == 1:
    conversão = bin(num)
elif opção == 2:
    conversão = oct(num)
elif opção == 3:
    conversão = hex(num)
else:
    print('Digite um número de 1 à 3.')
print(conversão[2:])
