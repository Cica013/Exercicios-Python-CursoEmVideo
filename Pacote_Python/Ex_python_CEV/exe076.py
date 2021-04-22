# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final mostre uma listagem de preços, organizando os dados de forma tabular.
listagem = ('Lápis', 1.75,
            'Caneta', 3.50,
            'Borracha', 2.00,
            'Caderno', 15.00,
            'Livro', 35.50,
            'Fichario', 30.00)
print(40*'=')
print('LISTA DE COMPRAS:')
print(40*'=')
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R${listagem[item]: ^7}')
