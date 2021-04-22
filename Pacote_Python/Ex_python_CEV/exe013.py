# Faça um programa que leia um salário de um funcionário e mostre seu novo salário com 15% de aumento.
salario = float(input('Digite aqui seu salário: '))
aumento = (salario * 15) / 100
novosalario = salario + aumento
print(f'Seu antigo salário era de {salario}, você vai receber um aumento de {aumento}, seu novo salário é {novosalario}')