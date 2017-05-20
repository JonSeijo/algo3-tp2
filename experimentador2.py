#encoding: utf-8

# Importe a mansalva, revisar

import os #listdir, path.join
import subprocess # Popen, communicate
import filecmp # cmp
import argparse
import random
import subprocess
import time
import sys
import random

# Cada problema en un experimentos.py separado
ejecutable_tiempos = "./tiempo2"

# InputFile donde se van a guardar cada instancia que se ejecute
input_path_tmp = "./experimentos/input.tmp"

repeticiones = 10
cota_inf_valor_random = 1
cota_sup_valor_random = 100000
n_max = 50 # Aumentar

# Todo random
csv_random_todo = "./experimentos/problema2/random_todo.csv"
n_max_random_todo = n_max
tipo_random_todo = "RANDOM_TODO"


def save_input_random_todo(f, n, outdegree):
    for i in range(1, n+1):
        precio = random.randint(cota_inf_valor_random, cota_sup_valor_random)
        pool = [j for j in range(1, n+1) if j != i]
        vecinos = random.sample(pool, outdegree[i])

        for v in vecinos:
            f.write(str(i) + ' ' + str(v) +  ' ' + str(precio) + '\n')


# Genera un input del tipo en input_tmp de tamaño n
def generate_input(tipo, n, m, outdegree):
    # aca guardo un input random en input_tmp de tamaño n
    with open(input_path_tmp, 'w') as f:
        f.write(str(n) + ' ' + str(m) + '\n')

        if tipo == tipo_random_todo:
            save_input_random_todo(f, n, outdegree)
        else:
            sys.exit("Tipo invalido en generacion de input")

        f.write("-1 -1")


# Experimentacion generica, el input es lo que varia dependiendo de los parametros que se le pasen
def experimentar(csv_filename, n_max, tipo):
    # Guardar encabezado de csv
    with open(csv_filename, 'w') as csv :
        csv.write("n,tiempo" + '\n')

    # Para cada tamaño
    for n in range(2, n_max):
        print(tipo + " - n actual: " + str(n))
        # Para cada repes_random de cada tamaño
        for repe in range(repeticiones):

            if tipo_random_todo:
                outdegree = [random.randint(1, n-1) for _ in range(n+1)]
                m = sum(outdegree[1:])
            else:
                sys.exit("Tipo invalido en generacion de outdegree")

            # Generar el input falopa en un input_tmp
            generate_input(tipo, n, m, outdegree)

            with open(input_path_tmp) as input_file:
                # Correr ejecutable con el input falopa
                # Guarda tiempo en output, ignora stderr (Python3!)
                tiempo = subprocess.check_output(
                            [ejecutable_tiempos], stdin=input_file, stderr=subprocess.DEVNULL
                        ).decode(sys.stdout.encoding)

            # Guardar en un csv
            # Cada linea: n; tiempo;
            with open(csv_filename, 'a') as csv :
                csv.write(str(n) + "," + tiempo + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-todos", help="TODOS LOS EXPERIMENTOS", action='store_true')
    parser.add_argument("-random_todo", help="Experimento: Random todo", action='store_true')
    args = parser.parse_args()

    if not len(sys.argv) > 1:
        sys.exit("No arguments passed! Use -h flag for help")

    if args.todos:
            experimentar(csv_random_todo, n_max_random_todo, tipo_random_todo)

    else:
        if args.random_todo:
            experimentar(csv_random_todo, n_max_random_todo, tipo_random_todo)
