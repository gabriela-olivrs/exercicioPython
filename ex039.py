from datetime import date

anoNasc = int(input('Ano nascimento:'))

anoAtual = date.today().year

idade = anoAtual - anoNasc

if idade < 18:
  print('Voce ainda vai se alistar, para isso aguarde {} anos'. format(18 - idade))

elif idade == 18:
    print('Ja esta na hora de se alistar!')

else:
    print('Ja passou {} anos do tempo de alistamento!'.format(idade - 18))


