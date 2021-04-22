# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from time import sleep
from random import randint
from operator import itemgetter

jogadores = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6)}

ranking = list()
print('VALORES SORTEADOS: ')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(ranking)
print('-=' * 30)
print(' ==  RANKING DOS JOGADORES  ==  ')
for i, l in enumerate(ranking):
    print(f'{i+1}° lugar: {l[0]} com {l[1]}.')
    sleep(1)
