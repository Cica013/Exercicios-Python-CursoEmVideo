# Faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado pelo usuário.
# O programa será interrompido quando o usuário digitar um valor negativo.
print(10 * '=-', 'Vamos ver a tabuada?', 10 * '=-')
while True:
    num = int(input('Digite um número: (Digite um número negativo para parar):  '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{c}x{num}={c*num}')
    print('Vamos novamente.')
print('Muito obrigado por utilizar nossso programa de tabuada!!! Volte sempre...')