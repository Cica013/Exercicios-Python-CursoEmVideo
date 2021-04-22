# Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de três e que se encontram no
# intervalo entre 1 e 500.
soma = 0
for contador in range (1,501):
    if contador % 2 != 0 and contador % 3 == 0:
        soma += contador
print(soma)
