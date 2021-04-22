# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
# ================================================================================================================
# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores
# como um valor monetário formatado.
from exe108 import moeda
from time import sleep

def lin():
    print('=' * 40)


print('PROGRAMA CALCULA VALORESSSSS!!!!')
lin()
sleep(1)
num = float(input('Digite um número para ser calculado: '))
porcen = int(input('Digite um número para calcular a porcentagem: '))
lin()
print(f'O valor {moeda.moeda(num)} com um aumento de {porcen}% fará o número ficar: {moeda.moeda(moeda.aumentar(num, porcen))}')
lin()
sleep(1)
print(f'O valor {moeda.moeda(num)} com um deconto de {porcen}% fará com que o valor fique: {moeda.moeda(moeda.diminuir(num, porcen))}')
lin()
sleep(1)
print(f'O dobro de {moeda.moeda(num)} será: {moeda.moeda(moeda.dobro(num))}')
lin()
sleep(1)
print(f'A metade de {moeda.moeda(num)} será: {moeda.moeda(moeda.metade(num))}')
lin()
sleep(1.5)
print('FIM DO PROGRAMA!!!')