n = int(input('Digite um número para calcular o Fatorial:'))
C = n
f = 1
print('Calculando {}!'.format(n), end='')
while C > 0:
    print('{} x '.format(C), end='')
    print(' x ' if C > 1 else ' = ', end='')
    f *= C
    C -= 1
print('{}.'.format(f))