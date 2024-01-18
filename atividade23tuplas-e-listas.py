#Faça um programa que leia os nomes dos 3 nadadores que subirão ao pódio na ordem do primeiro
#colocado para o terceiro. Imprima na tela a posição do nadador e seu nome.

swimmers = []

#Leitura dos nomes dos nadadores
for i in range(3):
    names = input(f"Swimmer {i + 1} ->")
    swimmers.append(names)

#Ordenação dos nadadores
swimmers = sorted(enumerate(swimmers, start = 1), key=lambda x: x[1])

#Impressão na tela da posição do nadador e seu nome

for position, name in swimmers:
    print(f"Position: {position}: {name}.")

