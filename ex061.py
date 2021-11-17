pTermo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razao:'))
an = pTermo 
i = 1
while i <= 10:
    print('{}->'.format(an), end='')
    an+=razao
    i+=1
print('End')



