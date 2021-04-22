# Melhore o desafio 61 perguntando se ele quer mostrar mais alguns termos. O programa encerra quando ele
# disser que quer msotrar 0 termos.
print('Vamos analisar uma P.A.')
primeiro = int(input('Digite aqui o termo: '))
razao = int(input('Digite aqui a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você ainda quer mostrar? '))



print('\033[31mFIM!!!')
