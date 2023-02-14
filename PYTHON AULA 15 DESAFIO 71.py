print('>>>'*30)
print('                                                    ATIVIDADE')
print('>>>'*30)
print('Crie um programa que simule o funcionamneto de um caixa eletrônico. No início, pergunte ao usuário qual será o ')
print('valor a ser sacado (número inteiro ) e o programa vai informar quantas cédulas de cada valor serão entregues.')
print('OBS.')

print('Considere que o caixa possui cédulas de R$50 R$20 R$10 R$1.')
print('----'*30)
print('^^'*50)
print('                                               BANCO DA TREMBOLONA    ')
print('^^'*50)
print('>>>'*30)
valor = int(input('Qual o valor você sacar? R$'))
print('>>>'*30)
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de {ced}R$')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
            totced = 0
        if total == 0:
            break
print('>>>'*30)
print('Volte sempre ao BANCO TREMBOLONA. Tenha um excelente dia!')