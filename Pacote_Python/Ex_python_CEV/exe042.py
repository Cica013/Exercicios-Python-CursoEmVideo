# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# -Equilatero: Todos os lados iguais -isóceles: dois lados iguais - escaleno: todos os lados diferentes
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print('Os valores podem formar um triângulo.')
else:
    print('Os valores não podem formar um triângulo.')

if n1 == n2 and n2 == n3:
    print('O triângulo a ser formado é um triângulo equilatero.')
elif n1 == n2 or n1 == n3 or n2 == n3:
    print('O triângulo a ser formado será um isósceles.')
elif n1 != n2 and n1 != n3 and n2 != n3:
    print('O triangulo a ser formado será o triângulo escaleno.')