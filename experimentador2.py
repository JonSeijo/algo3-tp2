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
n_max = 100 # Aumentar

# Todo random
csv_random_todo = "./experimentos/problema2/random_todo.csv"
n_max_random_todo = n_max
tipo_random_todo = "RANDOM_TODO"

# Minima cant posible de aristas (Sale 1 de cada una)
csv_aristas_minimas = "./experimentos/problema2/aristas_minimas.csv"
n_max_aristas_minimas = n_max
tipo_aristas_minimas = "ARISTAS_MINIMAS"

# Maxima cant posible de aristas (Salen n-1 de cada una)
csv_aristas_maximas = "./experimentos/problema2/aristas_maximas.csv"
n_max_aristas_maximas = n_max
tipo_aristas_maximas = "ARISTAS_MAXIMAS"


def save_input_random_costos(f, n, outdegree):
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
            save_input_random_costos(f, n, outdegree)
        elif tipo == tipo_aristas_minimas:
            # outdegree es fijo y es lo que da la cant de aristas de salida
            save_input_random_costos(f, n, outdegree)
        elif tipo == tipo_aristas_maximas:
            # outdegree es fijo y es lo que da la cant de aristas de salida
            save_input_random_costos(f, n, outdegree)
        else:
            sys.exit("Tipo invalido en generacion de input")

        f.write("-1 -1")


def create_outdegree(n, tipo):
    if tipo == tipo_random_todo:
        outdegree = [random.randint(1, n-1) for _ in range(n+1)]
    elif tipo == tipo_aristas_minimas:
        outdegree = [1 for _ in range(n+1)]
    elif tipo == tipo_aristas_maximas:
        outdegree = [n-1 for _ in range(n+1)]
    else:
        sys.exit("Tipo invalido en generacion de outdegree")

    return outdegree


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

            outdegree = create_outdegree(n, tipo)
            m = sum(outdegree[1:])

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
    parser.add_argument("-aristas_minimas", help="Experimento: Minima cantidad de aristas", action='store_true')
    parser.add_argument("-aristas_maximas", help="Experimento: Maxima cantidad de aristas", action='store_true')
    args = parser.parse_args()

    if not len(sys.argv) > 1:
        sys.exit("No arguments passed! Use -h flag for help")

    if args.todos:
            experimentar(csv_random_todo, n_max_random_todo, tipo_random_todo)
            experimentar(csv_aristas_minimas, n_max_aristas_minimas, tipo_aristas_minimas)
            experimentar(csv_aristas_maximas, n_max_aristas_maximas, tipo_aristas_maximas)

    else:
        if args.random_todo:
            experimentar(csv_random_todo, n_max_random_todo, tipo_random_todo)
        if args.aristas_minimas:
            experimentar(csv_aristas_minimas, n_max_aristas_minimas, tipo_aristas_minimas)
        if args.aristas_maximas:
            experimentar(csv_aristas_maximas, n_max_aristas_maximas, tipo_aristas_maximas)
