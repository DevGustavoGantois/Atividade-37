nome = str(input('Qual é o seu nome?'))
if nome == 'Gustavo':
    print('Que nome bonito!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Matheus':
    print('Seu nome é menos feio que os demais...')
elif nome in 'Ana':
    print('Nossa o seu nome é muito acima da média.')
else:
    print('Seu nome é bem feio...')
print('Tenha um bom dia {}.'.format(nome))