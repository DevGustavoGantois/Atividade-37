from calc import *
print('==============> SEJA BEM VINDO A CALCULADORA ELETRÔNICA <=============')
print('Escolha a opção que você deseja realizar:')
print('Digite 1 para somar.')
print('Digite 2 para subtrair.')
print('Digite 3 para multiplicar.')
print('Digite 4 para dividir.')
print('Digite 5 para exponenciar.')
print('##'*40)

menu = int(input('Digite uma opção:'))
while True:
    if menu == '0':
        break
    elif menu == '1':
        a = int(input('Digite o primeiro valor:'))
        b = int(input('Digite o segundo valor:'))
        print(soma(a, b))
        resp = str(input('Quer continuar? [S/N]')).strip().upper()
        resp == 'N'
        break
    elif menu == '2':
         a = int(input('Digite o primeiro valor:'))
         b = int(input('Digite o segundo valor:'))
         print(subtracao(a, b))
         resp = str(input('Quer continuar? [S/N]')).strip().upper()
         resp == 'N'
         break
    elif menu == '3':
         a = int(input('Digite o primeiro valor:'))
         b = int(input('Digite o segundo valor:'))
         resp = str(input('Quer continuar?[S/N]')).strip().upper()
         resp == 'N'
         break
    elif menu == '4':
        a = int(input('Digite o primeiro valor:'))
        b = int(input('Digite o segundo valor:'))
        resp = str(input('Quer continuar? [S/N]')).strip().upper()
        resp == 'N'
        break
    elif menu == '5':
        a = int(input('Digite o primeiro valor:'))
        b = int(input('Digite o segundo valor:'))
        resp = str(input('Quer continuar? [S/N]')).strip().upper()
        resp == 'N'
