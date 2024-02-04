#REVISÃO DAS ATIVIDADES:
#1.Crie um conjunto vazio chamado frutas e adicione as
#seguintes frutas a ele:
#"maçã","banana","uvas","laranja"e"morango". Em seguida, imprima o conjunto.

fruits = set()

fruits.add('Apple')
fruits.add('Banana')
fruits.add('Grapes')
fruits.add('Orange')
fruits.add('Strawberry')
print(fruits)

#2. Verifique se a fruta"banana"está presente no conjunto frutas e imprima o resultado.

fruits2 = {"Apple", "Banana", "Grapes", "Orange" , "Strawberry", "Cherry"}

print('Banana' in fruits2)

#3. Crie um conjunto chamado frutas_vermelhas e 
#adicione as seguintes frutas a ele:"morango","cereja"e
#"framboesa". Em seguida, imprima o conjunto.

red_fruits = set()
red_fruits.add('Strawberry')
red_fruits.add('Cherry')
red_fruits.add("raspberry")
print(red_fruits)

#4.Remova a fruta "cereja
#" do conjunto frutas_vermelhas e imprima o conjunto atualizado.

red_fruits2 = {"Strawberry", "Cherry", "raspberry"}
red_fruits2.remove('Cherry')
print(red_fruits2)

#5.Crie dois conjuntos, A e B, e realize a união dos dois 
#conjuntos.

set1 = {'Name1': 
        "Gustavo", 
        'Age1': 20, 
        'State1': 'BA', 
        'City1': 'Salvador'  }

set2 = {'Name2':
        "Duda",
        'Age2': 16,
        'State2':'BA',
        'City2': 'Salvador' }

print(set1 | set2)

#6.Crie um programa que recebe dois conjuntos e exibe a
#interseção deles.

set_intersection1={'Gustavo', 'Maria', 'Lucas', 'Felipe', 'Jorge', 'Junior', 'Matheus', 'Luan'}
set_intersection2={'Maria', 'Lucas', 'Matue', 'Teto', 'Bruno', 'Breno', 'Gustavo', 'Junior'}

result_intersection = set_intersection1.intersection(set_intersection2)
print(result_intersection)

#7.Escreva um programa que receba duas listas e calcule a união dos elementos únicos dessas listas, usando conjuntos.

def union_calculate(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    union_sets = set1.union(set2)

    union_list = list(union_sets)

    return union_list

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2 = [21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]

result_union_lists = union_calculate(list1, list2)
print(result_union_lists)

#8.Escreva um programa que percorra um dicionário contendo informações de pessoas (nome, idade) e exiba essas informações.

informations_people= {
    'Name1': 'Gustavo',
    'Age1': 20,
    'Name2': 'Nayra',
    'Age2': 55,
    'Name3': 'Augusto',
    'Age3': 58,
    'Name4': 'Billy',
    'Age4': 12
}

for key in informations_people.keys():

    if 'Name' in key:
        name_key = key

        age_key = key.replace('Name', 'Age')
        
print(f"The Name is -> {informations_people[name_key]} and Age is -> {informations_people[age_key]}.")

#9.Escreva um programa que percorra as chaves e valores de um dicionário separadamente e os exiba.

dictPeople = {
    'Name': 'Claudio',
    'Age': 60 ,
    'State': 'Paraíba',
    'City': 'João Pessoa',
}


for key_information in dictPeople: #podemos exibir os valores de forma simultanea usando um for key information, value_information in dicPeople. 
                                   #Exibir o print(f"key:{key_information}:{value_information}}"  
    print(key_information)

for value_information in dictPeople.values():
    print(value_information)


#10.Crie um programa que exiba os itens exclusivos de dois dicionários. Itens exclusivos são aqueles que não estão presentes em ambos os dicionários.


#Criando as chaves e valores do dicionário 1:
dict1 = {
    'Car1': 'Rolls Roice',
    'Car2': 'Ferrari',
    'Car3': 'Bugatti',
    'Car4': 'Audi',
    'Car5': 'BMW',
    'Car6': 'Mercedes'
}
#Criando as chaves e valores do dicionário 2:
dict2 = {
    'Car7': 'Fiat',
    'Car8': 'Gol',
    'Car9': 'Rolls Roice',
    'Car10': 'Ferrari',
    'Car11': 'Chevrolet',
    'Car12': 'BMW'
}

#Convertendo as chaves dos dicionários em conjuntos
exclusive_keys = set(dict1.keys()).symmetric_difference(set(dict2.keys()))
exclusive_values = set(dict1.values()).symmetric_difference(set(dict2.values()))
print('Exclusive Items:')

if exclusive_keys or exclusive_values:
    for keys_items in exclusive_keys:
        print(f'Keys: {keys_items}')
    for value_items in exclusive_values:
        print(f'Values: {value_items}')

#11.Desenvolva um programa que recebe um dicionário, uma chave e um valor como entrada e adiciona a chave e o valor ao dicionário, atualizando o valor se a chave já existir.

def receive_updating_dictionary(dictionary, value, key):
    
    dictionary[key] = value

my_dictionary = {'Name': 'Gustavo', 'Age': 20, 'State': 'BA', 'City': 'Salvador'}

new_key = input("Enter a new Key:")
new_value = input("Enter a new Value:")

receive_updating_dictionary(my_dictionary, new_key, new_value)

print(f"Updating dictionary:", my_dictionary)

#12.Escreva um programa que recebe um dicionário e uma
#lista de chaves como entrada e verifica se todas as chaves da lista existem no dicionário. A função deve retornar True se todas as chaves existirem e False caso contrário.
def verify_keys_in_dictionary(dictionary, list_key):
    
    return all(key in list_key for key in dictionary)

my_dictionary = {'Bahia': 'Salvador', 'Rio Grande do Sul': 'Gramado', 'São Paulo': 'Guarulhos', 'Santa Catarina': 'Florianopolis'}
my_list = ['Bahia', 'Rio Grande do Sul', 'São Paulo', 'Santa Catarina']

result_verify = verify_keys_in_dictionary(my_dictionary, my_list)
print(result_verify)


#13.Crie um programa que simule um sistema de votação. O programa deve permitir que os eleitores escolham entre
#opções de eleitores e conte os votos para cada opção. Use um dicionário para armazenar os resultados da
#votação, onde as chaves são as opções e os valores são o número de votos para cada opção. O programa deve permitir que os eleitores votem, encerre a votação e exiba 
#os resultados finais. Use While True e pare o programa somente se o usuário digitar o número 0 e exiba os resultados finais.

votes_results = {}

while True:
    vote = input("Enter your vote (Enter 0 to end the votes):")

    if vote == '0':
        print("Finished votes.")
        break
    if vote in votes_results:
        votes_results[vote] += 1
    else:
        votes_results[vote] = 1

print('Final results:')

for options, vote in votes_results.items():
    print(f'Options: {options}, {vote} votes.')

#14.Crie um dicionário que relacione nomes de alunos às suas notas em uma disciplina. Calcule a média das notas e exiba-a.

name_students= {
    'Gustavo': 80,
    'Luan': 60,
    'Gabriel': 55,
    'Jorge':45,
    'Augusto': 100,
    'Renato': 30
}


total_notes = sum(name_students.values())
average_notes_students = total_notes / len(name_students)


for name, note in name_students.items():
    print(f'\nStudent ->{name}:{note}')


print(f"The total notes of students: {average_notes_students:.2f}")

#15.Crie um programa que receba uma lista de números e remova todas as duplicatas usando um conjunto (set). Em seguida, exiba a lista original e a lista sem duplicatas.

my_list = set()

while True:
    response_list = input("Hello User! Enter a number (type 'Finished for finish'):")

    if response_list.lower() == 'finished':
        print("Finished Program! Thank You...")
        break

    my_list.add(int(response_list))

original_list = list(my_list)

print('Original List:', original_list)
print('List without Duplicates:', list(my_list))

#16.Crie um programa que realize a união de múltiplos
#conjuntos e exiba o conjunto resultante.

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {11,12,13,14,15,16,17,18,19,20}
set3 = {21,22,23,24,25,26,27,28,29,30}

result_unions = (set1 | set2 | set3)
print(result_unions)

#Uma forma diferente e mais inteligente desse exercicío:

set4 = set()
set5 = set()
set6 = set()

while True:
    response = input("Enter a number for complete the set (Type 'finished for FINISH!'):")
    
    set4.add(response)
    set5.add(response)
    set6.add(response)

    if response.lower() == 'finished':
        print("Finished program. See you later!")
        break

    result_union = (set4 | set5 | set6)

print(result_union)

#17.Desafio!!
#Cadastro de Alunos: O programa deve permitir ao usuário cadastrar alunos. Cada aluno terá as seguintes informações: nome, idade e notas em três disciplinas: 
#Matemática, Ciências e História. Os dados de cada aluno devem ser armazenados em um dicionário com as seguintes chaves: 
#'nome','idade',' notas '. As notas devem ser armazenadas em uma tuplas.
#Visualização de Alunos: O programa deve permitir ao usuário visualizar todos os alunos cadastrados, exibindo suas informações de forma organizada.
#Média de Notas: O programa deve calcular a média das notas de cada aluno e exibi-la.
#Aluno com Melhor Média: O programa deve identificar e exibir o aluno com a melhor média de notas.

students_informations = {}

while True:
    name = input("Enter your name (Type 'finished' for finish):")

    if name.lower() == 'finished':
        print("Thank you, your program is finish ")
        break
    age = int(input(f"Enter your age {name}:"))


    student_data = {
        'name': name,
        'age': age,
        'notes': {
            'Math': (),
            'Biology': (),
            'History': ()
        }
    }

    for subject in student_data['notes'].keys():
        note = input(f"\n Enter your note in {subject}:")
        student_data['notes'][subject] += (note,)
    students_informations[name] = student_data

    print("\n Student notes:")
    for sudent_names, student_data in students_informations.items():
        print(f"Student name is --> {student_data['name']}")
        print(f"Student age is --> {student_data['age']} ")
        print('Notes:')

    for subject, notes in student_data['notes'].items():
        print(f"{subject}:{notes}")

