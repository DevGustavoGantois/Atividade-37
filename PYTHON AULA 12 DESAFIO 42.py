print('                                                           ATIVDADE                                            ')
print('Mostre um triângulo e mostre qual tipo de triângulo ele irá formar.')
print('-------------------------------------------------------------------------')
print('                             TRIÂNGULOS.                                    ')
lado1 = int(input('Digite o valor do primeiro lado:'))
lado2 = int(input('Digite o valor do segundo lado:'))
lado3 = int(input('Digite o valor do terceiro lado:'))
print(' CALCULANDO OS VALORES...')
if lado1 == lado2 and lado3:
    print('O triângulo é EQUILÁTERO.')
elif lado1 == lado2 > lado3:
    print('O triângulo é ISÓSCELES.')
elif lado1 == lado2 < lado3:
    print('O triângulo é ISÓSCELES.')
elif lado2 == lado1 > lado3:
    print('O triângulo é ISÓSCELES.')
elif lado2 == lado1 < lado3:
    print('O triângulo é ISÓSCELES.')
elif lado3 == lado1 < lado2:
    print('O triângulo é ISÓSCELES.')
elif lado3 == lado1 > lado2:
    print('O triângulo é ISÓSCELES.')
elif lado1 < lado2 and lado1 < lado3:
    print('O triângulo é ESCALENO.')
elif lado1 > lado2 and lado1 > lado3:
    print('O triângulo é ESCALENO.')
