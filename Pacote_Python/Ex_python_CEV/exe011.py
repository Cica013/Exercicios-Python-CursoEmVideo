# Faça um programa que leia a largura e a altura de uma parede, mostre sua dimensão na tela e em seguida mostre quantos
# litros de tinta será necessário para pinta-lá. Considerando que 1 litro de tinta pinta dois metros quadrados.
larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = alt * larg
print(f'A área da parede é de {area:.1f}')
tinta = area / 2
print(f'Você irá precisar de {tinta:.1f} litros de tinta para pintar essa parede.')