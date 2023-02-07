print('                                                          ATIVIDADE                         ')
print('=================================================================================================')
print('Crie um programa que leia uma frase qualquer e diga se ela é um palidromo, desconsiderando os espaços. Exemplos')
print('de palindromos:')

print('APOS A SOPA.')

print('A SACADA DA CASA.')

print('A TORRE DA DERROTA.')

print('O LOBO AMA O BOLO.')

print('ANOTARAM A DATA DA MARATONA.')
print('==============================================================================================================')
frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto =''.join(palavras)
inverso =''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
