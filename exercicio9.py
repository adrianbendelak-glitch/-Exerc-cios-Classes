class Livro:
    def __init__(self, titulo:str, autor:str, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Livro: O '{self.titulo}' do Autor {self.autor} com ({self.paginas} paginas)"

    def comparar_tamanho(livro1, livro2):
        if livro1.paginas > livro2.paginas:
            print(f"O livro '{livro1.titulo}' é menor que o comparado.")
        elif livro1.paginas < livro2.paginas:
            print(f"O livro '{livro1.titulo}' é maior que o comparado.")
        else:
            print(f"O livro '{livro1.titulo}' tem o mesmo tamanho que o comparado.")

livro1 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 96)
print(livro1)
livro2 = Livro("1984", "George Orwell", 328)
print(livro2)
livro1.comparar_tamanho(livro2)
