import json


class Problem:

    def __init__(self, nome, tipo, variaveis, objectives, method, file, better):
        self.nome = nome
        self.tipo = tipo
        self.variaveis = variaveis
        self.objectives = objectives
        self.method = method
        self.file = file
        self.better = better

    def toJSON(self):
        return json.dumps(self.__dict__, cls=CustomEncoder)


class Quality:

    def __init__(self, problem, solutions_quality):
        self.problem = problem
        self.solutions_quality = solutions_quality


class Solution:

    def __init__(self, problem, solutions):
        self.problem = problem
        self.solutions = solutions


class Variable:

    def __init__(self, name, max, min):
        self.name = name
        self.max = max
        self.min = min

    def __str__(self):
        return self.name + " " + self.max + " " + self.min

    def toJSON(self):
        return json.dumps(self.__dict__)


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Problem) or isinstance(obj, Variable):
            return obj.toJSON()

        return json.JSONEncoder.default(self, obj)
