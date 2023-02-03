print('Aprendendo a usar (if:) e (else:) aula 10 ')
print('===========================================')
print('===========================================')
nome = str(input('Digite um nome:'))
print('Prazer em te conhecer' , nome)
if nome == 'Nayra':
    print('nossa seu nome é muito bonito!!'.format(nome))
    print('Bom dia {}'.format(nome))
else:
    print('nossa seu nome é tão feio...'.format(nome))
    print('Bom dia {}'.format(nome))

print('==============================================================================================================')
print('Outra atividade teste, testando a estrutura...')
print('===============================================================================================================')
print('CALCULANDO A MÉDIA DE UM ALUNO:')
aluno1 = float(input('Qual a nota do primeiro aluno?'))
aluno2 = float(input('Qual a nota do segundo aluno?'))
aluno3 = float(input('Qual a nota do terceiro aluno?'))
aluno4 = float(input('Qual a nota do quarto aluno?'))
print('============================================')
print(' O primeiro aluno tirou:' , aluno1)
print('O segundo aluno tirou:' , aluno2)
print('O terceiro aluno tirou: ', aluno3)
print('O quarto aluno tirou:' , aluno4)
nota = (aluno1 + aluno2 + aluno3 + aluno4)//4
print(' Se o aluno tirou mais de 6.0 ele vai passar de ano ')
print(' Se o aluno tirou abaixo de 6.0 ele não vai passar de ano')
if nota >= 6.0:
    print('PARABÉNS VOCÊ PASSOU DE ANO E ESTÁ APTO(A) PARA IR PARA PRÓXIMA SÉRIE!' .format(nota))
else:
    print('VOCÊ REPROVOU POIS SUA NOTA FOI ABAIXO DE 6.0 E TERÁ QUE REPETIR DE ANO...')

print('==========================Estrutúras de teste concluídas!================================================')


