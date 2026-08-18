class Veiculo:
    quantidade_veiculos = 0     # 1. Para que serve esta variável?
    registros_veiculos = []     # 2. Para que serve esta variável?
    # 3. Qual o nome técnico destas duas variáveis?
    
    def __init__(self, nome, marca): # 4. Qual o nome técnico das variáveis de dentro dos parenteses?
        Veiculo.quantidade_veiculos += 1 # 5. Por que utilizo Veiculo antes do nome da variável?

        # 6. Qual o nome técnico destas variáveis a seguir? Qual funcionalidade define esta denominação em Python?
        self.nome = nome
        self.marca = marca
        self.gasolina = 100
        Veiculo.registros_veiculos.append(self)     # 7. Por que utilizo o método .append nestá variavel de Veiculo?

    def __str__(self):      # 8. O que esta função reservada está definindo?
        return f"{self.nome} da {self.marca} com {self.gasolina} de gasolina"
    
    def __repr__(self):     # 9. O que esta função reservada está definindo?
        return self.nome

camaro = Veiculo("camaro", "chevrolet")
onyx = Veiculo("onyx", "chevrolet")

print(Veiculo.registros_veiculos)
print(Veiculo.quantidade_veiculos)
print(camaro)
print(onyx)