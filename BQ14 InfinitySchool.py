print('                                  ATIVIDADE.')
print('=='*40)
print('Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:')
print('- Telefonou para a vítima?')
print('- Esteve no local do crime?')
print('- Mora perto da vítima?')
print('- Devia para a vítima?')
print('- Já trabalhou com a vítima?')
print('-------------------------------------------------------------------------------------------')
print('O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa')
print('responder positivamente a 2 questões ela deve ser classificada como suspeita, entre 3 e 4 como Cúmplice e 5 como')
print('Assassino. Caso o contrário, ele será classificado como inocente.')
print('=='*50)
pergunta1 = str(input('-Telefonou para a vítima?')).strip().title()
pergunta2 = str(input('-Esteve no local do crime?')).strip().title()
pergunta3 = str(input('-Mora perto da vítima?')).strip().title() 
pergunta4 = str(input('Devia para a vítima?')).strip().title()
str(input('Já trabalhou com a vítima?')).strip().title()
resposta = 0
if pergunta1 == 'Sim':
  resposta += 1
if pergunta2 == 'Sim':
  resposta += 1
if pergunta3 == 'Sim':
  resposta += 1
if resposta == 2 or resposta == 3:
  print('Culpado!')
if pergunta4 == 'Sim':
  resposta = 5
  print('Assassino!')
else:
  print('Não é culpado!')