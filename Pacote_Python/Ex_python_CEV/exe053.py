# Criem um programa que leia uma frase e diga se ela é um palíndromo. Desconsiderando espaços.
frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(frase)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('A frase não é um palíndromo.')
    