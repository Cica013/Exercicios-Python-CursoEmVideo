# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando O total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
cont = 0
while True:
    jogadorNum = int(input('Digite aqui um número: '))
    jogadorPI = str(input('Você escolhe par ou impar? [P/I]:  ')).strip().upper()[0]
    maquinaNum = randint(0, 111)
    teste = (jogadorNum + maquinaNum) % 2
    if teste == 0:
        teste = 'P'
    elif teste == 1:
        teste = 'I'
    if jogadorPI == teste:
        cont += 1
        print(f'Eu escolhi: {maquinaNum}, Você: {jogadorNum} que dá: {jogadorNum+maquinaNum}')
        print(f'Você ganhou {cont} vez(es).')
        print('Você venceu. Vamos jogar novamente!!!')
    else:
        print(f'''Você escolheu {jogadorNum} e eu: {maquinaNum}. Que dá {jogadorNum+maquinaNum} 
Eu venci!!!
Você venceu {cont} vez(es).''')
        break

print('Fim!!!')
