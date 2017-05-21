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

repeticiones = 25
cota_sup_valor_random = 10000
n_max = 75 # Aumentar

# Arista_random_premium_random
csv_arista_random_premium_random = "./experimentos/problema1/arista_random_premium_random.csv"
n_max_arista_random_premium_random = 25
tipo_arista_random_premium_random = "arista_random_premium_random"

# Arista_random_premium_maximas
csv_arista_random_premium_maximas = "./experimentos/problema1/arista_random_premium_maximas.csv"
n_max_arista_random_premium_maximas = 25
tipo_arista_random_premium_maximas = "arista_random_premium_maximas"

# Arista_random_premium_minimas
csv_arista_random_premium_minimas = "./experimentos/problema1/arista_random_premium_minimas.csv"
n_max_arista_random_premium_minimas = 85
tipo_arista_random_premium_minimas = "arista_random_premium_minimas"

# Arista_random_premium_25
csv_arista_random_premium_25 = "./experimentos/problema1/arista_random_premium_25.csv"
n_max_arista_random_premium_25 = 30
tipo_arista_random_premium_25 = "arista_random_premium_25"


# Ninguna es premium
def save_input_arista_random_premium_minimas(f, aristas):
    for eje in aristas:
        premium = 0
        costo = random.randint(1, cota_sup_valor_random)
        f.write(str(eje[0]) + ' ' + str(eje[1]) +  ' ' + str(premium) + ' ' + str(costo) + '\n')

# Todas son premiums
def save_input_arista_random_premium_maximas(f, aristas):
    for eje in aristas:
        premium = 1
        costo = random.randint(1, cota_sup_valor_random)
        f.write(str(eje[0]) + ' ' + str(eje[1]) +  ' ' + str(premium) + ' ' + str(costo) + '\n')


# Random si es premium o no
def save_input_arista_random_premium_random(f, aristas):
    for eje in aristas:
        premium = random.randint(0, 1)
        costo = random.randint(1, cota_sup_valor_random)
        f.write(str(eje[0]) + ' ' + str(eje[1]) +  ' ' + str(premium) + ' ' + str(costo) + '\n')

# El 25% son premiums
def save_input_arista_random_premium_25(f, aristas):
    for eje in aristas:
        if random.random() < 0.25:
            premium = 1
        else:
            premium = 0
        costo = random.randint(1, cota_sup_valor_random)
        f.write(str(eje[0]) + ' ' + str(eje[1]) +  ' ' + str(premium) + ' ' + str(costo) + '\n')



# Genera un input del tipo en input_tmp de tamaño n
def generate_input(tipo, n, aristas, k):
    # aca guardo un input random en input_tmp de tamaño n
    with open(input_path_tmp, 'w') as f:
        f.write(str(n) + ' ' + str(len(aristas)) + '\n')
        f.write(str(1) + ' ' + str(n) + ' ' + str(k) + '\n')

        if tipo == tipo_arista_random_premium_random:
            save_input_arista_random_premium_random(f, aristas)
        elif tipo == tipo_arista_random_premium_minimas:
            save_input_arista_random_premium_minimas(f, aristas)
        elif tipo == tipo_arista_random_premium_maximas:
            save_input_arista_random_premium_maximas(f, aristas)
        elif tipo == tipo_arista_random_premium_25:
            save_input_arista_random_premium_25(f, aristas)
        else:
            sys.exit("Tipo invalido en generacion de input")

        f.write("-1 -1")


def generar_aristas(tipo, n):
    if (tipo == tipo_arista_random_premium_random
        or tipo == tipo_arista_random_premium_minimas
        or tipo == tipo_arista_random_premium_maximas
        or tipo == tipo_arista_random_premium_25):
        # Generar un m random
        m = random.randint(n-1, n*(n-1)/2)
        # De todas las aristas posibles tomar m
        return random.sample([(i, j) for i in range(1, n+1) for j in range(i+1, n+1)], m)
    else:
        sys.exit("Tipo invalido en generacion de input")


def generar_k(tipo, n):
    if (tipo == tipo_arista_random_premium_random
        or tipo == tipo_arista_random_premium_minimas
        or tipo == tipo_arista_random_premium_maximas
        or tipo == tipo_arista_random_premium_25):

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
    parser.add_argument("-arista_random_premium_minimas", help="Aristas random. K Random. Premium 0", action='store_true')
    parser.add_argument("-arista_random_premium_random", help="Aristas random. K Random. Premium random", action='store_true')
    parser.add_argument("-arista_random_premium_maximas", help="Aristas random. K Random. Premium todas", action='store_true')
    parser.add_argument("-arista_random_premium_25", help="Aristas random. K Random. Premium 25%", action='store_true')
    args = parser.parse_args()

    if not len(sys.argv) > 1:
        sys.exit("No arguments passed! Use -h flag for help")

    if args.todos:
        experimentar(csv_arista_random_premium_minimas, n_max_arista_random_premium_minimas, tipo_arista_random_premium_minimas)
        experimentar(csv_arista_random_premium_random, n_max_arista_random_premium_random, tipo_arista_random_premium_random)
        experimentar(csv_arista_random_premium_maximas, n_max_arista_random_premium_maximas, tipo_arista_random_premium_maximas)
        experimentar(csv_arista_random_premium_25, n_max_arista_random_premium_25, tipo_arista_random_premium_25)

    else:
        if args.arista_random_premium_random:
            experimentar(csv_arista_random_premium_random, n_max_arista_random_premium_random, tipo_arista_random_premium_random)
        if args.arista_random_premium_minimas:
            experimentar(csv_arista_random_premium_minimas, n_max_arista_random_premium_minimas, tipo_arista_random_premium_minimas)
        if args.arista_random_premium_maximas:
            experimentar(csv_arista_random_premium_maximas, n_max_arista_random_premium_maximas, tipo_arista_random_premium_maximas)
        if args.arista_random_premium_25:
            experimentar(csv_arista_random_premium_25, n_max_arista_random_premium_25, tipo_arista_random_premium_25)
