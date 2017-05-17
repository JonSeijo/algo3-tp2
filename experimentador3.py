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

repeticiones = 10
cota_valor_random = 2000

# Costo Random Existe Random (cr_er)
csv_cr_er = "./experimentos/problema3/costo_random_existe_random.csv"
n_max_cr_er = 50  #Aumentar
tipo_cr_er = "COSTO_RANDOM_EXISTE_RANDOM"

# Costo Igual Existe Random (ci_er)
csv_ci_er = "./experimentos/problema3/costo_igual_existe_random.csv"
n_max_ci_er = 50  #Aumentar
tipo_ci_er = "COSTO_IGUAL_EXISTE_RANDOM"

# Costo Igual Existe No (ci_en)
csv_ci_en = "./experimentos/problema3/costo_igual_existe_no.csv"
n_max_ci_en = 50  #Aumentar
tipo_ci_en = "COSTO_IGUAL_EXISTE_NO"

# Costo Igual Existe Si (ci_es)
csv_ci_es = "./experimentos/problema3/costo_igual_existe_si.csv"
n_max_ci_es = 50  #Aumentar
tipo_ci_es = "COSTO_IGUAL_EXISTE_SI"


# Para valores existe Random y costo Random
def save_input_cr_er(f, n):
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            existe = random.getrandbits(1)  # Valor aleatorio 0 o 1 para existe
            costo = random.randint(1, cota_valor_random) # Valor aleatorio entero para el peso
            f.write(str(i) + " " + str(j) + " " + str(existe) + " " + str(costo) + '\n')


# Para valores existe Random y costo Igual
def save_input_ci_er(f, n, costo):
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            existe = random.getrandbits(1)  # Valor aleatorio 0 o 1 para existe
            f.write(str(i) + " " + str(j) + " " + str(existe) + " " + str(costo) + '\n')


# Para valores iguales de costo y existe
def save_input(f, n, costo, existe):
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            f.write(str(i) + " " + str(j) + " " + str(existe) + " " + str(costo) + '\n')


# Genera un input del tipo en input_tmp de tamaño n
def generate_input(tipo, n):
    # aca guardo un input random en input_tmp de tamaño n
    with open(input_path_tmp, 'w') as f:
        f.write(str(n) + '\n')

        if tipo == tipo_cr_er:
            save_input_cr_er(f, n)
        elif tipo == tipo_ci_er:
            save_input_ci_er(f, n, 50) # Todo costo 50 arbitrario
        elif tipo == tipo_ci_en:
            save_input(f, n, 50, 0)
        elif tipo == tipo_ci_es:
            save_input(f, n, 50, 1)
        else:
            sys.exit("Tipo invalido en generacion de input")

        f.write("-1")



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
            # Generar el input falopa en un input_tmp
            generate_input(tipo, n)

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
    parser.add_argument("-cr_er", help="Experimento: Costo Random, Existe Random", action='store_true')
    # parser.add_argument("-cr_ei", help="Experimento: Costo Random, Existe Igual", action='store_true')
    parser.add_argument("-ci_er", help="Experimento: Costo Igual, Existe Random", action='store_true')
    parser.add_argument("-ci_es", help="Experimento: Costo Igual, Existe Si", action='store_true')
    parser.add_argument("-ci_en", help="Experimento: Costo Igual, Existe No", action='store_true')
    args = parser.parse_args()

    if not len(sys.argv) > 1:
        sys.exit("No arguments passed! Use -h flag for help")

    if args.todos:
            experimentar(csv_cr_er, n_max_cr_er, tipo_cr_er)
            # experimentar(csv_cr_ei, n_max_cr_ei, tipo_cr_ei)
            experimentar(csv_ci_er, n_max_ci_er, tipo_ci_er)
            experimentar(csv_ci_en, n_max_ci_en, tipo_ci_en)
            experimentar(csv_ci_es, n_max_ci_es, tipo_ci_es)

    else:
        if args.cr_er:
            experimentar(csv_cr_er, n_max_cr_er, tipo_cr_er)
        # if args.cr_ei:
            # experimentar(csv_cr_ei, n_max_cr_ei, tipo_cr_ei)
        if args.ci_er:
            experimentar(csv_ci_er, n_max_ci_er, tipo_ci_er)
        if args.ci_es:
            experimentar(csv_ci_es, n_max_ci_es, tipo_ci_es)
        if args.ci_en:
            experimentar(csv_ci_en, n_max_ci_en, tipo_ci_en)

