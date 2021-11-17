from random import randint
computador = randint(0 , 4)
acertou = False
contador = 0
while not acertou :
 num = int(input('pense em um numero de 0 a 5:'))
 contador += 1
 print('O numero sorteado foi {}'.format(computador))
 if num == computador:
     acertou = True
print('Você tentou {} vezes'.format(contador))


