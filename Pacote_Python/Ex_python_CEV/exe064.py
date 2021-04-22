# Criem um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
num = 0
cont = 0
n = 0
while n != 999:
    n = int(input('Digite um número: [999 PARA SAIR...] '))
    if n != 999:
        num += n
        cont += 1
print(f'Você digitou {cont} números. A soma entre eles resultará em: {num}')