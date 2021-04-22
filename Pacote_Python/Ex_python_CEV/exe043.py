# Desenvolva um programa que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo
# com a tabela abaixo: - Abaixo de 18.5: Abaixo do peso. -Entre 18.5 e 25 Peso ideal
# - 25 até 30: sobrepeso  - 30 até 40: Obesidade  - Acima de 40: Obesidade Morbida.
peso = float(input('Digite aqui o seu peso: '))
alt = float(input('Digite aqui a sua altura: '))
imc = peso / (alt ** 2)
print(f'Seu IMC é: {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc <= 25:
    print('Você está no peso ideal')
elif imc <= 30:
    print('Você está com sobrepeso.')
elif imc <= 40:
    print('Você está com obesidade.')
else:
    print('Obesidade morbida. :(')
