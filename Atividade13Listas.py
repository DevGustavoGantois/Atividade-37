#com intuito de organizar o pasto, o fazendeiro que andava estudando a linguagem Python queria fazer um arranjo em sua fazenda  usando o método de listas, sabendo disso ajude o agrônomo a realizar essa mudança. Levando em consideração que no pasto 1 (que também é uma lista)tem  4 listas com um animal diferente em cada(animais da sua escolha)e dentro dessas listas havia 4 cores de animais(cores da sua escolha porém sempre diferentes),faça um código responsável por mudar 3 listas de animais do pasto 1 para o pasto 2 que estava vazio e imprimindo o resultado final dos animais do pasto 2 e os animais do pasto 1 
#Exemplo de lista de animal:zebras=['zebras=',"branca","bege","preta"],
#OBS :Use as funções de manipulação de listas 

pasto_um=[
    ['zebras=', 'branca', 'preta', 'verde', 'verde'],
    ['galinhas=', 'vermelho', 'roxo', 'laranja', 'amarelo'],
    ['ovelhas=', 'cinza', 'lilas', 'rosa', 'azul claro'],
    ['vacas=', 'marrom', 'dourado', 'verde escuro', 'rosa choque']
]

pasto_dois=[]

for _ in range(3):
    animal=pasto_um.pop()
    pasto_dois.append(animal)

print("Animais do pasto 1:")
for animal in pasto_um:
    print(animal)
print('\n Animais do pasto 2:')
for animal in pasto_dois:
    print(animal)