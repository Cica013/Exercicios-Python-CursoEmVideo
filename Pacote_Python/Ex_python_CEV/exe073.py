# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol,
# na ordem de colocação. Depois mostre:
# a) os 5 primeiros. b) Os ultimos 4 colocados. c) times em ordem alfabética.
# d) em que posição está o time da Chapecoense.
lista = ('Internacional', 'Atrlético Mineiro', 'São Paulo', 'Chapecoense', 'Vasco da Gama', 'Flamengo', 'Palmeiras',
         'Santos',
         'Fortaleza', 'Fluminense', 'Sport Recife', 'Ceará SC', 'Grêmio', 'Corinthians', 'Atlético-Go'
                                                                                         'Atlético-PR', 'Coritiba',
         'Bragantino', 'Botafogo', 'Bahia', 'Goiás')
print(f'Os 5 primeiros times são: {lista[:6]}')
print(f'Os últimos 4 colocados: {lista[-4:]}')
print(f'A tabela do brasileiro em ordem alfabética fica: {sorted(lista)}')
print(f"O time da Chapecoense está na posição: {lista.index('Chapecoense')+1}")
