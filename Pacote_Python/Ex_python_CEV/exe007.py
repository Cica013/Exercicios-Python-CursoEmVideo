# Crie um programa que leia as duas notas de um aluno calcule e motre a sua média
nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1+n2) / 2
print(f'A média do aluno {nome}, é: {media}')