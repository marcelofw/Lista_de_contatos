

numero_contatos = int(input("Quantos contatos deseja criar? "))
lista_contatos = []

for i in range(numero_contatos):
    print(f"Insira as informações para o contato número {i + 1}:")
    Nome = input("Nome: ")
    Sobrenome = input("Sobrenome: ")
    Telefone = input("Telefone: ")
    Email = input("Email: ")
    Descricao = input("Descricao: ")
    lista_contatos.append([Nome + " " + Sobrenome, Telefone, Email, Descricao])

for i, contato in enumerate(lista_contatos, 1):
    print(f"Contato {i}: {contato[0]}, {contato[1]}, {contato[2]}, {contato[3]}")


