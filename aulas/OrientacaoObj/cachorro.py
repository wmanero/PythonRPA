class Cachorro:
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def rolar(self):
        print(f"O cachorro de raça {self.raca}, cujo nome é {self.nome} está rolando no chão agora!")

    def sentar(self):
        print(f"O cachorro de idade {self.idade}, cujo nome é {self.nome} está sentado agora!")

    def deitar(self):
        print(f"O cachorro de idade {self.idade}, cujo nome é {self.nome} está deitado agora!")