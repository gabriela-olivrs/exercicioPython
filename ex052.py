num = int(input("Numero:"))
tot = 0
for c in range (1 , num + 1):
    if num % c == 0:
     tot += 1
if tot == 2:
    print('Numero primo!')
else:
    print('Numero nao primo!')