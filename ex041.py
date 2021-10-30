from datetime import date
anoNascimento =  int(input('Ano de Nascimento do atleta:'))
atual = date.today().year
idade = atual - anoNascimento

if idade <= 9 :
    print('Idade: {} Categoria: Mirim'.format(idade))
elif idade <= 14:
    print('Idade: {} Categoria: Infantil'.format(idade))
elif idade <= 19:
    print('Idade: {} Categoria: Junior'.format(idade))
elif idade <= 20:
    print('Idade: {} Categoria: Senior'.format(idade))
else:
    print('Idade: {} Categoria: Master'.format(idade))