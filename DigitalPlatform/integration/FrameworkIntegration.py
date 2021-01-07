# This class will handle all integration with the Java Framework (Currently in Test)
# Author: Tiago Farinha

from ..entities import *

import subprocess, os, json, shutil


# Executes the Framework's Algorithm
def run_algorithm(path_to_jar, problems):
    print("A executar algoritmo...")

    json_problems = problems_to_json(problems)

    with open('data.json', 'w') as f:
        f.write(json_problems)

    try:
        subprocess.call(["java", "-jar", path_to_jar])

        if os.path.exists('jMetal.log'):
            os.remove("jMetal.log")

        print("Algoritmo executado com sucesso!\n\n")
    except Exception as e:
        print("Erro ao executar algoritmo: " + str(e))


def problems_to_json(problems):
    return json.dumps({"problems": problems}, cls=CustomEncoder).replace("\\", "").replace('"{', "{").replace('}"', "}")


# Reads the Last Algorithm's Output If Exists
def read_output(output_path):
    output = []
    if os.path.exists(output_path):
        with open(output_path) as f:
            output = f.readlines()
            output = [x.strip() for x in output]

            f.close()

        if "VAR" not in output_path:
            os.remove(output_path)
    return output
