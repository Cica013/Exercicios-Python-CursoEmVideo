# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores à 1.250,00, calcule um aumento de 10% . Para inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite aqui o salário do funcionário: '))
if salario > 1250:
    aumento = (salario * 10) / 100
else:
    aumento = (salario * 15) / 100
n_salario = salario + aumento
print(f'O salário do funcionário será de {n_salario} ')
