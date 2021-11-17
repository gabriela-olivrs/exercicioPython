c = False
while not c:
 print('________________________________#####____________________________________')

 numero1 = float(input('Inserir o primeiro numero:  '))
 numero2 = float(input('Inserir o segundo numero:  '))
 opcao = int(input('1: Para soma\n2: Para subtração\n3: Para multiplicação\n4: Para divisao\n5: Sair  '))
 if opcao == 1:
    print(numero1 + numero2)
 elif opcao == 2:
    print(numero1 - numero2)
 elif opcao == 3:
    print(numero1 * numero2)
 elif opcao == 4:
    print(numero1 / numero2)
 elif opcao == 5:
    c = True
 else:
    print('Opcao Invalida')

print('Fim do programa! Obrigada, volte sempre')

