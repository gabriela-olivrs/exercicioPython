valorCasa = float(input('Qual valor da casa? R$:'))
salario = float(input('Qual seu salario? R$:'))
tempo = int(input('Em quantos anos deseja pagar?'))
prestacaoMensal = valorCasa/(tempo * 12)

if prestacaoMensal <= (0.30*salario):
    print('Empréstimo Concedido!!!')

    print('Para pagar uma casa de {:.2f} em {} anos cada prestacao tera valor de: R$ {}'.format(valorCasa, tempo, prestacaoMensal))
else:
    print('Emprestimo Negado!!!')







