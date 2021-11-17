primeiro_numero = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razao:'))
numero = primeiro_numero
contador = 1
contador2 = 1
while contador <= 10:
    print('{} '.format(numero), end=' ')
    numero+=razao
    contador+=1
numeros_a_mais = int(input('Voce deseja imprimir mais quantos numeros?'))
while numeros_a_mais != 0:
    while contador2 <= numeros_a_mais:
        print('{}->'.format(numero), end='')
        numero+=razao
        contador2+=1
    numeros_a_mais = int(input('Voce deseja imprimir mais quantos numeros?'))

print('End')