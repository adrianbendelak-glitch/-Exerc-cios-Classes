# Lista de gabaritos para diferentes provas
GABARITOS = [
    ["A", "B", "C", "D", "A"],  # Prova 1
    ["B", "B", "D", "A", "C"],  # Prova 2
    ["C", "A", "C", "D", "B"]   # Prova 3
]

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.historico_notas = []  # Armazena todas as notas do aluno

    def fazer_prova(self, respostas, gabarito):
        if len(respostas) != len(gabarito):
            print("Erro: O número de respostas deve ser igual ao número de questões do gabarito.")
            return

        acertos = 0
        for i in range(len(gabarito)):
            if respostas[i].upper() == gabarito[i].upper():
                acertos += 1

        # Calcula a nota (exemplo: cada questão vale 2 pontos se forem 5 questões)
        nota = (acertos / len(gabarito)) * 10
        self.historico_notas.append(nota)
        print(f"Prova realizada por {self.nome}. Nota obtida: {nota:.1f}")

    def calcular_media(self):
        if not self.historico_notas:
            return 0.0
        
        soma = 0
        for nota in self.historico_notas:
            soma += nota
        
        return soma / len(self.historico_notas)

    def ver_boletim(self):
        media = self.calcular_media()
        situacao = "Aprovado" if media >= 6.0 else "Reprovado"

        # Formata as notas para exibição simples (ex: [8.0, 6.0, 10.0])
        notas_formatadas = [round(n, 1) for n in self.historico_notas]

        print("\n==========================================")
        print("             BOLETIM ESCOLAR              ")
        print("==========================================")
        print(f"Aluno: {self.nome}")
        print(f"Notas: {notas_formatadas}")
        print(f"Média Final: {media:.1f}")
        print(f"Situação: {situacao}")
        print("==========================================\n")


# ==========================================
# EXECUÇÃO NO TERMINAL
# ==========================================
if __name__ == "__main__":
    # Instanciando o aluno
    aluno1 = Aluno("Carlos Silva")

    # Respostas do aluno para cada prova
    respostas_prova1 = ["A", "B", "C", "D", "D"]  # Errou 1 -> Nota 8.0
    respostas_prova2 = ["B", "B", "A", "A", "C"]  # Errou 1 -> Nota 8.0
    respostas_prova3 = ["A", "A", "B", "D", "B"]  # Errou 2 -> Nota 6.0

    print("--- REALIZANDO AS PROVAS ---")
    aluno1.fazer_prova(respostas_prova1, GABARITOS[0])
    aluno1.fazer_prova(respostas_prova2, GABARITOS[1])
    aluno1.fazer_prova(respostas_prova3, GABARITOS[2])

    # Exibindo o boletim final
    aluno1.ver_boletim()