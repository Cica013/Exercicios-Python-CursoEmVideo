# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
# um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
ficha = list()
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Dejesa continuar? [S/N]')).strip()[0]
    if resp in 'Nn':
        break
for n, f in enumerate(ficha):
    print(f'{n+1}° Nome: {f[0]}. média: {f[2]:.1f}')
escolha = str(input('Quer ver as notas de algum aluno? [S/N]')).strip()[0]
while True:
    if escolha in 'Ss':
        notaAluno = int(input('Digite o número do aluno que gostaria de ver a nota: '))
        for c, f in enumerate(ficha):
            if notaAluno == c+1:
                print(f'Aluno: {f[0]} notas: {f[1]}')
        resp = str(input('Quer ver mais algum? [S/N]')).strip()[0]
        if resp in 'Nn':
            break
    else:
        break
print('Fim do programa...')
print('Até a próxima...')
