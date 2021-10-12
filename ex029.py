velocidade = float(input('Informe a velocidade:'))
if velocidade > 80:
    print('Voce foi multado...')
    print('O valor da multa é de: {:0.2f}'.format((velocidade-80)*7.00))

else:
    print('Voce esta dentro do limite!')
