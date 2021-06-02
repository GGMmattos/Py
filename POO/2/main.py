#Métodos de Classes - Python Orientado a Objetos
from random import randint
class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade =  idade

    #Metodo normal
    # Medodo de instância, precisa receber o parâmetro self
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # Métodos de Classes
    # utiliza a classe (cls)
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    #Método Estático
    # não recebe instância e nem  classe, mas podemos usar estes na sua utilização
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

#p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
p1 = Pessoa('Luiz', 32)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())