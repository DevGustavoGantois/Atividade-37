#Faça um programa que solicite ao usuário que digite 10 valores para
#preencher uma lista. Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.

listaDeNumeros=[]
listaPares=[]
listaImpares=[]

for i in range(10):
    numeros=int(input(f"Digite o valor {i + 1}:"))
    listaDeNumeros.append(numeros)
    if numeros % 2 == 0:
        listaPares.append(numeros)
    else:
        listaImpares.append(numeros)

soma = sum(listaDeNumeros)
print(f"A lista de números é = {listaDeNumeros}")
print(f"Os números pares são = {listaPares}")
print(f"Os números ímpares são = {listaImpares}")
print(f"A soma de todos os números pares e ímpares é = {soma}")