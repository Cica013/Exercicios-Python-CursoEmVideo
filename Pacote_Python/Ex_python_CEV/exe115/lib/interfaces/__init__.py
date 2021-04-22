def linha(tam=42):
    return '~' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    for key, value in enumerate(lista):
        print(f'\033[33m{key+1}\033[m-\033[34m{value}\033[m')
    print(linha())
    opc = leiaInt('\033[32mDigite sua opção: \033[m')
    return opc


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO... Digite um número inteiro.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n O programa foi interrompido pelo usuário.')
            return 0
        else:
            return num
