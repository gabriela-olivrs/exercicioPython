num =  int(input ('Digite o numero desejado:'))

print('Escolha\n 1 - para binario\n 2 - para octal\n 3 - para hexadecimal ')

opcao = int (input('opcao:'))
if opcao == 1:
    print('O número em binario é: {}'.format(bin(num)[2:]))
elif opcao == 2:
    print('O número em octal é: {}'.format(oct(num)[2:]))
elif opcao == 3:
   print('O numero em hexadecimal é: {}'.format(hex(num) [2:]))
else:
    print ('Opcao invalida!')


    