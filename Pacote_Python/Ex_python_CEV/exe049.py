# Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.
num = int(input('Escolha um número: '))
for c in range(1, 11):
    print(f'{num}x{c}={num*c}')
