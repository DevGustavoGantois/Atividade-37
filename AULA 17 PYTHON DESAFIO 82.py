print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-ATIVIDADE-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print("""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final
mostre o conteúdo das três listas geradas. """)
print('-='*40)
numeros = []
numerospares = []
numerosimpares = []
while True:
    numeros.append(int(input('Digite um número:')))
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()
    if resposta in 'N':
        break
for i, p in enumerate(numeros):
    if p % 2 == 0:
        numerospares.append(p) 
    elif p % 2 == 1:
        numerosimpares.append(p) 
print(f'Os valores da lista são {numeros}.')
print(f'Os valores pares lista {numerospares}.')
print(f'Os valores impares lista {numerosimpares}.') 

