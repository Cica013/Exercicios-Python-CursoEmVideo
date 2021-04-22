# Leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número inteiro: '))
primo = 0
for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[31m{c}\033[m', end=' ')
        primo += 1
    else:
        print(f'\033[32m{c}\033[m', end=' ')
print()
if primo > 2:
    print('O número não é primo.')
else:
    print('O número é primo.')
