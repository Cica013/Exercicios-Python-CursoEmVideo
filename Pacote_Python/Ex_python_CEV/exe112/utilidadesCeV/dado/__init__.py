# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
# leiaDinheiro() que seja capaz de funcionar como a função input, mas com uma validação de dados para aceitar
# apenas valores que sejam monetários.
def leiaDinheiro(txt=''):
    while True:
        num = str(input(f'{txt}: ')).replace(',', '.')
        if num.isalpha() or num.strip() == '':
            print(f'\033[1;31mO número {num} não é válido: \033[m')
        else:
            return float(num)
