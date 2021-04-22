# Faça um programa que leia um valor em metros e motre na tela seu valor em centímetros e milímetros
num = float(input('Digite um valor: '))
centímetros = num * 100
milímetros = num * 1000
print(f'O valor em centímetros é: {centímetros:.0f}  e o valor em milímetros é: {milímetros:.0f}')
