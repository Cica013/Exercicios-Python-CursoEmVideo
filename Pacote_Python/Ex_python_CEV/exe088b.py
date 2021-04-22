# Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint

jogo = list()
jogos = list()
print('=' * 30)
print('     \033[33m Sorteando jogos \033[m     ')
print('=' * 30)
jogador = int(input('\033[36mQuantos jogos você quer fazer?\033[m '))
tot = 1
while tot <= jogador:
    cont = 0
    while cont <= 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    tot += 1

for i, j in enumerate(jogos):
    print(f'\033[32mjogo \033[35m{i+1}: {j}')
