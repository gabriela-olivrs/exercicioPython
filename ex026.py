frase = str(input('Digite uma frase:')).strip().lower()
print('A quantidade de letra(s) A é igual a {}'.format(frase.count('a')))
print('A primeira letra A aparece na posição: {}'.format(frase.find('a')+1))
print('A última ocorrência de A apareceu na posição:{}'.format(frase.rfind('a')+1))

