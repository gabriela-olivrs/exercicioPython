sexo = str(input("Sexo:")).strip().upper()[0]
while sexo not in 'MmFf':
 sexo = str(input('Digitação incorreta, tente novamente! Sexo:')).strip().upper()[0]
print('O sexo iformado é: {}'.format(sexo))