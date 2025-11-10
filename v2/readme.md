# 🗃️ Inventory Manager (Terminal)

Este repositório contém um **sistema de gerenciamento de estoque de produtos**, desenvolvido em **Python**, com base em **Programação Orientada a Objetos (POO)**.  
O sistema foi projetado para rodar diretamente no **terminal**, oferecendo operações completas de **cadastro, consulta, edição e exclusão de produtos**, além do registro automático de **logs de alterações**.

---

## 🧾 Descrição Geral

O sistema permite ao usuário gerenciar produtos e fabricantes de forma prática, através de um **menu interativo**.  
Todos os produtos são representados por objetos da classe `Product`, e cada fabricante é representado pela classe `Producer`.  
Um identificador (`id`) é gerado automaticamente para cada produto, evitando duplicações e garantindo integridade no controle de estoque.

Além disso, todas as ações executadas (criação, edição, exclusão etc.) são registradas em um arquivo de **log** (`logs.txt`), permitindo rastrear o histórico de modificações.

---

## 🧩 Estrutura das Classes

### Classe `Producer`
Representa o fabricante do produto.
- `name` → nome do fabricante

### Classe `Product`
Representa um produto no estoque.
- `id` → gerado automaticamente (sem duplicações)
- `name` → nome do produto
- `producer` → objeto da classe `Producer`
- `price` → valor do produto
- `quantity` → quantidade disponível em estoque

### Classe `Inventory`
Gerencia o conjunto de produtos e fabricantes.
- Controla criação, consulta, atualização e exclusão de produtos
- Realiza validações de ID
- Registra logs de todas as ações

---

## 🔧 Funcionalidades

### 1. Criar Fabricante
- Permite cadastrar novos fabricantes.
- Evita duplicação de nomes já existentes.

### 2. Criar Produto
- Gera automaticamente um `ID` único.
- Solicita informações como nome, fabricante, preço e quantidade.
- Registra o produto no inventário e gera um log.

### 3. Consultar Produto
Permite pesquisar produtos de diferentes formas:
- Por **ID**
- Por **nome**
- Por **fabricante**
- Exibe todos os produtos cadastrados

### 4. Editar Produto
- Solicita o ID do produto a ser alterado.
- Permite modificar nome, fabricante, preço e quantidade.
- Registra a atualização no arquivo de logs.

### 5. Excluir Produto
- Solicita o ID do produto a ser removido.
- Remove o produto e registra a ação no log.

### 6. Consultar Logs
- Exibe o conteúdo do arquivo `logs.txt` com todas as ações realizadas no sistema.

### 7. Menu Principal
A função `menu()` exibe as principais opções de forma interativa.

## 🗂️ Estrutura do Projeto
### inventory-manager
- producer.py  #Classe do fabricante
-product.py  #Classe do produto
- inventory.py #Classe que gerencia o estoque e os logs
- main.py  #Arquivo principal com o menu interativo
- logs.txt  #Registro de logs de ações

## ✅ Boas Práticas Presentes

- Código **modularizado** e **orientado a objetos**
- **Geração automática de IDs** sem duplicação
- **Registro de logs** para rastrear ações
- Estrutura organizada em múltiplos arquivos
- **Validação** de entradas e tratamento de erros
- Interface limpa e intuitiva via terminal
