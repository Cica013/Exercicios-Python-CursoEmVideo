# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário inclindo o total de gols feitos durante o campeonato.
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Digite aqui o nome do jogador: '))
tot = int(input('Digite aqui quantas partidas ele jogou: '))
for c in range(1, tot+1):
    partidas.append(int(input(f'Quantos gols ele fez na {c}° partida: ')))
total = sum(partidas)
jogador["gols"] = partidas
jogador["Total gols"] = total
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'   => Na partida {i+1} o jogador marcou {v} gols.')
print(f'Por fim ele marcou {total} gols no total.')

