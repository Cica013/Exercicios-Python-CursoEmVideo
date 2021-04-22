# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do progrma mostre:
# -A média de idade do grupo. -Qual o nome do homem mais velho. -Quantas mulheres tem menos de 20 anos de idade.
somaIdade = 0
idadeHomem = 0
maisVelho = ''
contaMulher = 0
for c in range(1,5):
    print(10*'=',f'{c}° Pessoa', 10*f'=')
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite (M/F) para o Sexo: ')).strip().upper()
    print(30*'=')
    somaIdade += idade
    if c == 1 and sexo == 'M':
        idadeHomem = idade
        maisvelho = nome
    if sexo == 'M' and idade > idadeHomem:
        idadeHomem = idade
        maisvelho = nome
    if sexo == 'F' and idade < 20:
        contaMulher += 1
mediaIdade = somaIdade / 4
print(f'A média de idade do grupo é: {mediaIdade}')
print(f'O nome do Homem mais velho é: {maisvelho}')
print(f'No grupo há {contaMulher} mulher(es) com menos de 20 anos de idade.')


