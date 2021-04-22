# Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60,00 R$ por dia e 0,15 R$ por Km rodado.

print('Vamos calcular o valor do aluguel do seu carro.')
dia = int(input('Digite aqui a quantidade de dias que você alugou o carro: '))
km = float(input('Digite aqui a quantidade de km percorridos com o carro: Km '))
totalDia = 60.0 * dia
totalKm = 0.15 * km
total = totalDia + totalKm
print(f'O valor cobrado pelas diárias com o veículo foi de R${totalDia}, e o valor cobrado pelo km percorrido foi de R${totalKm}, o Valor total a ser pago é de: R${total}')