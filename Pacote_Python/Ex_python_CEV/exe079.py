# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. caso o número
# já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.
lista = []
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print()
    else:
        lista.append(num)
    escolha = str(input('Deseja continuar? [s/n]')).strip().upper()[0]
    if escolha in 'N':
        break
print(sorted(lista))
