# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos eles,
# mostre também o maior e o menor. O programa deve perguntar se o usuário quer continuar a cada interação.
resp = 'S'
soma = 0
cont = 0
maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]

print(f'Você digitou {cont} números, e a média entre todos eles é: {soma / cont}')
print(f'O maior número digitado foi: {maior} e o menor número digitado foi: {menor}.')
