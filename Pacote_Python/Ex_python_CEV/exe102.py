# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: O primeiro que indique o número a
# calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do farorial.
def fatorial(num, show=False):
    print('Calculando fatorial...')
    fat = 1
    for c in range(num, 0, -1):
        if show:
            if c > 1:
                print(c, end=' x ')
            else:
                print(end=' = ')
        fat *= c
    return fat


print(f'{fatorial(5, True):.1f}')
