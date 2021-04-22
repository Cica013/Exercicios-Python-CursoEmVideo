# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,
# mostre o conteúdo da estrutura na tela.
nome = str(input('Digite o nome do aluno: '))
media = float(input('Digite a média do aluno: '))
aluno = {'nome': nome, 'media': media}
print(f'O aluno {aluno["nome"]}, tirou a média: {aluno["media"]}')
