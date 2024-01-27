#Suponha que você está gerenciando uma competição esportiva e tem
#uma lista de tuplas representando os resultados das equipes em
#diferentes modalidades. Cada tupla contém o nome da equipe, seguido
#por uma lista de pontuações obtidas em cada rodada da competição.

#1.Calcule a média das pontuações de cada equipe e armazene esses
#valores em uma nova lista chamada medias.
#2.Ordene a lista medias em ordem decrescente.
#3.Crie uma nova lista chamada classificacao que contém tuplas, onde
#cada tupla contém o nome da equipe e sua média de pontuações.
#4.Exiba na tela a classificação final das equipes, mostrando o nome da
#equipe e sua média, da equipe com a pontuação mais alta para a
#mais baixa.

teams_results = [('Team A', [12, 4, 3]),
                 ('Team B', [11, 8, 2]),
                 ('Team C', [14, 6, 1]),
                 ('Team D', [5, 7, 2]),
                 ('Team E', [7, 8, 1]),
]

average = [(teams, sum(points) / len(points)) for teams, points in teams_results]

average.sort(key=lambda x: x[1], reverse=True)

classification = [(teams, avg) for teams, avg in average]

for position, (teams, avg) in enumerate(classification, start=1):
    print(f"{position}. {teams}: {avg:.2f} points.")
