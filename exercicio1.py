class Animal:
    def __init__(self, nome : str, barulho : str, idade: int = 0):
        self.nome = nome
        self.barulho = barulho
        self.idade = 2
    def fazer_barulho(self):
        print(f"{self.nome} fez {self.barulho}")
    def aniversario(self):
        self.idade += 1
        print(f"{self.nome} fez {self.idade} anos")
def main():
    gato = Animal("Neymar","MIAU!!!", 1)
    cachorra = Animal("Elisa","MOOO!!!", 2)
    macaco = Animal("buck","huuuhaaa", 5)

    gato.fazer_barulho()
    cachorra.fazer_barulho()
    macaco.fazer_barulho()

    gato.aniversario()
    cachorra.aniversario()
    macaco.aniversario()

if __name__ == "__main__":
    main()
