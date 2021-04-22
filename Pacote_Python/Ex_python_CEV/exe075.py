# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Qunatas vezes apareceu o valor 9. b) Em que posição foi digitado o primeiro 3. c) Quais foram os números pares.
num = (int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')))
print(f'Você digitou os números {num}')
print(f'Nesta lista aparece o número 9: ({num.count(9)}) vez(es).')
if 3 in num:
    print(f'O número 3 foi encontrado em: ({num.index(3)+1}) posição.')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
for c in num:
    if c % 2 == 0:
        print('Os números pares digitados foram: ', end='')
        print(c, end=' ')