class OrdemDeServiço:
    total_os_criadas = 0
    os_abertas = 0

    def __init__(self, cliente: str, descrição: str):
        self.cliente = cliente
        self.descrição = descrição
        self.status = "Aberta"  
        
        OrdemDeServiço.total_os_criadas += 1
        OrdemDeServiço.os_abertas += 1 
        self.id_os = OrdemDeServiço.total_os_criadas

    def finalizar_os(self):
        if self.status == "concluída":
            print(f"A ordem de serviço #{self.id_os} já está concluída!")
            return

        self.status = "concluída"
        OrdemDeServiço.os_abertas -= 1
        print(f"A ordem de serviço #{self.id_os} do cliente '{self.cliente}' foi concluída com sucesso!")

    @classmethod
    def verificar_ordens_abertas(cls):
        print(f"\nTotal de ordens abertas: {cls.os_abertas}")
        return cls.os_abertas


def menu():
    lista_os = []

    while True:
        print("\n--- SISTEMA DE ORDEM DE SERVIÇO ---")
        print("1. Criar nova Ordem de Serviço")
        print("2. Listar todas as Ordens de Serviço")
        print("3. Finalizar uma Ordem de Serviço")
        print("4. Verificar quantidade de OS abertas")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            cliente = input("Nome do cliente: ").strip()
            descricao = input("Descrição do serviço: ").strip()
            if cliente and descricao:
                nova_os = OrdemDeServiço(cliente, descricao)
                lista_os.append(nova_os)
                print(f"OS #{nova_os.id_os} criada para {cliente}!")
            else:
                print("Cliente e descrição são obrigatórios.")

        elif opcao == "2":
            if not lista_os:
                print("\nNenhuma Ordem de Serviço cadastrada.")
            else:
                print("\n--- LISTA DE ORDENS DE SERVIÇO ---")
                for os in lista_os:
                    print(f"ID: #{os.id_os} | Cliente: {os.cliente} | Serviço: {os.descrição} | Status: {os.status}")

        elif opcao == "3":
            if not lista_os:
                print("\nNenhuma OS cadastrada para finalizar.")
                continue

            try:
                id_busca = int(input("Digite o ID da OS que deseja finalizar: "))
                encontrada = False
                for os in lista_os:
                    if os.id_os == id_busca:
                        os.finalizar_os()
                        encontrada = True
                        break
                if not encontrada:
                    print(f"Ordem de Serviço #{id_busca} não encontrada.")
            except ValueError:
                print("Por favor, digite um número de ID válido.")

        elif opcao == "4":
            OrdemDeServiço.verificar_ordens_abertas()

        elif opcao == "5":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()