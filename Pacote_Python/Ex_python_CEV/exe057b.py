# Faça um programa que leia o sexo de uma pessoa, mas só aceite 'F' ou 'M'.
# Caso esteja errado peça a digitação novamente até ter um valor correto.
sexo = str(input('Digite seu sexo (M/F): ')).strip()[0]
while sexo not in 'MmFf':
    print('Você digitou algo de errado.')
    sexo = str(input('Digite novamente seu sexo (M/F):'))
if sexo in 'Ff':
    print('O sexo escolhido foi FEMININO.')
elif sexo in 'Mm':
    print('O sexo escolhido foi MASCULINO.')
print('FIM!')