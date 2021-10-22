frase = str(input('Digite uma frase qualquer:')).strip().upper()
palavra = frase.split()
join = ''.join(palavra)

inverso = ''

for i in range (len(join) -1, -1, -1):
    inverso += join[i]

if(join == inverso):
    print('É palindromo')
else:
    print('Não é palindromo')

    #SPLIT GERA UMA LISTA E JOIN JUNTA A LISTA TIRANDO O ESPAÇO
    #SEM USAR O FOR PODEMOS UTILIZAR A ESTRUTURA INVERSO[::-1]
