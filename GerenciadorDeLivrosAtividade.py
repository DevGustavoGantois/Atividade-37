#Gerenciador de Livros de Biblioteca - passo 1
#Crie um programa que permita aos usuários:
#Adicionar novos livros à biblioteca, com informações como título, autor e número de cópias disponíveis.
#Listar todos os livros disponíveis na biblioteca.
#Permitir aos usuários fazer empréstimos de livros, reduzindo o número de cópias disponíveis quando um livro é emprestado.
#- passo 2
#Permitir aos usuários devolver livros, aumentando o número de cópias disponíveis quando um livro é devolvido.
#Verificar a disponibilidade de um livro específico na biblioteca.
#Mostrar a lista de livros emprestados a um usuário específico.

livros_biblioteca = []
livros_emprestados = []

def informacoes_usuario(nome, idade, email, senha, telefone):
    print("<=======================================================================>")
    print(f"Nome do aluno: {nome}")
    print(f"Idade do aluno: {idade}")
    print(f"Email do aluno: {email}")
    print(f"Senha do aluno: {senha}")
    print(f"Telefone do aluno: {telefone}")

def novos_livros(titulo, autor, copias_disponiveis):
    print(f"Titulo: {titulo}")
    print(f"Autor: {autor}")
    print(f"Copias disponiveis: {copias_disponiveis}")

def numeros_livros_disponiveis(livros):
    for livro in livros_biblioteca:
        print(f"Título: {livro['titulo']} - Copias disponiveis: {livro['copias_disponiveis']}")

def emprestar_livro(titulo):
    for livro in livros_biblioteca:
        if livro['titulo'] == titulo and livro['copias_disponiveis'] > 0:
            livro['copias_disponiveis'] -= 1
            livros_emprestados.append(livro)
            print(f"Livro '{titulo}' emprestado com sucesso.")
            return
    print(f"Livro '{titulo}' indisponível ou sem cópias disponíveis.")

def devolver_livro(titulo):
    for livro in livros_emprestados:
        if livro['titulo'] == titulo:
            livro['copias_disponiveis'] += 1
            livros_emprestados.remove(livro)
            print(f"Livro '{titulo}' devolvido com sucesso.")
            return
    print(f"Livro '{titulo}' não encontrado nos livros emprestados.")

def main():
    cadastro_sim_nao = input(f"Olá! Você já possui cadastro na biblioteca (sim/não)?")

    if cadastro_sim_nao.lower() == "sim":
        email = input("Digite seu e-mail ou seu nome de usuário:")
        senha = input("Digite sua senha:")
    elif cadastro_sim_nao.lower() == "não":
        nome = input("Olá aluno. Digite o seu nome:")
        idade = int(input("Digite sua idade:"))
        email = input(f"Email do aluno {nome}:")
        senha = input(f"Digite sua senha {nome}:")
        telefone = input(f"Digite seu número de telefone:")
        informacoes_usuario(nome, idade, email, senha, telefone)
        print("<======================================================================>")
    else:
        print("Opção inválida. Programação encerrado...")
        return

    while True:
        cadastrar_livro = input("Você deseja pegar algum livro na biblioteca (sim/não):")
        if cadastrar_livro.lower() == "não":
            print("Programa encerrado...Volte sempre.")
            break
        elif cadastrar_livro.lower() == "sim":
            titulo = input("Título do livro:")
            autor = input("Nome do Autor:")
            copias_disponiveis = int(input("Cópias disponíveis:"))
            livro = {
                'titulo': titulo,
                'autor': autor,
                'copias_disponiveis': copias_disponiveis
            }
            livros_biblioteca.append(livro)
            print(f"Livro '{titulo}' adicionado à biblioteca.")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


              
            
            
