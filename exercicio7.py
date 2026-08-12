class Bicicleta:
    def __init__(self, modelo: str):
        self.modelo = modelo
        self.velocidade = 0

    def pedalar(self):
        if self.velocidade + 5 <= 60:
            self.velocidade += 5
            print(f"A bike {self.modelo} acelerou! Velocidade: {self.velocidade} km/h")
        else:
            self.velocidade = 60
            print(f"A bike {self.modelo} já atingiu o limite máximo de velocidade: 60 km/h!")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 5
            print(f"Reduzindo... Velocidade: {self.velocidade} km/h")
        else:
            print("A bicicleta já está totalmente parada!")

    def radar_de_velocidade(self):
        print(f"Radar: A velocidade atual da bike é {self.velocidade} km/h")


print("-------------------------------------------------------------")
print("                  BICICLETA EM ANDAMENTO                     ")
print("-------------------------------------------------------------")

minha_bike = Bicicleta(10)

print("--- Aceleração ---")
minha_bike.pedalar()
minha_bike.pedalar()

print("\n--- Checando Velocidade ---")
minha_bike.radar_de_velocidade()

print("\n--- Frenagem ---")
minha_bike.frear()
minha_bike.frear()
minha_bike.frear()