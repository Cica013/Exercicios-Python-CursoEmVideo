# Faça um programa que leia um ângulo na tela e mostre seu seno cosseno e a tângente.
from math import sin, cos, tan, radians
ângulo = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print(f'O seno é: {seno:.2f}, o cosseno é: {cosseno:.2f} e a tângente é: {tangente:.2f} ')