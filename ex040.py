nota1 = float(input('nota 1:'))
nota2 = float(input('nota 2:'))

media = (nota1 + nota2)/2

if media < 5.0:
    print('Reprovado')
elif media >= 5.0 and media <= 6.9:
    print('Recuperacao')
else:
    print('Aprovado')

