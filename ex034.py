salario = float(input('Salário:'))
if salario>1250.00:
    print('O aumento sera de 10% e voce recebera R$:{}'. formar(salario + (0.10*salario)))
else:
    print('O aumento sera de 15% e voce recebera R$:{}'.format(salario + (0.15*salario)))
    

