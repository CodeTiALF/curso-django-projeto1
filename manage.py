class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def listar_atributos(self):
        atributos = vars(self)  # Obtém um dicionário dos atributos da instância
        for atributo, valor in atributos.items():
            print(f'{atributo}: {valor}')

# Criar uma instância da classe Usuario
usuario1 = Usuario("joao123", "senha123")

# Listar os atributos e valores do usuário
print("Atributos e Valores do Usuário:")
usuario1.listar_atributos()
