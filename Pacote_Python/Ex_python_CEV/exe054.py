# Criem um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.
maior = 0
menor = 0
from datetime import date
for c in range(1,8):
    nasc = int(input('Digite a sua data de nascimento: '))
    idade = date.today().year - nasc
    if idade < 18:
        menor += 1
    elif idade >= 18:
        maior += 1
print(f'O grupo tem {menor} menores de idade e {maior} maiores de idade.')