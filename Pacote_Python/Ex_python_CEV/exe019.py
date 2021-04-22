# O professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que o ajude com isso.
from random import choice
lista = []
for x in range(1,5):
    nome = str(input(f'Digite o nome do {x}° aluno: '))
    lista += nome
print(choice(lista))