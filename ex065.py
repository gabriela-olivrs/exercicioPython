resp = 'S'
soma = 0
quantidade = 0
media = 0
while resp in 'Ss':
    num =  int (input('Digite um numero: '))
    quantidade +=1
    soma +=num
    if quantidade ==1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
media = soma / quantidade
print('A media é: {}'.format(media))
print('O maior valor foi {}, e o menor foi {}'.format(maior, menor))
print('Acabou')