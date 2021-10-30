from random import randint
from time import sleep
from typing import ParamSpec
itens = ('Pedra', 'Papel', 'Tesoura')
pc =  randint(0,2)
print(''''Suas opções:
0 - Pedra
1 - Papel
2 - Tesoura''')
jogador = int(input('Jogue:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!!!!')
sleep(1)
print('O PC jogou: {}'.format(itens[pc]))
print('Vc jogou: {}' .format(itens[jogador]))

if pc == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Vc ganhou!')
    elif jogador == 2:
        print('O PC ganhou!')
    else:
        print('Jogada Invalida')

if pc == 1:
    if jogador == 0:
        print('O PC ganhou!')
    elif  jogador == 1:
        print('Empatou!')
    elif jogador == 2:
        print('Voce ganhou!')
    else:
        print('Jogada invalida!')

if pc == 2:
    if jogador == 0:
        print('Voce ganhou!')
    elif jogador == 1:
        print('O PC ganhou!')
    elif jogador == 2:
        print('Empatou!')
      





