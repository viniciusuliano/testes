class Pessoas:
    def __init__(self, nome):
        self.nome = nome
        pass


class Representante(Pessoas):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario


class Cordenadores(Pessoas):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario
