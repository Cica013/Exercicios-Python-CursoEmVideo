# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
valor = int(input('Que valor você quer sacar?:  '))
total = valor
totced = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f'Você irá receber {totced} notas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
