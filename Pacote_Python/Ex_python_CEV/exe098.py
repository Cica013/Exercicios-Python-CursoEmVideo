# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu
# programa tem que realizar três contagem através da função criado:
# a) De 1 até 10, de 1 em 1.
# b) De 10 até 0, de 2 em 2.
# c) Uma contagem personalizada.
def linha():
    print('*=' * 30)


def contador(a, b, c):
    if a > b:
        for d in range(a, b - 1, c):
            print(d, end=' ')

    else:
        for d in range(a, b + 1, c):
            print(d, end=' ')
    print()


print('FAZENDO A CONTAGEM DE NÚMEROS')
linha()
print('Primeiro de 1 até 10 de 1 em 1')
contador(1, 10, 1)
linha()
print('Agora de 10 até 0 de 2 em 2')
contador(10, 0, -2)
linha()
print('Agora é a sua vez!!!')
n1 = int(input('Digite o início da contagem: '))
n2 = int(input('Digite agora até onde vai a contagem: '))
n3 = int(input('Digite de quantos em quantos ela tem que ir: '))
linha()
print('Sua contagem:', end=' ')
contador(n1, n2, n3)

print('\033[1;31mFIM DO PROGRAMA, ATÉ A PRÓXIMA!\033[m')