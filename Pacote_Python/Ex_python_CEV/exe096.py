# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e
# comprimento) e mostre a área do terreno.
def área(a, b):
    m = a*b
    print(f'{m:.2f}')


c = float(input('Digite a dimensão de comprimento do terreno: '))
l = float(input('Digite a largura do terreno: '))
print(f'A dimensão do terreno é de: {área(c, l)}')
