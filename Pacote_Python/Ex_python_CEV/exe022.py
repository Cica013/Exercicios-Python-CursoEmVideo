# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas. - Quantas letras tem ao todo sem considerar espaços.
# - Quantas letras tem o primeiro nome.
nome = str(input('Digite aqui seu nome completo: ')).strip()
print(f'Seu nome com as letras maiúsculas é: {nome.upper()}')
print(f'Seu nome com as letras minúsculas é: {nome.lower()}')
print(f'''Seu nome tem {len(nome)-nome.count(' ')} letras''')
print(f'''Seu primeiro nome tem {nome.find(' ')} letras.''')