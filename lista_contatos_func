lista_contatos = []

def criar_contato():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    descricao = input("Descricao: ")
    return [nome + " " + sobrenome, telefone, email, descricao] 

def adicionar_contato(contato):     
    lista_contatos.append(contato)

def mostrar_contatos():
    if not lista_contatos:
        print("Nenhum contato cadastrado.")
    else:
        print("\nLista de contatos")
        for i, contato in enumerate(lista_contatos, 1):
            print(f"Contato {i}: Nome: {contato[0]}, Telefone: {contato[1]}, E-mail: {contato[2]}, Descricao: {contato[3]}")

quantidade = int(input("Quantos contatos deseja criar? "))

for i in range(quantidade):
    print(f"\nInsira as informações para o contato {i + 1}: ")
    contato = criar_contato()
    adicionar_contato(contato)

mostrar_contatos()










