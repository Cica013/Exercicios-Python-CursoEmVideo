# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
# Este é o módulo...
from time import sleep


def lin():
    print('=' * 40)


def aumentar(num=0, por=0, formato=False):
    aumenta = ((num * por) / 100) + num
    return aumenta if formato is False else moeda(aumenta)


def diminuir(num=0, por=0, formato=False):
    diminui = num - (num * por) / 100
    return diminui if formato is False else moeda(diminui)


def dobro(num, formato=False):
    return num * 2 if formato is False else moeda(num * 2)


def metade(num, formato=False):
    return num / 2 if formato is False else moeda(num / 2)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor}'.replace('.', ',')


def resumo(num=0, porcen=0) -> object:
    lin()
    print(
        f'O valor {moeda(num)} com um aumento de {porcen}% fará o número ficar: {aumentar(num, porcen, True)}')
    lin()
    sleep(1)
    print(
        f'O valor {moeda(num)} com um deconto de {porcen}% fará com que o valor fique: {diminuir(num, porcen, True)}')
    lin()
    sleep(1)
    print(f'O dobro de {moeda(num)} será: {dobro(num, True)}')
    lin()
    sleep(1)
    print(f'A metade de {moeda(num)} será: {metade(num, True)}')
    lin()
    sleep(1.5)
