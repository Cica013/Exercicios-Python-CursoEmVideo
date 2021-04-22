# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km por hora, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km Acima do limite.
vel = float(input('Digite aqui a velocidade do veículo em Km: '))
if vel > 80:
    print(f'\033[1;31mVocê foi multado em\033[m R${(vel-80) * 7:.2f}')
else:
    print('Você está dentro do limite de velocidade. Tenha uma boa viagem!')