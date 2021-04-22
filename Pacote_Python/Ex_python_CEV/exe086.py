# Crie um programa que cria uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formação correta.
matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite o número da parte [{l}, {c}] da matriz: ')))
for l in range(0, 3):
    for c in range(0, 3):
        print(f' [{matriz[l][c]:^5}]', end='')
    print()
