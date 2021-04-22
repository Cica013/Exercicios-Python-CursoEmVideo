# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# - Quantidade de notas - A maior nota - A menor nota
# - A média da turma - A situação (opcional) Adicione também as docstrings.
def notas(*n, sit=False):
    f = dict()
    f['total'] = len(n)
    f['maior'] = max(n)
    f['menor'] = min(n)
    f['média'] = sum(n) / len(n)
    if sit:
        if f['média'] >= 7:
            f['situação'] = 'Boa!!'
        elif f['média'] >= 5:
            f['situação'] = 'Razoável!'
        else:
            f['situação'] = 'Ruim.'
    return f


# Programa principal.
resp = notas(2, 5, 6, 1, sit=True)
print(resp)
