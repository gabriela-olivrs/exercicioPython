precoNormal = float(input('Preço: R$'))

print('DIGITE:\n 1 - Para pagamento a vista\n 2 - Para pagamento a vista no cartao')
print('3 - Para pagamento em até 2x no cartao\n 4 - Para pagamento em 3x ou mais no cartao')

opcao = int(input())

if opcao == 1:
    print('Voce tera 10% de desconto e pagara {}' .format(precoNormal- (0.10*precoNormal)))
elif opcao == 2:
    print('Voce tera 5% de desconto e pagara {}'. format(precoNormal - (0.05 * precoNormal)))
elif opcao == 3:
    print('Voce pagara o preco normal de {}' . format(precoNormal))
else:
    print('Voce pagara juros de 20%, resultando em um montate de {}' . format(precoNormal + (0.20 * precoNormal)))