#Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos onde a chave deste dicionário é o número de matrícula dos próprios alunos. O programa deve permitir adicionar, remover, atualizar e listar os alunos.
#Para isso, você deve implementar um módulo que contém as seguintes funções:
#AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário de alunos.
#RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos.
#AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno no dicionário .
#VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um.
#Lembre Se de Modularizar o código

alunos ={}
def AdicionarAluno():
    nome = input("Digite o seu nome aluno:")
    matricula = input(f"Digite o número da sua matrícula {nome}:")
    alunos[matricula] = nome
    print(f"Aluno: {nome} adiciona com matricula {matricula}.")

def RemoverAlunos():
    matricula = input("Você deseja remover alguma matrícula (sim/não):")
    if matricula in alunos:
        del alunos[matricula]
        print("O aluno não deseja remover a matrícula...") 
    else:
        print("Matricula não encontrada.")           

def AtualizarAluno():
    matricula = input("Digite sua matriculada para ser adicionada:")
    if matricula in alunos:
        novo_nome = input("Digite o novo nome do aluno:")
        alunos[matricula] = novo_nome
        print(f"Nome do aluno com matrícula {matricula} atualizado para {novo_nome}")
    else:
        print("Matricula não encontrada.")

def VerAlunos():
    print("Lista de Alunos:")
    for matricula, nome in alunos.items():
        print(f"Nome do aluno: {nome}/Número da Mátricula: {matricula}")