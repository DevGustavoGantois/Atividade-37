print('Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.')
print('Ex:Ana Maria de Souza ')
print('Primeiro: Ana')
print('úlitmo: Souza')
print('=========================================================================================================================')
print('==========================================================================================================================')
PS = str(input('Digite seu nome:')).strip()
nome = PS.split()
print('Muito prazer em te conhecer!' , nome)
print('Primeiro nome é : {} ' .format(nome[0]))
print('Ultimo nome é : {}'.format(nome[len(nome)-1]))