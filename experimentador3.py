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

# Cada problema en un experimentos.py separado
# Es un gran copypaste de tester.py

ejecutable = "./tiempos3"

csv_random = "./experimentos/problema3/random.csv"
repes_random = 50
n_max_random = 100
tipo_random = "RANDOM"

# Experimentacion generica, que varia dependiendo de los parametros que se le pasen
def experimentar(csv, repes, n_max, tipo):
    # Guardar encabezado de csv
    # Para cada repes_random
        # Generar el input falopa en un archivo
        # Correr ejecutable con el input falopa
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

