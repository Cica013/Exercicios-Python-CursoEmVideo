# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final tudo isso será
# guardado em um dicionário, incuindo o total de gols feitos durante o campeonato.  Aprimore o Desafio 093 para que
# ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = list()
while True:
    jogador = dict()
    jogador['nome'] = str(input('Digite aqui o nome do jogador: '))
    jogador['partidas'] = int(input('Digite o número de partidas jogadas: '))
    gol = 0
    gols = []
    totGols = 0
    for c in range(1, jogador['partidas']+1):
        gol = int(input(f'Digite aqui quantos gols ele fez na {c}° partida: '))
        gols.append(gol)
        totGols += gol
    jogador['gols'] = gols
    jogador['Total gols'] = totGols
    print('*=' * 30)
    for k, v in jogador.items():
        print(f'O campo: {k} tem o valor: {v}.')
        print('*='*30)
    time.append(jogador.copy())
    jogador.clear()
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
for i, v in enumerate(time):
    print(f'Jogador {i+1}. Nome: {v["nome"]}')
    print('*=' * 30)
while True:
    escolha = int(input('Digite o número do jogador que deseja analizar: '))
    for i, v in enumerate(time):
        if escolha == i+1:
            print(v)
