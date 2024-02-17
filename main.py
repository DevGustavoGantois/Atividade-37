import CadastroAlunos

while True:
    print("\nEscolha uma opção:")
    print("1 - Adicionar Aluno")
    print("2 - Remover Aluno")
    print("3 - Atualizar Aluno")
    print("4 - Ver Alunos")
    print('5 - Sair')

    opcao = input("Digite o número da opção desejada:")

    if opcao == '1':
        CadastroAlunos.AdicionarAluno()
    elif opcao == '2':
        CadastroAlunos.RemoverAlunos()
    elif opcao == '3':
        CadastroAlunos.AtualizarAluno()
    elif opcao == '4':
        CadastroAlunos.VerAlunos()
    elif opcao == '5':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
    

