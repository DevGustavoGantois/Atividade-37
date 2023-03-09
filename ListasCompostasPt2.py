teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
print(teste)
galera.append(teste)
print(galera)
#Gustavo 40 vai estar dentro de outra lista:
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
print(teste)
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
#Quando faço um append teste, estou fazendo uma ligação entre as 2 estruturas, então caso mude 
#a primeira estrutura que é o teste ele vai mudar a estrutura que é o galera.


#Então nesse caso teremos que fazer uma copia.
#Essa copia ira separar as 2 estruturas.
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
print(teste)
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
#podemos fazer dessa maneira:
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
#Caso mande mostrar só a galera 0
print(galera[0])
#Vai mostrar João, 19.
#Se eu botar:
print(galera[0] [0])
#Vai pegar somente o João que é o item 0 na posição 0 da lista.
#Se mostrar:
print(galera[2] [1])
#Ele irá mostrar a idade do joaquim, pois a chave está na posição 2 e o item 1 da posição 2 é 13
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera
print(p[0])
#Vai mostrar os nomes.
print(p[1])
#Vai mostrar as idades.


#Vai mostrar a lista formatada com os itens das listas dentro da lista maior.
print(f'{p[0]} tem {p[1]} anos de idade.')

#Pedir nome e idade
galera= list()
dado= list()
for c in range (0,3):
    dado.append(str(input('Nome:')))
    dado.append(str(input('Idade:')))
    galera.append(dado[:])
    dado.clear()

print(galera)
#Caso você esquecer disso [:] o programa irá dar clear em todo, ou seja, só terão listas vazias.
galera= list()
dado= list()
for c in range (0,3):
    dado.append(str(input('Nome:')))
    dado.append(str(input('Idade:')))
    galera.append(dado[:])
    dado.clear()
#Caso queira mostrar só as pessoas que tem 21 anos.
totmai = totmen = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')

