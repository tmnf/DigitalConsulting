from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .webservice import serializers
from .models import Solution
from .integration import FrameworkIntegration

from .entities import *

problems = []


def index(request):
    if request.method == "POST":
        name = request.POST.get('nome')
        tipo = request.POST.get('type')

        objectives = request.POST.get('objectives')
        variables = request.POST.get('variables')
        variables_array = []

        for line in variables.splitlines():
            variable_data = line.split(" ")
            variables_array.append(Variable(variable_data[0], variable_data[1], variable_data[2]))

        method = request.POST.get('method')
        file = "evaluate.jar"

        size = request.POST.get('size')

        if not name or not tipo or not variables or not method or not file or not size or not objectives:
            return render(request, 'index.html')

        problems.append(Problem(name, tipo, variables_array, objectives, method, file, size))

        context = {"problems": problems}

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')


def show_results(request):
    if request.method == 'POST':
        FrameworkIntegration.run_algorithm('DigitalPlatform/integration/framework.jar', problems)
        lines = FrameworkIntegration.read_output(
            'ADS-Solutions-And-Results/ADS/data/ADS/' + problems[0].nome + '/FUN0.tsv')

        qualities = []

        # Alterar isto para aceitar varios problemas
        q = Quality(problems[0].nome, lines)
        # q.solutions_quality.sort(custom_sort)
        qualities.append(q)

        context = {'qualities': qualities}
        return render(request, 'results.html', context)

    return render(request, 'index.html')


def custom_sort(line1, line2):
    m1 = 0
    for value in line1.split():
        m1 += float(value)

    m1 = m1 / (len(line1.split()))

    m2 = 0
    for value in line2.split():
        m2 += float(value)

    m2 = m2 / (len(line2.split()))

    offset = 1
    if problems[0].better == "Menor":
        offset = -1

    if m1 > m2:
        return 1 * offset
    elif m1 == m2:
        return 0
    else:
        return -1 * offset


def show_purchase(request):
    if request.method == 'POST':
        lines = FrameworkIntegration.read_output(
            'ADS-Solutions-And-Results/ADS/data/ADS/' + problems[0].nome + '/VAR0.tsv')

        solutions = []

        s = Solution(problems[0].nome, lines)
        # s.solutions.sort(custom_sort)
        solutions.append(s)

        context = {'solutions': solutions}
        return render(request, 'purchase.html', context)

    return render(request, 'results.html')


# WebService Views

@api_view(['GET', 'POST'])
def solution_rest_api(request, problem, num_variables, final):
    framework_executable = 'DigitalPlatform/integration/framework.jar'
    framework_output = 'ADS-Solutions-And-Results/ADS/data/ADS/Kursawe/FUN0.tsv'
    keyword = 'qualities'

    if final == "true":
        framework_output = 'ADS-Solutions-And-Results/ADS/data/ADS/Kursawe/VAR0.tsv'
        keyword = 'solutions'

    # Para testar o get usar os links:
    #       * http://127.0.0.1:8000/solutions/TesteTiago/?format=api (Em formato pesquisavel)
    #       * http://127.0.0.1:8000/solutions/TesteTiago/?format=json (Em formato json)

    # O GET ESTA APENAS EM CODIGO DE TESTE
    if request.method == 'GET':
        solutions = []

        if num_variables != 0:
            FrameworkIntegration.run_algorithm(framework_executable, num_variables)

            for x in FrameworkIntegration.read_output(framework_output):
                solutions.append(Solution(problem=problem, variables=x))

        serializer = serializers.SolutionSerializer(solutions, many=True)

        final_response = {'problem': problem,
                          'number_of_solutions': len(solutions),
                          keyword: serializer.data}

        return Response(final_response)
    else:
        # AQUI SERA ACEITA O REQUEST POST DO UTILIZADOR, GERADAS AS SOLUÇOES E DEVOLVIDAS.
        return Response(serializers.SolutionSerializer.errors, status=400)
