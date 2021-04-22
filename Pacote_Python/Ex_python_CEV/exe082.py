# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores impares digitados respectivamente. ao final, mostre o conteúdo das três
# listas gerados.
lista = []
par = []
impar = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    elif num % 2 != 0:
        impar.append(num)
    escolha = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if escolha in 'N':
        break
lista.sort()
par.sort()
impar.sort()
print(f'Lista: {lista}')
print(f'Lista par: {par}')
print(f'Lista impar: {impar}')
