# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final mostre:
# a) Quantas pessoas tem menos de 18 anos b) quantos homens foram cadastrados c) Quantas mulheres tem menos de 20 anos.
menor = 0
homens = 0
mulheres = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: [M/F]  ')).strip().upper()[0]
    continuar = str(input('Quer continuar? [S/N]:  ')).strip().upper()[0]
    if continuar == 'N':
        break
    if idade < 18:
        menor += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulheres += 1
print(f'No grupo digitado temos {menor} pessoas com menos de 18 anos, temos {homens} homens cadastrados e por fim, '
      f'no grupo tem {mulheres} mulheres abaixo de 20 anos.')