# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele pretende pagar.
# A prestação mensal não pode exceder 30% do salário ou então o emprestimo será negado.
casa = float(input('Digite aqui o valor da casa: '))
salario = float(input('Digite aqui o valor do salário: '))
anos = int(input('Digite aqui em quantos anos pretende pagar: '))
meses = anos * 12
mensalidade = casa / meses
print(f'mensalidade: {mensalidade:.2f}')
porc = (salario*30/100)
print(f'Porcentagem: {porc:.2f}')
if mensalidade > porc:
    print(f'As mensalidades da casa sairão no valor de {mensalidade:.2f}. e esse valor exede a porcentagem necessária '
          f'para a aprovação do emprestimo. Dessa maneira o emprestimo será negado.')
else:
    print('Seu emprestimo foi aprovado!')
