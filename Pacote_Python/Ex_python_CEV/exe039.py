# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai
# se alistar ao serviço militar, se é a hora de se alistar ou se já passou tempo do alistamento. Seu programa também
# deverá mostrar o tempo que falta ou que passou do prazo.
from time import sleep
from datetime import date
atual = date.today().year
nasc = int(input('Digite aqui a data do seu nascimento: '))
idade = atual - nasc
alistamento = 18
print('\033[34mProcessando...\033[m')
sleep(2)
print(f'Você tem: \033[1;31m{idade}\033[m anos de idade.')
if idade == alistamento:
    print('\033[33mProcessando...\033[m')
    sleep(2)
    print('Cheguou a hora de você se alistar!')
elif idade < alistamento:
    print('\033[33mProcessando...\033[m')
    sleep(2)
    print(f'Ainda não está na hora de você se alistar. Faltam exatamente \033[1;31m{alistamento - idade}\033[m anos para você se alistar.')
elif idade > alistamento:
    print('\033[33mProcessando...\033[m')
    sleep(2)
    print(f'Você já passou \033[1;31m{idade - alistamento}\033[m anos da idade de alistamento. \033[1;32m MELHOR CORRER!!!\033[m')
print(f'\033[1;36mFIM!\033[m')