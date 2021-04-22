# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por cada Km
# para viagens de até 200km e R$0,45 para viagens mais longas.
viagem = float(input('Digite aqui a distância em Km da Viagem: '))
if viagem <= 200:
    calc = viagem * 0.50
    print('A sua viagem vai sair sem desconto. ')
else:
    calc = viagem * 0.45
    print('O valor da viagem vai ser com desconto.')
print(f'Você irá pagar R${calc:.2f} na sua viagem')
