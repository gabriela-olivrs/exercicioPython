distancia = float(input('Informe a distancia em km:'))
if distancia <= 200:
    print('Voce pagara: {:0.2f}'.format(distancia * 0.50))
else:
    print('Voce pagara: {:0.2f}'. format(distancia * 0.45))