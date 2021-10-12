num1 = float(input('num1:'))
num2 = float(input('num2:'))
num3 = float(input('num3:'))
if (num1>num2)&(num1>num3):
    print('O maior numero é {}'.format(num1))
if (num2>num1)&(num2>num3):
    print('O maior numero é {}'.format(num2))
else:
    print('O maior numero é {}'.format(num3))

    #menor
if((num1<num2)&(num1<num3)):
    print('O menor numero é {}'.format(num1))
if((num2<num1)&(num2<num3)):
    print('O menor numero é {}'.format(num2))
else:
    print('O menor numero é {}'.format(num3))

