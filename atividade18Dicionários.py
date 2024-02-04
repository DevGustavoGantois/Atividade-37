#Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.
#O programa deve fornecer as seguintes funcionalidades:
#Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.
#Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.
#Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos números de matrícula.
#O programa deve ser executado em um loop contínuo até que o usuário escolha sair.

informacao_estudantes = {}

while True:
    nome = input('Digite o seu nome (ou "terminar o programa" para sair): ')
    
    if nome.lower() == 'terminar o programa':
        print("Saindo do programa...")
        break

    numero_matricula = input('Digite o número da sua matrícula: ')

    if numero_matricula.lower() == 'remover matricula':
        matricula_remover = input('Digite a matrícula que você deseja remover: ')
        if matricula_remover in informacao_estudantes:
            del informacao_estudantes[matricula_remover]
            print(f"Matrícula {matricula_remover} removida com sucesso.")
        else:
            print(f"Matrícula {matricula_remover} não encontrada.")
    else:
        informacao_estudantes[numero_matricula] = nome 

    print('\nInformações dos estudantes:')
    for matricula_aluno, nome_aluno in informacao_estudantes.items():
        print(f"Matrícula: {matricula_aluno}, Nome: {nome_aluno}")

    print("<----------------------------------------->")




