# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# a) Quantos números foram digitados. b) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.
cont = 0
lista = []
while True:
    num = int(input('Digite um número:'))
    cont += 1
    lista.append(num)

    opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção in 'N':
        break
print(f'Foi digitado {cont} número(s)')

lista.sort(reverse=True)
print(f'A lista em forma decrescente é: {lista}')
if 5 in lista:
    print('O número 5 foi digitado e está na lista.')
else:
    print('O número 5 não foi digitado e por isso não está na lista.')

