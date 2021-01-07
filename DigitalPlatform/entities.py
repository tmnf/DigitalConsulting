class Problem:

    def __init__(self, nome, tipo, variaveis, method, file):
        self.nome = nome
        self.tipo = tipo
        self.variaveis = variaveis
        self.method = method
        self.file = file


class Quality:

    def __init__(self, problem, solutions_quality):
        self.problem = problem
        self.solutions_quality = solutions_quality
