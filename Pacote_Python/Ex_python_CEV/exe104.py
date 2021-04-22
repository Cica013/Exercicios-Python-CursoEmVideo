# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função imput() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# EX: n=leiaInt('Digite um número inteiro: ')
def leiaInt(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mErro... Digite apenas número inteiro!!!\033[m')
        if ok:
            break
    return valor


# Programa principal.
n = leiaInt('Digite um número: ')
print(f'Você digitou o número: {n}.')
print('Fim do programa...')