maior = 0
menor = 0

for i in range (0,5):
    peso = int(input('Qual o peso Kg:'))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso é: {} kg, enquanto o menor peso é: {} kg'.format(maior, menor))     
    