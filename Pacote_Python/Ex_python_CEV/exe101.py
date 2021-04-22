# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa.
# retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou Obrigatório nas eleições.
from datetime import date

def voto(ano):
    anoAtual = date.today().year
    idade = anoAtual - ano
    if idade < 16:
        return f'Você tem {idade} anos e não pode votar ainda!'
    elif idade >= 16 and idade < 18:
        return f'Você tem {idade} anos e pode escolher se quer ou não votar, é opcional.'
    elif idade >= 18 and idade <= 60:
        return f'Você tem {idade} anos de idade e é obrigatório o seu voto!'
    elif idade > 60:
        return f'Você tem {idade} anos de idade e tem o voto opcional.'


nasc = int(input('Digite o seu ano de nascimento: '))
print(voto(nasc))
