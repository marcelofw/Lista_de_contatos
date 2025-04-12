numero_contatos = int(input("Quantos contatos deseja criar? "))
lista_contatos = []

for i in range(numero_contatos):
    print(f"\nContato {i + 1}: ")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    descricao = input("Descrição: ")

    contato = {
        "nome": nome,
        "sobrenome": sobrenome,
        "telefone": telefone,
        "email": email,
        "descricao": descricao
    }

    lista_contatos.append(contato) #cria uma lista de dicionários?

print("\nLista de contatos:")
for i, contato in enumerate(lista_contatos, start=1):    #start=1 equivale a 1?
    print(f"\nContato {i}: ")
    print(f"Nome: {contato['nome']} {contato['sobrenome']}")
    print(f"Telefone: {contato['telefone']}")
    print(f"Email: {contato['email']}")
    print(f"Descrição: {contato['descricao']}")
    print("-" * 30)

