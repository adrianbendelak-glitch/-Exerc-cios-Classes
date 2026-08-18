class OrdemDeServiço:
    total_os_criadas = 0
    os_abertas = 0
    status = "Aberta"

    def __init__(self, cliente:str, descrição:str):
        self.cliente = cliente
        self.descrição = descrição
        OrdemDeServiço.total_os_criadas += 1
        OrdemDeServiço.os_abertas += 1 
        self.id_os = OrdemDeServiço.total_os_criadas

    def finalizar_os(self):
        self.status = "concluída"
        OrdemDeServiço.os_abertas -= 1
        print(f"A ordem de serviço do cliente {self.cliente} foi concluída com sucesso!")

    def __init__(self):
        self.ordem1 = OrdemDeServiço("João", "Ryan", "lucas")
        self.ordem2 = OrdemDeServiço("Joyce", "Maria", "lucca")
        self.ordem3 = OrdemDeServiço("John", "Robert", "luiza")

    def verificação(self):
        