numero = int(input('Digite um numero para ser somado ao total ou digite 999 para parar:'))
cont = 0;
total = 0;
while numero != 999 :
    total +=numero;
    cont += 1
    numero = int(input('Digite um numero para ser somado ao total ou digite 999 para parar:'))
print('Voce digitou {} numeros e a soma entre eles equivale a {}'.format(cont, total))




