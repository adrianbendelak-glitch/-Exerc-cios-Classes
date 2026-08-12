class Aplicativo:
    def __init__(self, nome, consumo):
        self.nome = nome
        self.consumo = consumo

class Celular:
    def __init__(self, bateria_maxima=100):
        self.ligado = False
        self.bateria = bateria_maxima

    def ligar(self):
        self.ligado = True
        print("Celular ligado.")

    def desligar(self):
        self.ligado = False
        print("Celular desligado.")

    def executar_app(self, app):
        if not self.ligado:
            print(f"Não foi possível executar '{app.nome}': Celular está desligado.")
            return

        if self.bateria >= app.consumo:
            self.bateria -= app.consumo
            print(
                f"Executando '{app.nome}'... (Consumo: {app.consumo}% | Bateria restante: {self.bateria}%)"
            )
        else:
            print(
                f"Bateria insuficiente ({self.bateria}%) para rodar '{app.nome}' (Requer: {app.consumo}%)."
            )


print("-------------------------------------------------------------")
print("                  EXECUÇÃO DO CÓDIGO                         ")
print("-------------------------------------------------------------")

app1 = Aplicativo("Instagram", 15)
app2 = Aplicativo("Manicraft", 40)

meu_celular = Celular(bateria_maxima=100)

print("--- Tentando rodar desligado ---")
meu_celular.executar_app(app1)

print("\n--- Ligando o celular e executando os apps ---")
meu_celular.ligar()
meu_celular.executar_app(app1)
meu_celular.executar_app(app2)