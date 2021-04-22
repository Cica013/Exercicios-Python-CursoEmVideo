# Crie um programa que leia dois valores e mostre um menu como o abaixo na tela. Seu programa deverá realizar
# a operação solicitada em cada caso.
# [1] somar [2] multiplicar [3] maior [4] novos números [5] sair do programa.
cond = True
while cond == True:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    print('''Agora escolha uma das condições abaixo:
    [1] somar.
    [2] Multiplicar.
    [3] maior.
    [4] nóvos números.
    [5] Sair do programa.''')
    escolha = int(input('Digite aqui o número de sua opção: '))
    if escolha == 1:
        soma = n1+n2
        print(f'A soma dos valores é? {soma}')
    elif escolha == 2:
        print(f'Os valores multiplicados resultará em {n1*n2}')
    elif escolha == 3:
        maior = n1
        if n2 > n1:
            maior = n2
            print(f'O maior valor é: {maior}')
    elif escolha == 4:
        print()
    elif escolha == 5:
        cond = False
print('FIM!')