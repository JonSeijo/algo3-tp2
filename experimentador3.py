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

ejecutable_tiempos = "./tiempo3"

# InputFile donde se van a guardar cada instancia que se ejecute
input_path_tmp = "./experimentos/input.tmp"

# Variables para experimentar con instancias random
csv_random = "./experimentos/problema3/random.csv"
repes_random = 15
n_max_random = 20 # Solo hasta 20 para testear rapido, aumentarlo!
cota_peso_random = 2000
tipo_random = "RANDOM"

# Genera un input del tipo en input_tmp de tamaño n
def generate_input(tipo, n):
    if tipo == tipo_random:
        # aca guardo un input random en input_tmp de tamaño n
        print("Deberia generar input tam " + str(n))
        with open(input_path_tmp, 'w') as f:
            f.write(str(n) + '\n')
            for i in range(1, n+1):
                for j in range(i+1, n+1):
                    # Valor aleatorio 0 o 1
                    existe = random.getrandbits(1)
                    # Valor aleatorio entero para el peso
                    costo = random.randint(1, cota_peso_random)

                    f.write(str(i) + " " + str(j) + " " + str(existe) + " " + str(costo) + '\n')

            f.write("-1")

    else:
        sys.exit("Tipo invalido en generacion de input")


# Experimentacion generica, el input es lo que varia dependiendo de los parametros que se le pasen
def experimentar(csv_filename, repes, n_max, tipo):
    # Guardar encabezado de csv
    with open(csv_filename, 'w') as csv :
        csv.write("n;tiempo;" + '\n')

    # Para cada tamaño
    for n in range(2, n_max):
        # Para cada repes_random de cada tamaño
        for repe in range(repes):
            # Generar el input falopa en un input_tmp
            generate_input(tipo, n)

            with open(input_path_tmp) as input_file:
                # Correr ejecutable con el input falopa
                # Guarda tiempo en output, ignora stderr (Python3!)
                output = subprocess.check_output(
                            [ejecutable_tiempos], stdin=input_file, stderr=subprocess.DEVNULL
                        ).decode(sys.stdout.encoding)

                print(output)

                # Guardar en un csv por linea
                #     n; tiempo;

    print ("Experimento random")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-random", help="Ejecuta el experimento: Random", action='store_true')
    args = parser.parse_args()

    if not len(sys.argv) > 1:
        sys.exit("No arguments passed! Use -h flag for help")

    if args.random:
        experimentar(csv_random, repes_random, n_max_random, tipo_random)
