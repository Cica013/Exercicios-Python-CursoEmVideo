# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados... b) A soma dos valores de terceira coluna...
# c) O maior valor da segunda linha.
par = col = lin = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l}] [{c}] da matriz: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            col += matriz[l][c]
        if l == 1:
            lin += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos pares deu: {par}')
print(f'A soma dos valores da terceira coluna deu: {col}')
print(f'A soma dos valores da segunda linha foram: {lin}')
