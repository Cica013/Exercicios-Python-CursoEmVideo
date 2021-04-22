# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
# de tipo invalido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO... Digite um número inteiro.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n O programa foi interrompido pelo usuário.')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO... Digite um número real válido.\033[m')
            continue
        else:
            return num


num = leiaInt('Digite um número inteiro: ')
print(f'O número inteiro digitado foi: {num}')
numF = leiaFloat('Digite um número flutuante: ')
print(f'O número real digitado foi: {numF}')

