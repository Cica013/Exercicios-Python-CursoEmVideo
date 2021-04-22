# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.
def escreva(txt):
    s = len(txt)+4
    print('~' * s)
    print(f'  {txt}')
    print('~' * s)


escreva('Meu curso de python')
escreva('Cica')
