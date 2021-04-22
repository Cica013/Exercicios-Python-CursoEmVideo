# A confederação de natação precisa de um programa que leia o ano de nascimento de um atleta e moste sua categoria,
# de acordo com a idade:
# - Até 9 anos: Mirim  - Até 14 anos: Infantil  - Até 19 anos: Junior  - Até 25 anos: Sênior  - Acima: Master.
from datetime import date
print('\033[1;33m+=\033[m'*50)
print('Vamos avaliar a sua idade para ver qual a sua classificação para as olimpíadas de natação')
print('\033[1;33m+=\033[m'*50)
nasc = int(input('Digite aqui a sua data de nascimento: '))
idade = date.today().year - nasc
print(f'A sua idade atual é: {idade}')

if idade < 0:
    print('Você nem nasceu ainda Porra!')
elif idade < 1:
    print('Ele ainda é um bebê e não pode nadar se não sabe nem engatinhar.')
elif idade <= 9:
    print('Você se classifica na faixa etária mirim.')
elif idade <= 14:
    print('Você se classifica na faixa etária Infantíl.')
elif idade <= 19:
    print('Você se classifica na faixa etária Junior.')
elif idade <= 25:
    print('Você se classifica na faixa etária Sênior.')
elif idade > 25:
    print('Você se classifica na faixa etária Master.')

print('Boa sorte nos Jógos! :)')

