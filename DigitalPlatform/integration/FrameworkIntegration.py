# This class will handle all integration with the Java Framework (Currently in Test)
# Author: Tiago Farinha

import subprocess, os


# Executes the Framework's Algorithm
def run_algorithm(path_to_jar, num_of_variables):
    print("A executar algoritmo...")
    try:
        subprocess.call(["java", "-jar", path_to_jar, str(num_of_variables)])

        if os.path.exists('jMetal.log'):
            os.remove("jMetal.log")

        print("Algoritmo executado com sucesso!\n\n")
    except Exception as e:
        print("Erro ao executar algoritmo: " + str(e))


# Reads the Last Algorithm's Output If Exists
def read_output(output_path):
    output = []
    if os.path.exists(output_path):
        with open(output_path) as f:
            output = f.readlines()
            output = [x.strip() for x in output]

            f.close()

        os.remove(output_path)
    return output
