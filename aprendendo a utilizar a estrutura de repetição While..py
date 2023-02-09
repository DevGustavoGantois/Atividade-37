par = 0
impar = 0
while n == 'Ss':
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
    else:
        impar += 1
print('Você digitou {} números pares e {} números impáres!'.format(par, impar))