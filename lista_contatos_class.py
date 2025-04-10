
class Contato():
    def __init__(self, nome, sobrenome, telefone, email, descricao):
        self.nome_completo = nome + " " + sobrenome             
        self.telefone = telefone
        self.email = email
        self.descricao = descricao
    
    def exibir(self):
        print(f"Nome: {self.nome_completo}")        
        print(f"Telefone: {self.telefone}")
        print(f"Email: {self.email}")
        print(f"Descrição: {self.descricao}")
        print(f"-" * 30)

lista_contatos = []

quantidade = int(input("Quantos contatos deseja criar? "))

for i in range(quantidade):
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    descricao = input("Descrição: ")
    contato = Contato(nome, sobrenome, telefone, email, descricao)
    lista_contatos.append(contato)          

print(lista_contatos)

print("\nLista de contatos:")
for contato in lista_contatos:
    contato.exibir()                    




