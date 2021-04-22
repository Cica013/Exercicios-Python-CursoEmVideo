# Faça um programa que leia o valor de um produto e mostre seu novo valor com 5% de desconto.
produto = float(input('Digite aqui o valor do produto: '))
desconto = (produto*5) / 100
valor = produto - desconto
print(f'O valor do produto é de {produto} , Seu dosconto é de {desconto} , o Valor final será: {valor} .')