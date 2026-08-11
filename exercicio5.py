class Produto:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def reduzir_estoque(self, quantidade: int):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        else:
            print(f"[!] Estoque insuficiente para '{self.nome}'. Disponível: {self.estoque}")
            return False


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []  # Lista para armazenar tuplas (produto, quantidade)

    def adicionar_ao_carrinho(self, produto: Produto, quantidade: int):
        if quantidade <= 0:
            print("[!] A quantidade deve ser maior que zero.")
            return

        # Tenta reduzir do estoque antes de colocar no carrinho
        if produto.reduzir_estoque(quantidade):
            self.produtos.append((produto, quantidade))
            print(f"[+] {quantidade}x '{produto.nome}' adicionado(s) ao carrinho!")

    def mostrar_carrinho(self):
        print("\n==========================================")
        print("          CARRINHO DE COMPRAS             ")
        print("==========================================")

        if not self.produtos:
            print("O carrinho está vazio.")
            print("==========================================\n")
            return

        total_geral = 0.0

        for produto, quantidade in self.produtos:
            subtotal = produto.preco * quantidade
            total_geral += subtotal
            print(f"- {produto.nome} | Qtd: {quantidade} | Un: R$ {produto.preco:.2f} | Subtotal: R$ {subtotal:.2f}")

        print("------------------------------------------")
        print(f"TOTAL DA COMPRA: R$ {total_geral:.2f}")
        print("==========================================\n")


# ==========================================
# EXECUÇÃO NO TERMINAL
# ==========================================
if __name__ == "__main__":
    print("--- INICIANDO SISTEMA DE COMPRAS ---\n")

    # 1. Cadastrando produtos no estoque
    notebook = Produto("Notebook", 3500.00, 5)
    mouse = Produto("Mouse Gamer", 150.00, 10)
    teclado = Produto("Teclado Mecânico", 250.00, 2)

    # 2. Criando o carrinho de compras
    meu_carrinho = CarrinhoDeCompras()

    # 3. Adicionando itens ao carrinho
    meu_carrinho.adicionar_ao_carrinho(notebook, 1)
    meu_carrinho.adicionar_ao_carrinho(mouse, 2)

    # 4. Tentando comprar mais do que tem no estoque (Teclado só tem 2)
    meu_carrinho.adicionar_ao_carrinho(teclado, 3)

    # 5. Exibindo o conteúdo e o total do carrinho
    meu_carrinho.mostrar_carrinho()

    # 6. Verificando o estoque restante dos produtos
    print("--- ESTOQUE RESTANTE ---")
    print(f"{notebook.nome}: {notebook.estoque} unidades")
    print(f"{mouse.nome}: {mouse.estoque} unidades")
    print(f"{teclado.nome}: {teclado.estoque} unidades")