# Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10. só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
condicao = True
while condicao == True:
    print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
    print('Vamos ver se você consegue adivinhar...')
    lista = []
    for c in range(1, 11):
        lista += [c]
    from random import choice

    maquina = choice(lista)
    escolha = int(input('Digite o número que acha que eu pensei: '))
    cont = 0
    while escolha != maquina:
        if escolha > maquina:
            print('Menos...')
        elif escolha < maquina:
            print('Mais...')
        escolha = int(input('Digite outro número: '))
        cont += 1
    print(f'Acertou!!!... Você precisou de {cont} chances para advinhar. :)')
    continuar = str(input('Quer continuar? (S/N)')).strip()[0]
    while continuar not in 'SsNn':
        print('Digite somente (S) ou (N).')
        continuar = str(input('Quer continuar? (S/N)')).strip()[0]
        if continuar in 'Ss':
            print('Obáaa... Bora jogar denovo então.')
        elif continuar in 'Nn':
            print('Ok então, até a próxima!!!')
            condicao = False