class Hospede:
    def __init__(self, nome, email, cpf, telefone, id=None):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.id = id

    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "id": self.id
        }
