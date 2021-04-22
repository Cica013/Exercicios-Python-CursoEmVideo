# Escreva um programa que faça o computador pensar em um número de 0 à 5 e peça para o usuário tentar descobrir qual foi o número escolhido
# pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
lista = [0, 1, 2, 3, 4, 5]
from random import choice
escolha = choice(lista)
from time import sleep
print(f''' \033[1;32mVamos jogar um jogo?
 Quero ver se você consegue adivinhar em qual número eu estou pensando\033[m''')
sleep(2)
num = int(input('\033[34mDigite um número de 0 à 5: \033[m'))
print('huuummm, Deixa eu pensar...')
sleep(3)
if num == escolha:
    print('\033[1;35mNossaaaaa você é bom nesse jogo!!!!\033[m')
elif num > 5 or num < 0:
    print('\033[1;31;43mCara, digite algo que se encaixe na brincadeira.\033[m')
else:
    print('\033[36m Eu sabia que um humano não seria pário para uma máquina como eu.\033[m')