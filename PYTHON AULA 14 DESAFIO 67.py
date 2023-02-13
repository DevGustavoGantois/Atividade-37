print('-=-'*40)
print('                                           ATIVIDADE                              ' )
print('-=-'*40)
print('Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.')
print('O programa será interrompido quando o número solicitado for negativo.')
print('-=-'*40)
numero = 0
while True != 10:
    print('--'*30)
    numero = int(input('Quer ver a tabuada de qual valor?'))
    if numero < 0:
        break
    print('--'*30)
    for c in range(1, 11):
        print(f'{numero}x{c} = {numero*c} ')
print('PROGRAMA TABUADA ENCERRADA. Volte sempre!')
