print('-=-'*30)
print('                                                         ATIVIDADE                             ')
print('-=-'*30)
print('Crie um programa que leia o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o ')
print('usuário quer ou não continuar. No final, mostre:')

print('A) Quantas pessoas tem mais de 18 anos.')

print('B) Quantos homens foram cadastros.')

print('C) Quantas mulheres tem menos de 20 anos')
print('-=-'*30)
Tot18 = totH = totM20 = 0
while True:
    print('=='*20)
    print('CADASTRE UMA PESSOA.')
    print('=='*20)
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
    if idade >= 18:
        Tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {Tot18} ')
print(f'Ao todo temos o {totH} homens cadastrados')
print(f'E temos o total de {totM20} mulheres com menos de 20 anos.')




