# Faça um programa que tenha uma lista chamada números e duas funções chamadas Sorteia() e somaPar(). A primeira
# função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os
# valofes pares sorteados pela função anterior.
from random import randint
def sorteia(lista):
    for c in range(1, 6):
        lista.append(randint(1, 20))
    print(lista)


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos números pares é: {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)
