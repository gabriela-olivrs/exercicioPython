from random import random
from time import sleep
num = int(input('pense em um numero de 0 a 5:'))
num2 = int(random())
print('Processando...')
sleep(3)
print('O numero sorteado foi {}'.format(num2))
if num == num2:
    print('Você venceu!!!!')
else:
    print('Voce perdeu...')

