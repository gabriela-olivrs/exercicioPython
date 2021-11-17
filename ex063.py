quantidade = int(input('Quantos numeros voce deseja exibir?'))
primeiro = 0;
segundo = 1;
print('{}'.format(primeiro , segundo ), end=' ')
cont = 2;

while cont <= quantidade:
    terceiro = primeiro + segundo;
    primeiro = segundo;
    segundo = terceiro;
    print('{}'.format(terceiro ), end=' ')
    cont+=1
print('Fim')


