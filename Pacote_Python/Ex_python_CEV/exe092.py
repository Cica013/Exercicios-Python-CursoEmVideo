# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário se
# por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar, considerando que ela deve ter 35 anos
# de contribuição.
from datetime import date

nome = str(input('Digite aqui o nome: '))
nasc = int(input('Digite aqui o ano de nascimento: '))
cart = int(input('Digite aqui a carteira de trabalho (Ou 0 se não possuir): '))
idade = date.today().year - nasc
if cart == 0:
    lista = dict(nome=nome, idade=idade, carteira='Não possui CTPS.')
else:
    contrato = int(input('Qual foi o ano de contratação?: '))
    salario = float(input('Qual o salário?: '))
    aposen = (contrato - nasc) + 35
    lista = dict(
        nome=nome,
        idade=idade,
        carteira=cart,
        contratação=contrato,
        salário=salario,
        aposentadoria=aposen
    )
for k, v in lista.items():
    print(f'{k} = {v}')
