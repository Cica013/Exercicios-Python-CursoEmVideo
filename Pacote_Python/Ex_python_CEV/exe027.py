# Faça um programa que leia o nome completo de uma pessoa e mostre na tela o seu primeiro e último nome separadamente.
nome = str(input('Digite aqui o seu nome completo: ')).strip()
nome = nome.split()
print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu último nome é: {nome[len(nome)-1]}')
