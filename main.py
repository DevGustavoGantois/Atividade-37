print("LISTA DE TAREFAS")
print("<--------------------------------->")

def main():
    tarefas = []

    while True:
        print("<----------------------------------->")
        print("OLÁ!! SEJA BEM-VINDO...  ")
        print("<-------------------------------->")
        print("Opção 1 => Adicionar tarefas.")
        print("Opção 2 => Listar tarefas.")
        print("Opção 3 => Marcar tarefas como concluídas.")
        print("Opção 4 => Remover alguma tarefa.")
        print("Opção 5 => Sair do programa, digite -> 'Sair do programa'")

        opcao = input("Digite a opção que você deseja escolher:")

        if opcao == '1':
            adicionar_tarefas(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            marcar_tarefas_concluida(tarefas)
        elif opcao == '4':
            remover_tarefas(tarefas)
        elif opcao == 'Sair do programa':
            print("Programa encerrado.")
            break
        else:
            print("Por favor. Digite novamente, este comando não existe...")

def adicionar_tarefas(tarefas):
    nome = input("Qual o nome dessa tarefa:")
    descricao = input("Descreva essa tarefa:")
    prioridade = input("Qual o nível de prioridade dessa tarefa:")
    categoria = input("Qual é a categoria dessa tarefa:")
    
    nova_tarefa = {'nome': nome, 'descricao': descricao, 'prioridade': prioridade, 'categoria': categoria, 'concluida': False}
    tarefas.append(nova_tarefa)

def listar_tarefas(tarefas):
    for tarefa in tarefas:
        print(tarefa)

def marcar_tarefas_concluida(tarefas):
    listar_tarefas(tarefas)
    nome_tarefa = input("Digite o nome da tarefa que você deseja marcar como concluída:")
    
    for tarefa in tarefas:
        if tarefa['nome'] == nome_tarefa:
            tarefa['concluida'] = True
            print("Tarefa marcada como concluída.")
            return
    
    print("Tarefa não encontrada.")

def remover_tarefas(tarefas):
    listar_tarefas(tarefas)
    nome_tarefa = input("Digite o nome da tarefa que você deseja remover:")
    
    for tarefa in tarefas:
        if tarefa['nome'] == nome_tarefa:
            tarefas.remove(tarefa)
            print("Tarefa removida.")
            return
    
    print("Tarefa não encontrada.")

if __name__ == '__main__':
    main()

