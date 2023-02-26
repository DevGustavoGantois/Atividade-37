print('--')
print('>>'*40)
print('                                       ELEIÇÕES 2023                 ')
print('--'*40)
print('VOTAÇÃO.')
nasc = int(input('Em que ano você nasceu?'))
idade = 2023-nasc
if idade < 16:
   print('Não pode votar.')
elif idade >= 16 and idade < 18:
   print('Pode votar antecipadamente.')
elif idade >= 18 and idade <= 60:
   print('é obrigado a votar.')
else:
   print('Pode votar, mas não é obrigatório.')
print(' FIM DO PROGRAMA...')
