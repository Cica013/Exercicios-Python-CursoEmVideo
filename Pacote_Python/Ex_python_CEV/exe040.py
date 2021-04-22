# Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final,
# de acordo com a média atingida.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print(f'A média do aluno foi {media:.1f} e ele foi \033[1;32mAPROVADO!\033[m')
elif media >= 5:
    print(f'A média do alino foi {media:.1f} e ele foi aprovado com \033[1;33mRECUPERAÇÃO!\033[m')
else:
    print(f'A média do aluno foi {media:.1f} e ele foi \033[1;31mREPROVADO!\033[m')
