# Crie um programa que faça o computador jogar JOKENPÔ com você.
print('-='*25)
print('Vamos jogar JOKENPÔ???')
print('-='*25)
sn = str(input('Digite (SIM) ou (NÃO): ')).strip().upper()
lista = ['PEDRA', 'PAPEL', 'TESOURA']
if sn == 'SIM':
    from time import sleep
    from random import choice
    print('Obaaaá. Bora jogar então.')
    sleep(2)
    print('''Bora lá. Escolhe:
     (PEDRA), (PAPEL), ou (TESOURA)???''')
    sleep(1)
    opcao = str(input('Pode digitar aqui: ')).strip().upper()
    maquina = choice(lista)
    print('maquina = ', maquina)
    print('Pessoa = ', opcao)
    if opcao == 'PEDRA' and maquina == 'TESOURA' or opcao == 'TESOURA' and maquina == 'PAPEL' or opcao == 'PAPEL' and maquina == 'PEDRA':
        sleep(1)
        print('Humano maldito!! Você venceu!!')
    elif opcao != 'PEDRA' and opcao != 'PAPEL' and opcao != 'TESOURA':
        print('Você digitou algo errado aí. Humano Burro!!')
    elif opcao == maquina:
        print('Deu EMPATEEEE!!!')
    else:
        sleep(1)
        print('Eu venci. Sempre soube que as maquinas eram melhores que os seres humanos!!')
else:
    print('Não quer jogar então sai fora!!!')