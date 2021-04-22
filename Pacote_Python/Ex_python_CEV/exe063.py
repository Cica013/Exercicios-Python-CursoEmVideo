# Escreva um programa que leia um número inteiro n qualquer e mostre na tela os n primeiros termos de uma
# sequência fibonacci. ex: 0 1 1 2 3 5 8
print('*'*30)
n = int(input('Digite quantos termos você quer que apareça: '))
print('*'*30)

n1 = 0
n2 = 1
print(f'{n1} -> {n2}', end='')
cont = 3
while cont <= n:
    n3 = n1+n2
    cont +=1
    print(f' -> {n3}', end='')
    n1 = n2
    n2 = n3
print(' FIM!')
