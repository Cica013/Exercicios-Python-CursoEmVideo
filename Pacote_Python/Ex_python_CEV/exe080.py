# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção ( sem usar o sort()). No final mostre a lista ordenada na tela.
lista = []
n = 0
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while True:
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(lista)