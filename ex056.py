
soma = 0
media = 0
MulherMenor20 = 0
maiorIdadeH = 0
HomemMaisVelho = ''
for i in range (0,4):
    nome = str(input('Digite seu nome:   '))
    idade = int(input('Idade:   '))
    sexo = str(input('F - Para Feminino\nM - Para Masculino   ')).upper()
    soma += idade
    
    if i == 1 and sexo == 'M':
        maiorIdadeH = idade;
        HomemMaisVelho = nome
    #GUSTAVO USO IN 'Mm' Para aceitar os dois valores
    if sexo == 'M' and idade > maiorIdadeH:
        maiorIdadeH = idade;
        HomemMaisVelho = nome

    if sexo == 'F' and idade < 20:
        MulherMenor20 += 1

media = soma / 4
print('Media: {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeH, HomemMaisVelho))
print('{} Mulheres tem menos de 20 anos '.format(MulherMenor20))
