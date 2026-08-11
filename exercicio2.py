class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
        self.combustivel = 0
        self.quilometragem = 0  # Inicia em 0 km
        self.limite_tanque = 100

    def abastecer(self, quantidade):
        if quantidade <= 0:
            print("A quantidade a abastecer deve ser maior que zero.")
            return

        if self.combustivel + quantidade > self.limite_tanque:
            self.combustivel = self.limite_tanque
            print(f"Tanque cheio! Combustível ajustado para o limite máximo ({self.limite_tanque}L).")
        else:
            self.combustivel += quantidade
            print(f"Abastecido com sucesso. Nível de combustível: {self.combustivel}L.")

    def acelerar(self):
        if self.combustivel >= 5:
            self.combustivel -= 5
            self.quilometragem += 15  # Aumenta 15 km a cada aceleração bem-sucedida
            print("Vrummm! O carro acelerou.")
        else:
            print("Combustível insuficiente para acelerar!")

    def painel(self):
        print("\n--- PAINEL DO CARRO ---")
        print(f"Veículo: {self.marca} {self.modelo}")
        print(f"Combustível: {self.combustivel}L / {self.limite_tanque}L")
        print(f"Quilometragem: {self.quilometragem} km")
        print("-----------------------")


# ==========================================
# EXECUÇÃO NO TERMINAL
# ==========================================
if __name__ == "__main__":
    print("--- TESTANDO O CARRO NO TERMINAL ---")

    # 1. Criando o carro
    meu_carro = Carro("Toyota", "Corolla")
    
    # Exibe o painel inicial
    meu_carro.painel()

    # 2. Tenta acelerar sem combustível
    print("\n[Tentando acelerar sem combustível]")
    meu_carro.acelerar()

    # 3. Abastecendo
    print("\n[Abastecendo o carro]")
    meu_carro.abastecer(30)

    # 4. Acelerando duas vezes
    print("\n[Acelerando o veículo]")
    meu_carro.acelerar()
    meu_carro.acelerar()

    # 5. Exibindo painel atualizado
    meu_carro.painel()