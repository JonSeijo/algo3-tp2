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
ejecutable_tiempos = "./tiempo1"

# InputFile donde se van a guardar cada instancia que se ejecute
input_path_tmp = "./experimentos/input.tmp"

repeticiones = 10
cota_sup_valor_random = 10000
n_max = 15 # Aumentar

# Todo random
csv_random_todo = "./experimentos/problema1/random_todo.csv"
n_max_random_todo = n_max
tipo_random_todo = "RANDOM_TODO"


def save_input_random_todo(f, aristas):
    for eje in aristas:
        premium = random.randint(0, 1)
        costo = random.randint(1, cota_sup_valor_random)
        f.write(str(eje[0]) + ' ' + str(eje[1]) +  ' ' + str(premium) + ' ' + str(costo) + '\n')

# Genera un input del tipo en input_tmp de tamaño n
def generate_input(tipo, n, aristas, k):
    # aca guardo un input random en input_tmp de tamaño n
    with open(input_path_tmp, 'w') as f:
        f.write(str(n) + ' ' + str(len(aristas)) + '\n')
        f.write(str(1) + ' ' + str(n) + ' ' + str(k) + '\n')

        if tipo == tipo_random_todo:
            save_input_random_todo(f, aristas)
        else:
            sys.exit("Tipo invalido en generacion de input")

        f.write("-1 -1")


def generar_aristas(tipo, n):
    if tipo == tipo_random_todo:

        # Generar un m random
        m = random.randint(n-1, n*(n-1)/2)

        # De todas las aristas posibles tomar m
        return random.sample([(i, j) for i in range(1, n+1) for j in range(i+1, n+1)], m)

    else:
        sys.exit("Tipo invalido en generacion de input")


def generar_k(tipo, n):
    if tipo == tipo_random_todo:
        return random.randint(1, n*(n-1)/2)
    else:
        sys.exit("Tipo invalido en generacion de input")


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

            # Todas las aristas finales
            aristas = generar_aristas(tipo, n)
            k = generar_k(tipo, n)

            # Generar el input falopa en un input_tmp
            generate_input(tipo, n, aristas, k)

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
