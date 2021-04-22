# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso
# você deve mostrar para cada palavra, quais são as suas vogais.
tupla = ('banana', 'maça', 'bolo', 'pera', 'cadeira', 'mesa', 'amora', 'goiabada')
for palavra in tupla:
    print(f'\nA palavra: {palavra}, contém', end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, ',',  end=' ')
