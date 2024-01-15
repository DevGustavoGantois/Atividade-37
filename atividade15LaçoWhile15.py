#Desenvolva um programa que 
#faça a tabuada de um número qualquer 
#inteiro que será digitado pelo usuário, mas 
#a tabuada não deve necessariamente iniciar em 1 e 
#terminar em 10, o valor inicial e final devem ser informados também pelo usuário, 
#conforme exemplo abaixo

#Montar a tabuada de: 5 -> Começar por: 4 e Terminar em: 7

#5 X 4 = 20 
#5 X 5 = 25 
#5 X 6 = 30 
#5 X 7 = 35 

#Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

inicio_da_Tabuada=int(input("Digite o número inicial da tabuada:"))
final_da_Tabuada=int(input("Digite o número final da tabuada:"))

while final_da_Tabuada < inicio_da_Tabuada:
    print("Programa encerrado, não é possível fazer essa operação...")
    inicio_da_Tabuada=int(input("Digite o número inicial da tabuada:"))
    final_da_Tabuada=int(input("Digite o número final da tabuada:"))

else:
    for i in range(inicio_da_Tabuada, final_da_Tabuada + 1):
        print(f"{inicio_da_Tabuada} * {i} = {inicio_da_Tabuada * i}")