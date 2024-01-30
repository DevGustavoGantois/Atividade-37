#Crie um programa que simule um sistema de votação. O programa deve permitir que os eleitores escolham entre opções de eleitores e conte os votos para cada opção.
#Use um dicionário para armazenar os resultados da votação, onde as chaves são as opções e os valores são o número de votos para cada opção. 
#O programa deve permitir que os eleitores votem, encerre a votação e exiba os resultados finais. Use While True e pare o programa
#somente se o usuário digitar o número 0 e exiba os resultados finais.

wishes = {}

while True:
    print("Options of wishes:")
    print("<------------------------>")
    print("Option A. 1")
    print("Option B. 2")
    print("Option C. 3")
    print("Option D. 4")
    print("Option E. 5")
    print("Finish the wishes. 0")

    vote_user = input('Enter your whise (Enter 0 for finish whises):')

    if vote_user == '0':
        break
    elif vote_user in ['1', '2', '3', '4', '5']:
        # Atualiza o dicionário de votos
        wishes[vote_user] =wishes.get(vote_user, 0) + 1
        print("Vote registered successfully!\n") 
    else:
        print("Invalid Option. Try again.\n") 

#Exibe os resultados finais.
print('\n Finals results of votes:')
for option, quantity_votes in wishes.items():
    print(f'Option {option}: {quantity_votes} votes.')
    
print("Vote finished. Thank you!!")


