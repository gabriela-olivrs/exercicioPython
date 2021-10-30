r1= float(input('reta 1:'))
r2= float(input('reta 2:'))
r3= float(input('reta 3:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 :
    if r1 == r2 == r3:
        print('Pode formar um triangulo equilatero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Pode formar um triangulo isoceles')
    elif r1 != r2 != r3:
        print('Pode formar um triangulo escaleno')
else:
    print ('Os seguimentos informados nao pode formar um triangulo')


