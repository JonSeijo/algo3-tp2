#encoding: utf-8

# Importe a mansalva, revisar

import os #listdir, path.join
import subprocess # Popen, communicate
import filecmp # cmp
import argparse
import random
import subprocess
import time

# Cada problema en un experimentos.py separado
# Es un gran copypaste de tester.py

ejecutable = "./tiempos3"
n_max_random = 100
repes_random = 50


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-random", help="Ejecuta el experimento: Random", action='store_true')
    args = parser.parse_args()

    if args.random:
        for n in range(2, n_max_random):
            # Guardar encabezado de csv
            # Para cada repes_random
                # Generar el input falopa en un archivo
                # Correr ejecutable con el input falopa
                # Guardar en un csv por linea
                #     n; tiempo;

