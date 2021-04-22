# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# a) Quantas pessoas cadastradas. b) A média de idade.
# c) uma lista com mulheres. d) Uma lista com idade acima da média.
dicio = dict()
lista = list()
while True:
    nome = str(input('Digite aqui o nome: ')).strip()
    while True:
        sexo = str(input('Digite aqui o sexo: ')).strip()
        if sexo in 'FfMm':
            break
        else:
            print('Erro... Digite apenas F ou M')

    idade = int(input('Digite aqui a idade: '))
    dicio = dict(nome=nome, sexo=sexo, idade=idade)
    lista.append(dicio.copy())
    dicio.clear()
    opcao = str(input('Deseja continuar cadastrando? [S/N]')).strip()[0]
    if opcao in 'Nn':
        break
    else:
        print('Mais um então!...')
print(f'Foram cadastradas {len(lista)} pessoas.')
soma = 0
for c in lista:
    soma += c['idade']
media = soma / len(lista)
print(f'A média de idade do grupo é de: {media:5.2f}')
print('*='*30)
woman = list()
for f in lista:
    if f['sexo'] in 'Ff':
        woman.append(f['nome'])
print(f'As mulheres do grupo são: {woman}')
print('*='*30)
print('As pessoas com a idade acima da média do grupo são: ')
for i in lista:
    if i['idade'] > media:
        print(f'Nome: {i["nome"]} com idade: {i["idade"]}')
