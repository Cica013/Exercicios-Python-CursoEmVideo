# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
# Este é o módulo...
def aumentar(num=0, por=0):
    aumenta = ((num * por) / 100) + num
    return aumenta


def diminuir(num=0, por=0):
    diminui = num - (num * por) / 100
    return diminui


def dobro(num):
    return num*2


def metade(num):
    return num/2


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor}'.replace('.', ',')
