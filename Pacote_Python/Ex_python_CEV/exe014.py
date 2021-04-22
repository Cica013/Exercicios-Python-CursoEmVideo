# Escreva um programa que leia uma temperatura em C° e a converta para F°
c = float(input('Digite aqui a temperatura em C°: '))
conversão = ((9 * c) / 5) + 32
print(f'A temperatura em C° digitada foi de {c} e convertida em F° será {conversão}')