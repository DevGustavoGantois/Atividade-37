print('-=-'* 40)
print('                                                      ATIVIDADE                           ')
print('-=-'*40)
print('Leia o primeiro termo da razão de uma PA, mostrando os 10 primeiros termos de progressão. E pergunte ao usuário')
print('se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.')
print('-=-'*40)
primeiro = int(input('Qual o primeiro termo?'))
razao = int(input('Qual a razão da PA:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} termos mostrados.'.format(total))





