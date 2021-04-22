# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
# de pagamento: - À vista dinheiro/cheque: 10% de desconto - À vista no cartão: 5% de desconto
# - Em até duas vezes no cartão: preço normal. - 3 vezes ou mais no cartão 20% de juros.
produto = float(input('Digite o valor do produto: '))
print('Agora selecione uma opção de pagamento: ')
print('[1] Para pagamento à vista no dinheiro ou cheque com 10% de desconto.')
print('[2] Para pagamento à vista no cartão com 5% de desconto.')
print('[3] Para pagamento em até duas vezes no cartão pagando o preço normal do produto.')
print('[4] Para pagamento com parcelas de 3 vezes ou mais com 20% de juros. ')
escolha = int(input('Digite a opção desejada: '))
if escolha == 1:
    print(f'O valor do produto sairá com desconto de 10%, você irá pagar R${produto - ((produto*10) / 100):.2f} em vez de R${produto:.2f}.')
elif escolha == 2:
    print(f'O valor do produto sairá com 5% de desconto para você. Então você irá pagar: R${produto - ((produto * 5) / 100):.2f}. ')
elif escolha == 3:
    print(f'O valor do produto não sofrerá alteração, você irá pagar o preço normal de: R${produto:.2f}')
elif escolha == 4:
    print(f'Com esse tipo de pagamento o valor irá ter um juros de 20% colocando o valor de {produto:.2f} no valor {produto +((produto * 20) / 100):.2f}')
