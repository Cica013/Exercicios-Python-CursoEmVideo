# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. seu aplicativo deverá analisar
# se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expr = input('Digite a expressão: ')
a = expr.count('(')
b = expr.count(')')
if a == b:
    print('Sua expressão é válida.')
else:
    print('Sua expressão é invalida.')
print('FIM!!')