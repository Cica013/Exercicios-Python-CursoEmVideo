# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# utilizando a estrutura while.
print('Vamos analisar uma P.A.')
termo = int(input('Digite aqui o termo: '))
razao = int(input('Digite aqui a razão: '))
cont = 1
while cont <= 10 :
    print(termo, end=' ')
    termo += razao
    cont += 1

print('\033[31mFIM!!!')
