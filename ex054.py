from datetime import date
maiorIdade = 0
menorIdade = 0

for i in range(0,6):
    idade = date.today().year - ano
    ano = int(input('Ano Nascimento:'))
    if (idade >= 21):
       maiorIdade+=1
    else:
        menorIdade+=1
print('{} pessoas sao maior(es) de idade e {} pessoas são menor(es) de idade:'.format(maiorIdade, menorIdade))




