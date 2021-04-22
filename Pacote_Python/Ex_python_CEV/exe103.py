# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: O nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.
def ficha(nome='Jogador desconhecido.', gols=0):
    fichaJogador = dict()
    fichaJogador['nome'] = nome
    fichaJogador['gols'] = gols
    print(f'O jogador: {fichaJogador["nome"]}, marcou: {fichaJogador["gols"]} gols.')



j = str(input('Digite o nome do jogador: '))
g = str(input('Digite quantos gols o jogador fez: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gols=g)
else:
    ficha(j, g)

