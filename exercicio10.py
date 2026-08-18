class OrdemDeServiço:
    total_os_criadas = 0
    os_abertas = 0

    def __init__(self, cliente: str, descrição: str):
        self.cliente = cliente
        self.descrição = descrição
        self.status = "Aberta"  # Atributo individual da ordem
        
        OrdemDeServiço.total_os_criadas += 1
        OrdemDeServiço.os_abertas += 1 
        self.id_os = OrdemDeServiço.total_os_criadas

    def finalizar_os(self):
        if self.status == "concluída":
            print(f"A ordem de serviço #{self.id_os} já está concluída!")
            return

        self.status = "concluída"
        OrdemDeServiço.os_abertas -= 1
        print(f"A ordem de serviço do cliente {self.cliente} foi concluída com sucesso!")

    def verificar_ordens_abertas(self):
        print(f"Total de ordens abertas: {self.os_abertas}")
        return self.os_abertas


# Instanciando com 2 argumentos (cliente, descrição):
ordem1 = OrdemDeServiço("João", "Troca de tela")
ordem2 = OrdemDeServiço("Joyce", "Formatacao de PC")
ordem3 = OrdemDeServiço("John", "Manutencao")

ordem1.verificar_ordens_abertas()

print("---")

ordem2.finalizar_os()

print("---")

ordem1.verificar_ordens_abertas()