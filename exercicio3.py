class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = float(saldo_inicial)
        self.limite_cheque_especial = 500.0  # Permite saldo negativo até -500.00

    def adicionar_saldo(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"[+] R$ {valor:.2f} creditados na conta de {self.titular}.")
        else:
            print("[!] Valor inválido para depósito.")

    def transferir(self, valor, conta_destino):
        if valor <= 0:
            print("[!] O valor da transferência deve ser maior que zero.")
            return

        # Validação do limite: Saldo atual - valor não pode ser menor que -500
        if self.saldo - valor < -self.limite_cheque_especial:
            limite_disponivel = self.saldo + self.limite_cheque_especial
            print(f"\n[X] TRANSFERÊNCIA BLOQUEADA para {self.titular}!")
            print(f"    Motivo: Limite excedido. Saldo atual: R$ {self.saldo:.2f} | Limite disponível para uso: R$ {limite_disponivel:.2f}\n")
            return

        # Exibe saldos ANTES
        print("\n==========================================")
        print("--- SALDOS ANTES DA TRANSFERÊNCIA ---")
        print(f"  {self.titular}: R$ {self.saldo:.2f}")
        print(f"  {conta_destino.titular}: R$ {conta_destino.saldo:.2f}")
        print("------------------------------------------")

        # Efetua a transação
        self.saldo -= valor
        conta_destino.adicionar_saldo(valor)

        # Exibe saldos DEPOIS
        print("--- SALDOS DEPOIS DA TRANSFERÊNCIA ---")
        print(f"  {self.titular}: R$ {self.saldo:.2f}")
        print(f"  {conta_destino.titular}: R$ {conta_destino.saldo:.2f}")
        print("==========================================\n")


# ==========================================
# TESTE NO TERMINAL (Execução direta)
# ==========================================
if __name__ == "__main__":
    print("--- INICIANDO TESTE DO SISTEMA BANCÁRIO ---\n")

    # Criando duas contas
    conta_joao = ContaBancaria("João", 100.0)
    conta_maria = ContaBancaria("Maria", 200.0)

    # Teste 1: Transferência normal usando o saldo
    print("1. João transfere R$ 50,00 para Maria:")
    conta_joao.transferir(50.0, conta_maria)

    # Teste 2: Transferência entrando no cheque especial (Saldo fica -350.00)
    print("2. João transfere R$ 400,00 para Maria (Entrando no Cheque Especial):")
    conta_joao.transferir(400.0, conta_maria)

    # Teste 3: Tentativa de ultrapassar o limite de -500.00 (Deve ser BLOQUEADO)
    print("3. João tenta transferir R$ 200,00 para Maria (Excederia o limite de -500):")
    conta_joao.transferir(200.0, conta_maria)