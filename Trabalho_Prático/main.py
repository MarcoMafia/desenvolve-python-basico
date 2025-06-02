import os
#lê todos os usuários cadastrados, incluindo a senha e o nível de permissão
def ler_usuarios():
    usuarios = []
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r", encoding="utf-8") as file:
            for linha in file:
                usuario, senha, permissao = linha.strip().split(",")
                usuarios.append({"usuario": usuario, "senha": senha, "permissao": permissao})
    return usuarios
#salva a lista de usuários em usuarios.txt
def salvar_usuarios(lista):
    with open("usuarios.txt", "w", encoding="utf-8") as file:
        for u in lista:
            file.write(f"{u['usuario']},{u['senha']},{u['permissao']}\n")
#solicita o login e retorna o usuario validado
def fazer_login():
    usuarios = ler_usuarios()
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    for u in usuarios:
        if u["usuario"] == usuario and u["senha"] == senha:
            print(f"Bem-vindo, {usuario} ({u['permissao']})!")
            return u
    print("Login inválido.")
    return None
#cadastra um novo usuário à lista e depois salva em usuarios.txt
def cadastrar_usuario():
    usuarios = ler_usuarios()
    usuario = input("Novo usuário: ")
    senha = input("Senha: ")
    permissao = input("Permissão (gerente/funcionario/cliente): ")
    usuarios.append({"usuario": usuario, "senha": senha, "permissao": permissao})
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!")
#remove o usuário que esteja em usuarios.txt
def excluir_usuario():
    usuarios = ler_usuarios()
    nome = input("Nome do usuário a excluir: ")
    usuarios = [u for u in usuarios if u["usuario"] != nome]
    salvar_usuarios(usuarios)
    print("Usuário excluído.")
#atualiza a senha de um usuário
def atualiza_senha():
    usuarios = ler_usuarios()
    nome = input("Nome do usuário: ")
    nova_senha = input("Nova senha: ")
    for u in usuarios:
        if u["usuario"] == nome:
            u["senha"] = nova_senha
    salvar_usuarios(usuarios)
    print("Senha atualizada.")
#lê os produtos e serviços cadastrados, incluindo o código, o valor e a quantidade
def ler_produtos():
    produtos = []
    if os.path.exists("produtos&serviços.txt"):
        with open("produtos&serviços.txt", "r", encoding="utf-8") as file:
            for linha in file:
                codigo, nome, preco, quantidade = linha.strip().split(",")
                produtos.append({"codigo": codigo, "nome": nome, "preco": float(preco), "quantidade": int(quantidade)})
    return produtos
#salva a lista de produtos em produtos&serviços.txt
def salvar_produtos(lista):
    with open("produtos&serviços.txt", "w", encoding="utf-8") as file:
        for p in lista:
            file.write(f"{p['codigo']},{p['nome']},{p['preco']},{p['quantidade']}\n")
#solicita o nome, o código, o preço e a quantidade de um produto e o adiciona em produtos&serviços.txt
def cadastrar_produto():
    produtos = ler_produtos()
    codigo = input("Código: ")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    produtos.append({"codigo": codigo, "nome": nome, "preco": preco, "quantidade": quantidade})
    salvar_produtos(produtos)
    print("Produto cadastrado.")
#exclui o produto de produtos&serviços.txt relacionado ao código solicitado
def excluir_produto():
    produtos = ler_produtos()
    codigo = input("Código do produto a excluir: ")
    produtos = [p for p in produtos if p["codigo"] != codigo]
    salvar_produtos(produtos)
    print("Produto excluído.")
#atualiza os dados de um produto
def atualizar_produto():
    produtos = ler_produtos()
    codigo = input("Código do produto: ")
    for p in produtos:
        if p["codigo"] == codigo:
            p["nome"] = input("Novo nome: ")
            p["preco"] = float(input("Novo preço: "))
            p["quantidade"] = int(input("Nova quantidade: "))
    salvar_produtos(produtos)
    print("Produto atualizado.")
#busca o produto por nome ou código e o exibe
def buscar_produto():
    produtos = ler_produtos()
    termo = input("Buscar por nome ou código: ").lower()
    for p in produtos:
        if termo in p["nome"].lower() or termo == p["codigo"]:
            print(p)
            return
    print("Produto não encontrado.")
#lista os produtos por nome ou por preço
def listar_ordenado(chave):
    produtos = ler_produtos()
    produtos_ordenados = sorted(produtos, key=lambda x: x[chave])
    for p in produtos_ordenados:
        print(p)
# menu para escolher qual ação realizar dentro do sistema, de acordo com a permissão de cada usuário
def menu_interno(usuario):
    while True: #opções de qualquer usuario
        print("\n--- Menu Principal ---")
        print("1. Buscar produto/serviço")
        print("2. Listar produtos por nome")
        print("3. Listar produtos por preço")
        if usuario["permissao"] in ["gerente", "funcionario"]: #opções de qualquer funcionário da loja
            print("4. Cadastrar produto")
            print("5. Excluir produto")
            print("6. Atualizar produto")
        if usuario["permissao"] == "gerente": #opções apenas para o gerente
            print("7. Cadastrar usuário")
            print("8. Excluir usuário")
            print("9. Atualizar senha")
        print("0. Sair")
# execução da opção selecionada
        op = input("Escolha uma opção: ")
        if op == "1":
            buscar_produto()
        elif op == "2":
            listar_ordenado("nome")
        elif op == "3":
            listar_ordenado("preco")
        elif op == "4" and usuario["permissao"] in ["gerente", "funcionario"]:
            cadastrar_produto()
        elif op == "5" and usuario["permissao"] in ["gerente", "funcionario"]:
            excluir_produto()
        elif op == "6" and usuario["permissao"] in ["gerente", "funcionario"]:
            atualizar_produto()
        elif op == "7" and usuario["permissao"] == "gerente":
            cadastrar_usuario()
        elif op == "8" and usuario["permissao"] == "gerente":
            excluir_usuario()
        elif op == "9" and usuario["permissao"] == "gerente":
            atualiza_senha()
        elif op == "0":
            break
        else:
            print("Opção inválida ou não permitida.")

#menu inicial
while True:
    print("\n--- Bem-vindo ao Sistema ---")
    print("1. Login")
    print("0. Sair")
    escolha = input("Escolha: ")
    if escolha == "1":
        usuario = fazer_login()
        if usuario:
            menu_interno(usuario)
    elif escolha == "0":
        break
    else:
        print("Opção inválida.")