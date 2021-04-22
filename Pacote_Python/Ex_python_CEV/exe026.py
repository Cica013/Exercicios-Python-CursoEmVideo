# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em qual posição ela aparece a primeira vez
# Em qual posição ela aparece por último.

frase = str(input('Digite aqui uma frase: ')).strip().upper()
print(f'''Na frase foi encontrato {frase.count('A')} letras A ''')
print(f'''A primeira letra A está na posição {frase.find('A')}''')
print(f'''A última letra A foi encontrada na posição {frase.rfind('A')}''')