class PetVirtual:
    def __init__(self, nome: str):
        self.nome = nome
        self.fome = 5
        self.felicidade = 5

    def alimentar(self):
        if self.fome > 0:
            self.fome = max(0, self.fome - 2)
            print(f"{self.nome} foi alimentado! Fome atual: {self.fome}")
        else:
            print(f"{self.nome} já está de barriga cheia!")

    def brincar(self):
        self.felicidade += 2
        self.fome += 1
        print(
            f"Você brincou com {self.nome}! Felicidade: {self.felicidade} | Fome: {self.fome}"
        )

    def status(self):
        print(
            f"\n--- STATUS DE {self.nome.upper()} ---"
            f"\nNome: {self.nome}"
            f"\nFome: {self.fome}"
            f"\nFelicidade: {self.felicidade}"
        )
        if self.fome >= 8:
            print(f"Atenção: {self.nome} precisa comer!")
        print("-------------------------\n")


print(" ==============================================================================")
print("                        PET VIRTUAL EM AÇÃO                                    ")
print(" ==============================================================================")

meu_pet = PetVirtual("Lagartixo123")

meu_pet.status()

meu_pet.brincar()
meu_pet.brincar()

meu_pet.alimentar()
meu_pet.alimentar()
meu_pet.alimentar()

meu_pet.status()