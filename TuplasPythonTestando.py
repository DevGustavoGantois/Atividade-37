lanche = ('Hamburguer' , 'Suco',  'Pizza', 'Pudim' , 'Batata Frita')
#tuplas são imutaveis
for cont in range (0, len(lanche)):
    print(f'Eu vou comer pra caramba {lanche[cont]} na posição {cont}!')
#As duas formas são a mesma coisa...mas escritas de formas diferentes.
#Na forma de cima eu usei o RANGE e na de baixo eu usei diretamente a variável LANCHE.
#Tem momentos que será bom fazer na de baixo e tem momentos que será bom fazer na forma de cima.
#As duas funcionam igualmente!
for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi pra caramba!')