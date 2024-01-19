#Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes. (Use laços de repetição)

#Lista de caracteres
char_list=['a','b','c','d','e','f','g','h','i','j']

#Inicializa o contador das consoantes
consonant_count=0

#Lista para armazenar as consoantes:
consonants=[]
#Loop para verificar cada caractere:
for char in char_list:

    if char.lower() not in ['a','e','i','o','u']:
        consonant_count+=1
        consonants.append(char)

#Imprime o número de consoantes e as consoantes encontradas:
        print('Number of consonants:', consonant_count)
        print('Consonants ->', consonants)