# Faça um programa que leia quanto a pessoa tem na carteira de mostre quantos dólares ela pode comprar.
# Considerando que 1 dólar está 3,27 R$.
carteira = float(input('Digite aqui quantos reais você tem na sua carteira: '))
conversão = carteira / 3.27
print(f'Com o que você tem na carteira você pode comprar {conversão:.2f} Dólares.')