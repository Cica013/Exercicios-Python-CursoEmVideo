# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até um valor válido.
condição = False
while condição == False:
    sexo = str(input('Digite o sexo (M/F): ')).strip().upper()
    if sexo != 'F' and sexo != 'M':
        print('Você digitou algo de errado. Digite (F) Ou (M) para escolher o sexo.')
    else:
        condição = True
if sexo == 'F':
    print('O sexo escolhido foi FEMININO.')
elif sexo == 'M':
    print('O sexo escolhido foi MASCULINO.')
print('FIM!')