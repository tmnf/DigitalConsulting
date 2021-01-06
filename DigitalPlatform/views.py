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
        tipo = request.POST.get('tipo')
        variables = request.POST.get('variables')
        method = "jarfile"
        # file = request.POST.get('file')
        file = "evaluate.jar"

        problems.append(Problem(name, tipo, variables, method, file))

        context = {"problems": problems}

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')


def show_results(request):
    if request.method == 'POST':
        qualities = [Quality("Teste 123", ["10 50", "13 20"])]  # Vai receber do metodo de integração

        context = {'qualities': qualities}
        return render(request, 'results.html', context)

    return render(request, 'index.html')


def show_purchase(request):
    if request.method == 'POST':
        qualities = [Quality("Teste 123", ["10 50", "13 20"])]  # Vai receber do metodo de integração

        context = {'qualities': qualities}
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
