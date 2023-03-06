print("""=========================================ATIVIDADE==============================================================
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-se em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem
crescente.""")
print('=='* 60)
#totvalores
#valorexistente
valores = []
while True:
    numeros = int(input('Digite um valor:'))
    if numeros not in valores:
        valores.append(numeros)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado. Não vou adicionar, tente novamente')
    pergunta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if pergunta == 'N':
        break
print('=-'*40)
print(f'Você digitou os valores {valores}.')