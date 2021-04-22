# Faça um mini-sistema que utilize o interactive Help do python. O usuário vai digitar o comando e o manual vai
# aparecer. quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# OBS: use cores.
from time import sleep

cores = (
    '\033[m',         # 0 - Sem cores
    '\033[0;30;41m',  # 1 - Vermelho
    '\033[0;30;42m',  # 2 - verde
    '\033[0;30;43m',  # 3 - amarelo
    '\033[0;30;44m',  # 4 - azul
    '\033[0;30;45m',  # 5 - roxo
    '\033[;7;30m',    # 6 - branco
        )


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(cores[6], end='')
    help(com)
    print(cores[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')
    sleep(1)


# Programa principal.
comand = ''
while True:
    comand = str(input('Digite o comando ou biblioteca: '))
    if comand.upper().strip() == 'FIM':
        break
    else:
        ajuda(comand)
título('ATÉ LOGO', 1)