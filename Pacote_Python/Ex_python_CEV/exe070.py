# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre: a) Qual é o total gasto na compra. b) Quantos produtos custam mais de 1000 reais.
# c) Qual o nome do produto mais barato.
print(10*'=', 'LOJINHA SANTA EFIGÊNIA', 10*'=')
cont = caro = total = barato = 0
nome = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o proço do produto: '))
    total += preço
    cont += 1
    if preço > 1000:
        caro += 1
    if cont == 1:
        barato = preço
        nome = produto
    else:
        if preço < barato:
            barato = preço
            nome = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break

print('Fim do programa.')
print(f'O total da compra foi: {total:.2f}')
print(f'Na compra tem {caro} produtos acima de mil reais.')
print(f'O produto mais barato foi {nome} de preço: {barato:.2f}')
