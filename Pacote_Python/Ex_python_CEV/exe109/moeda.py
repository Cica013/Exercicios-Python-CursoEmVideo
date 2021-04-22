# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
# Este é o módulo...
def aumentar(num=0, por=0, formato=False):
    aumenta = ((num * por) / 100) + num
    return aumenta if formato is False else moeda(aumenta)


def diminuir(num=0, por=0, formato=False):
    diminui = num - (num * por) / 100
    return diminui if formato is False else moeda(diminui)


def dobro(num, formato=False):
    return num*2 if formato is False else moeda(num*2)


def metade(num, formato=False):
    return num/2 if formato is False else moeda(num/2)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor}'.replace('.', ',')
