# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas. b) Uma listagem com as pessoas mais pesadas. c) uma listagem com as pessoas
# mais leves.
grupo = list()
pessoa = list()
mai = men = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if mai == 0:
        mai = men = pessoa[1]
    else:
        if pessoa[1] > mai:
            mai = pessoa[1]
        if pessoa[1] < men:
            men = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()
    resp = str(input('Quer continuar? [S/N]')).strip()[0]
    if resp in 'Nn':
        break
print(f'Ao todo no grupo tem: {len(grupo)} pessoas.')
print(f'O maior peso foi de: {mai}, das pessoas: ', end=' ')
for p in grupo:
    if p[1] == mai:
        print(f'{p[0]}', end=', ')
print()
print(f'O menor peso foi de: {men} das pessoas: ', end=' ')
for p in grupo:
    if p[1] == men:
        print(f'{p[0]}', end=', ')
print()
