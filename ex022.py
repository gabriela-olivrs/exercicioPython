nome = str(input("Nome completo:")).strip()
print('Com todas as letras maiúsculas: {}'. format(nome.upper()))
print('Com todas as letras minúsculas: {}'. format(nome.lower()))
print('Quantas letras sem espaço {}'. format(len(nome.replace(' ', ''))))
print('Quantas letras tem o primeiro nome {}:'.format(nome.find(' ')))

#o .strip retira os espaços antes e depois
#o. find conta ate o primeiro espaço