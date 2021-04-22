# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o
# maior e o menor valor digitados e as suas respectivas posições na lista.
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite o {c+1}° valor: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(30*'*')
print(f'Lista: ', listanum)
print(50 * '*')
print(f'O maior valor digitado foi: {mai}', end=' ')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'Na posição: {i}...')
print(50 * '*')
print(f'O menor valor digitado foi: {men}', end=' ')
for u, m in enumerate(listanum):
    if m == men:
        print(f'Na posição: {u}...')
print(50 * '*')
print('FIM!!')
