# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
# ================================================================================================================
# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores
# como um valor monetário formatado.
# ================================================================================================================
# modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o
# valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108
# =================================================================================================================
# Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
# informações geradas pelas funçções que já temos no módulo criado até aqui.
# =================================================================================================================
# Crie um pacote chamado utilidadesCeV qque tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107,108 e 109 para o primeiro pacote e mantenha tudo funcionando.
from exe112.utilidadesCeV import moeda, dado
from time import sleep


def lin():
    print('=' * 40)


print('PROGRAMA CALCULA VALORESSSSS!!!!')
lin()
sleep(1)
num = dado.leiaDinheiro('Digite o valor a ser calculado: ')
porcen = dado.leiaDinheiro('Digite a porcentagem a ser calculada: ')
moeda.resumo(num, porcen)

print('FIM DO PROGRAMA!!!')

