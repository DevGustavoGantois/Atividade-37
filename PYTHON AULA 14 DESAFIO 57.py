print('                                                            ATIVIDADE                              ')
print('========================================================================================================')
print('Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a')
print('digitação novamente até ter um valor correto.')
print('--------------------------------------------------------------------------------------------------------------')
sexo = str(input('Informe o seu Sexo [M/F]:')).strip().upper()[0]
while sexo not in 'MmFf':
            sexo = str(input('Dados inválidos ,por favor, informe seu sexo ->')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

