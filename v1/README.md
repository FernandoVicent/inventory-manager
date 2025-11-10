# 🗃️ Sistema de Controle de Estoque (Terminal)

Este repositório contém um sistema simples de controle de estoque de produtos, projetado para ser utilizado no terminal. Ele oferece funcionalidades essenciais como cadastro, consulta, edição e exclusão de produtos, organizando tudo de forma prática em uma lista de dicionários.

---

## 🧾 Descrição Geral

Este sistema permite ao usuário gerenciar produtos por meio de um menu interativo no terminal. Cada produto é armazenado como um dicionário dentro de uma lista chamada `estoque`, contendo informações como ID, nome, fabricante e valor.

---

## 🧩 Estrutura dos Produtos

Cada produto cadastrado possui os seguintes campos:

- `id` → número inteiro único, gerado aleatoriamente entre 1 e 999, sem repetições.
- `nome` → nome do produto informado pelo usuário.
- `fabricante` → nome do fabricante.
- `valor` → valor do produto (string, para manter o formato original do input).

---

## 🔧 Funcionalidades

### 1. Cadastrar Produto
- Gera um ID único com a função `gerar_id_unico()`.
- Solicita informações do produto ao usuário.
- Adiciona o produto à lista `estoque`.

### 2. Consultar Produto
Submenu com as seguintes opções:
- Consultar **todas as peças**
- Consultar por **código (ID)**
- Consultar por **fabricante**
- **Retornar** ao menu principal

A consulta utiliza verificações simples e apresenta os dados por meio da função `exibir_produto()`.

### 3. Editar Produto
- Solicita o ID do produto a ser editado.
- Permite a atualização do nome, fabricante e valor.
- Exibe mensagem de sucesso ou erro conforme o caso.

### 4. Excluir Produto
- Solicita o ID do produto a ser excluído.
- Remove o produto da lista, se encontrado.
- Exibe uma mensagem única de confirmação ou erro.

### 5. Menu Principal
- Exibe as principais opções por meio da função `menu()`:
  - Cadastrar
  - Consultar
  - Editar
  - Excluir
  - Sair

---

## ✅ Boas Práticas Presentes

- Código modular, separado em funções.
- Função dedicada para evitar duplicidade de IDs.
- Uso adequado de listas e dicionários.
- Verificações simples e eficazes para as operações.
