# Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
print('-' * 30)
print('        JOGA NA MEGA      ')
print('-' * 30)
lista = list()
jogos = list()
tot = 1
jogador = int(input('Digite aqui quantos jogos você pretende fazer: '))
while tot <= jogador:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'Sorteando {jogador} números', '=-' * 3)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
print('-=' * 5, 'BOA SORTE!', '=-' * 5)