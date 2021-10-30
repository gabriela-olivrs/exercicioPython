#an = a1 + (n-1)*r
pTermo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razao:'))
an = pTermo + (10 - 1) * razao
for c in range(pTermo , an + razao , razao):
    print(c, end='-> ')
    