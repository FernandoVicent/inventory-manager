from menu import menu
from random import randint

estoque = []


def gerar_id_unico():
    while True:
        novo_id = randint(1, 999)
        if all(produto['id'] != novo_id for produto in estoque):
            return novo_id


def cadastrar_produto():
    produto_id = gerar_id_unico()
    print(f"\nO código da sua peça é: {produto_id}")

    nome = input("Digite o nome do produto: ")
    fabricante = input("Digite o nome do fabricante: ")
    valor = input("Digite o valor do produto: ")

    produto = {
        'id': produto_id,
        'nome': nome,
        'fabricante': fabricante,
        'valor': valor
    }

    estoque.append(produto)
    print("Produto cadastrado com sucesso!\n")


def exibir_produto(produto):
    print(f"{'_' * 20}")
    print(f"ID: {produto['id']}")
    print(f"Produto: {produto['nome']}")
    print(f"Fabricante: {produto['fabricante']}")
    print(f"R$: {produto['valor']}")
    print(f"{'_' * 20}")


def consultar_produto():
    print("_" * 50)
    opcao = menu([
        "Consultar todas as peças",
        "Consultar peças por código",
        "Consultar peças por fabricante",
        "Retornar"
    ])
    print("_" * 50)

    if opcao == 1:
        for produto in estoque:
            exibir_produto(produto)

    elif opcao == 2:
        codigo = int(input("Digite o código do produto: "))
        encontrado = False
        for produto in estoque:
            if produto['id'] == codigo:
                exibir_produto(produto)
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado.")

    elif opcao == 3:
        fabricante = input("Digite o nome do fabricante: ")
        encontrados = [p for p in estoque if p['fabricante'].lower() == fabricante.lower()]
        if encontrados:
            for produto in encontrados:
                exibir_produto(produto)
        else:
            print("Nenhum produto encontrado para esse fabricante.")

    elif opcao == 4:
        print("Retornando ao menu principal.")
    else:
        print("Opção inválida.")


def editar_produto():
    codigo = int(input("Digite o ID do produto que deseja editar: "))
    for produto in estoque:
        if produto['id'] == codigo:
            produto['nome'] = input("Digite o novo nome do produto: ")
            produto['fabricante'] = input("Digite o novo fabricante: ")
            produto['valor'] = input("Digite o novo valor: ")
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado.")

def excluir_produto():
    codigo = int(input("Digite o ID do produto que deseja excluir: "))
    for produto in estoque:
        if produto['id'] == codigo:
            estoque.remove(produto)
            print("Produto removido com sucesso!")
        else:
            print("Produto não encontrado.")

# Loop principal
while True:
    print("_" * 50)
    escolha = menu([
        "Cadastrar Produto",
        "Consultar Produto",
        "Editar Produto",
        "Excluir Produto"
    ])
    print("_" * 50)

    if escolha == 0:
        print("Saindo...")
        break
    elif escolha == 1:
        cadastrar_produto()
    elif escolha == 2:
        consultar_produto()
    elif escolha == 3:
        editar_produto()
    elif escolha == 4:
        excluir_produto()
    else:
        print("Opção inválida, tente novamente.")
