# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final mostre os valores pares e ímpares em ordem crescente.
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print('-=' * 40)
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores ímpares digitados foram {num[1]}')
lista = num[0]+num[1]
print(f'Lista concatenada: {lista}')
print(f'Lista concatenada em ordem crescente: {sorted(lista)}')
