# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
from exe107 import moeda
from time import sleep

def lin():
    print('=' * 40)

print('PROGRAMA CALCULA VALORESSSSS!!!!')
lin()
sleep(1)
num = int(input('Digite um número para ser calculado: '))
porcen = int(input('Digite um número para calcular a porcentagem: '))
lin()
print(f'O valor {num} com um aumento de {porcen}% fará o número ficar: {moeda.aumentar(num, porcen)}')
lin()
sleep(1)
print(f'O valor {num} com um deconto de {porcen}% fará com que o valor fique: {moeda.diminuir(num, porcen)}')
lin()
sleep(1)
print(f'O dobro de {num} será: {moeda.dobro(num)}')
lin()
sleep(1)
print(f'A metade de {num} será: {moeda.metade(num)}')
lin()
sleep(1.5)
print('FIM DO PROGRAMA!!!')