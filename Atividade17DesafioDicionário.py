#Cadastro de Alunos: O programa deve permitir ao usuário cadastrar alunos. Cada aluno terá as seguintes informações: nome, idade e notas em três disciplinas: 
#Matemática, Ciências e História. Os dados de cada aluno devem ser armazenados em um dicionário com as seguintes chaves: 
#'nome','idade',' notas '. As notas devem ser armazenadas em uma tuplas.
#Visualização de Alunos: O programa deve permitir ao usuário visualizar todos os alunos cadastrados, exibindo suas informações de forma organizada.
#Média de Notas: O programa deve calcular a média das notas de cada aluno e exibi-la.
#Aluno com Melhor Média: O programa deve identificar e exibir o aluno com a melhor média de notas.

student_informations = {}

while True:

    name = input('Enter your name:')
    
    if name.lower() == 'finished':
        print('Finished the Program. See you later user!')  
        break

    age = int(input(f"Enter your age {name}:"))

    student_data = {
        'name': name,
        'age': age,
        'notes': {
            'Math':(),
            'Biology':(),
            'History':()
        }
    }

    for subject in student_data['notes'].keys():
        note = float(input(f"Enter the subject notes -> {subject}:"))
        student_data['notes'][subject] += (note)


    student_informations[name] = student_data

print('\nStudents Information:')
for student_names, student_data in student_informations.items():
    print(f"\nStudent name --> {student_data['name']}")
    print(f"\nStudent age --> {student_data['age']} ")
    print(f"Notes:")
    for subject, notes in student_data['notes'].items():
        print(f"{subject}:{notes}")

#EXPLICANDO O CÓDIGO:
#1.Criei um dicionário vazio para adicionar as informações sobre os alunos: nome, idade e matérias com suas respectivas notas:
#2.Criei um loop infinito para mostrar quantas quantas vezes for preciso as informações pedidas pelo usuário.
#3.Usei o nome dentro do While e se(Estrutura condicional) o usuário digitar finished o programa irá terminar
#4.Criei um dicionário student_data para armazenar o nome idade e notas e um dicionário aninhado com esse contendo as notas.
#5.Criei um loop de repetição for para percorrer as chaves do notes no student_data
#6.Criei uma váriavel chamada notes com um input digitando as notas  dentro do dicionário
#7.armazenei as notas dentro de uma tupla para não ocorrer alterações nas mesmas.
#8.Criei um dicionário[chave]=valor se a chave existir no dicionário ela terá sobrescrito caso contrário ela será criada e o valor será atribuido a ela
#9.Deium print f mostrando o nome dos estudantes, idade e notas 
#10.Criei um for subject, notes em student_data['notes'].items() para mostrar os itens
#dentro do dicionário notes dentro do dicionário student_data.
#11.Mostrei o valor no terminal com um print f {subject}:{notes}.