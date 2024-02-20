# Inicialização da lista de produtos
produtos = []
totalProdutos = 0.0

# Função para adicionar produtos à lista
def adicionar_produto():
    global totalProdutos
    nome = input("Informe o nome do produto: ")
    quantidade = int(input("Informe a quantidade: "))
    valor_unitario = float(input("Informe o valor unitário: "))

    # Calcula o valor total do produto e atualiza o valor total de todos os produtos
    total_produto = quantidade * valor_unitario
    totalProdutos += total_produto

    # Adiciona o produto à lista
    produtos.append({"produto": nome, "quantidade": quantidade, "valor": valor_unitario, "total": total_produto})

    print("Produto adicionado com sucesso!\n")

# Função para visualizar a lista de produtos
def visualizar_lista():
    if not produtos:
        print("Lista de produtos vazia.\n")
        return

    print("Lista de Produtos:")
    for produto in produtos:
        print(f"Produto: {produto['produto']}, Quantidade: {produto['quantidade']}, Valor Unitário: R${produto['valor']:.2f}, Total: R${produto['total']:.2f}")
    
    print(f"\nValor Total de Todos os Produtos: R${totalProdutos:.2f}\n")

# Função para atualizar informações de um produto
def atualizar_produto():
    global totalProdutos
    nome_atualizar = input("Informe o nome do produto que deseja atualizar: ")

    for produto in produtos:
        if produto['produto'] == nome_atualizar:
            quantidade = int(input("Informe a nova quantidade: "))
            valor_unitario = float(input("Informe o novo valor unitário: "))

            # Calcula o valor total do produto e atualiza o valor total de todos os produtos
            total_produto = quantidade * valor_unitario
            totalProdutos = totalProdutos - produto['total'] + total_produto

            # Atualiza as informações do produto
            produto['quantidade'] = quantidade
            produto['valor'] = valor_unitario
            produto['total'] = total_produto

            print("Produto atualizado com sucesso!\n")
            return
    
    print("Produto não encontrado.\n")

# Função para remover um produto da lista
def remover_produto():
    global totalProdutos
    nome_remover = input("Informe o nome do produto que deseja remover: ")

    for produto in produtos:
        if produto['produto'] == nome_remover:
            totalProdutos -= produto['total']
            produtos.remove(produto)
            print("Produto removido com sucesso!\n")
            return
    
    print("Produto não encontrado.\n")

# Loop principal
while True:
    print("Opções:")
    print("1 - Adicionar Produto")
    print("2 - Visualizar Lista de Produtos")
    print("3 - Atualizar Produto")
    print("4 - Remover Produto")
    print("5 - Encerrar Programa")

    opcao = int(input("Escolha uma opção (1-5): "))

    if opcao == 1:
        adicionar_produto()
    elif opcao == 2:
        visualizar_lista()
    elif opcao == 3:
        atualizar_produto()
    elif opcao == 4:
        remover_produto()
    elif opcao == 5:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.\n")




    
