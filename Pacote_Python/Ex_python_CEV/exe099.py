# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros em valores inteiros.
# seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*num):
    cont = 0
    mai = 0
    print('Analizando valores passados...')
    for valor in num:
        print(valor, end=' ')
        if cont == 0:
            mai = valor
        else:
            if valor >= mai:
                mai = valor
        cont += 1
    print(f'\nO maior valor é: {mai} ')


maior(2, 5, 6, 9, 1, 2, 3, 7, 12)
maior(5, 3, 4, 9, 6, 65, 456, 2123156, 45648975132, 1234645, 456412345612678, 12456784165496452)
maior(1, 3, 9, 11, 25, 23)
