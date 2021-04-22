# Crie um programa que mostre na tela todos os números pares que estão entre 1 e 50.
from time import sleep
for contagem in range (1,51):
    if contagem % 2 == 0:
        print(contagem, end=' ')
        sleep(1)
