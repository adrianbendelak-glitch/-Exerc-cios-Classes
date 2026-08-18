class CofreDigital:
    
    def __init__(self, senha: int, titular: str):
        self.__senha = senha
        self.titular = titular
        self.__saldo = 0.0  # Saldo protegido (privado)

    def depositar_valor(self, valor: float):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso! Saldo atual: R${self.__saldo:.2f}")  
        else:
            print("Valor inválido para depósito!")
        
    def sacar_valor(self, valor: float, senha_informada: int):
        if senha_informada != self.__senha:
            print("Senha incorreta. Acesso negado!")
            return

        if valor <= 0:
            print("Valor inválido para saque!")
        elif valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso! Saldo atual: R${self.__saldo:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def consultar_saldo(self, senha_informada: int):
        if senha_informada == self.__senha:
            print(f"Titular: {self.titular} | Saldo atual: R${self.__saldo:.2f}")
        else:
            print("Senha incorreta. Acesso negado!")

            

print("=== CRIAÇÃO DO COFRE DIGITAL ===")
nome_titular = input("Digite o nome do titular: ")
senha_cofre = int(input("Crie uma senha numérica (ex: 1234): "))

# Instancia o cofre com os dados informados
meu_cofre = CofreDigital(senha=senha_cofre, titular=nome_titular)

while True:
    print("\n" + "="*30)
    print(f"   COFRE DIGITAL DE {meu_cofre.titular.upper()}")
    print("="*30)
    print("1. Depositar")
    print("2. Sacar")
    print("3. Consultar Saldo")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1-4): ")

    if opcao == "1":
        valor = float(input("Digite o valor para depósito: R$ "))
        meu_cofre.depositar_valor(valor)

    elif opcao == "2":
        valor = float(input("Digite o valor para saque: R$ "))
        senha_inf = int(input("Digite sua senha: "))
        meu_cofre.sacar_valor(valor, senha_inf)

    elif opcao == "3":
        senha_inf = int(input("Digite sua senha: "))
        meu_cofre.consultar_saldo(senha_inf)

    elif opcao == "4":
        print("\nSaindo do sistema... Até logo!")
        break

    else:
        print("Opção inválida! Tente novamente.")