import json
import os

ARQUIVO = "clientes.json"

#carregar os clientes do arquivo

def carregar_clientes():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r") as f:
        return json.load(f)

#salvar no arquivo

def salvar_clientes(clientes):
    with open(ARQUIVO, "w") as f:
        json.dump(clientes, f, indent=4)

# Cadastrar novo cliente

def cadastrar_cliente(clientes):
    print("\nCadastrar Cliente")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    endereco = input("Endereço: ")

    # Verifica se já existe CPF igual
    for c in clientes:
        if c["cpf"] == cpf:
            print("Já existe um cliente com esse CPF")
            return

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }

    clientes.append(cliente)
    salvar_clientes(clientes)

    print("Cliente cadastrado")

# Buscar cliente pelo CPF

def buscar_cliente(clientes):
    cpf = input("\nDigite o CPF do cliente que deseja buscar: ")

    for c in clientes:
        if c["cpf"] == cpf:
            print("\nCliente Encontrado")
            print(json.dumps(c, indent=4, ensure_ascii=False))
            return

    print("Cliente não encontrado")

# Alterar dados de um cliente

def alterar_cliente(clientes):
    cpf = input("\nCPF do cliente a ser alterado: ")

    for c in clientes:
        if c["cpf"] == cpf:
            print("\nDeixe em branco caso não queira alterar o valor.")

            novo_nome = input(f"Nome ({c['nome']}): ") or c["nome"]
            novo_telefone = input(f"Telefone ({c['telefone']}): ") or c["telefone"]
            novo_email = input(f"Email ({c['email']}): ") or c["email"]
            novo_endereco = input(f"Endereço ({c['endereco']}): ") or c["endereco"]

            c["nome"] = novo_nome
            c["telefone"] = novo_telefone
            c["email"] = novo_email
            c["endereco"] = novo_endereco

            salvar_clientes(clientes)
            print("Dados alteradoso")
            return

    print("Cliente não encontrado")

# Apagar cliente

def apagar_cliente(clientes):
    cpf = input("\nCPF do cliente a ser removido: ")

    for c in clientes:
        if c["cpf"] == cpf:
            clientes.remove(c)
            salvar_clientes(clientes)
            print("Cliente removido")
            return

    print("Cliente não encontrado")


# Mostrar todos os clientes

def listar_clientes(clientes):
    print("\nLista de Clientes")
    if not clientes:
        print("Nenhum cliente cadastrado")
        return

    for c in clientes:
        print(json.dumps(c, indent=4, ensure_ascii=False))
        print("------------------------------")

# Menu principal

def main():
    clientes = carregar_clientes()

    while True:
        print("""
Menu
1 - Cadastrar cliente
2 - Buscar cliente por CPF
3 - Alterar cliente
4 - Apagar cliente
5 - Listar todos
0 - Sair
""")

        opc = input("Escolha: ")

        if opc == "1":
            cadastrar_cliente(clientes)
        elif opc == "2":
            buscar_cliente(clientes)
        elif opc == "3":
            alterar_cliente(clientes)
        elif opc == "4":
            apagar_cliente(clientes)
        elif opc == "5":
            listar_clientes(clientes)
        elif opc == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
