import os #listdir, path.join
import subprocess # Popen, communicate
import sys # exit
import filecmp # cmp

print("")

for nro in (1, 2, 3): 

    # PREPARACIÓN ---
    directory = "./tests/problema" + str(nro)
    executable = "./solucion" + str(nro)

    # Intro
    print("PROBLEMA " + str(nro))

    # Verificación de la existencia del ejecutable
    if not os.path.isfile(executable):
        print(" Warning: no existe ejecutable en la ruta {}".format(executable))
        print(" Continuando...\n")
        continue

    # Limpieza de salidas viejas
    outputs = [f for f in os.listdir(directory) if f.endswith(".out")]
    for filename in outputs:
        os.remove(os.path.join(directory, filename))


    # GENERACIÓN DE SALIDAS ---
    inputs = sorted([f for f in os.listdir(directory) if f.endswith(".in")])
    for filename in inputs:
        # Inicialización de rutas
        base_path = os.path.join(directory, os.path.splitext(filename)[0])
        in_path = base_path + ".in"
        out_path = base_path + ".out"
        expected_path = base_path + ".expected"

        # Verificación de que el '.expected' correspondiente existe
        if not os.path.isfile(expected_path):
            print("Warning: el archivo {} no tiene un '.expected' correspondiente".format(filename))
            continue

        # Ejecución del programa
        in_file = open(in_path, 'r')
        out_file = open(out_path, 'w')
        err_file = open(os.devnull, 'w')
        cmd = [executable]
        p = subprocess.Popen(cmd, stdin=in_file, stdout=out_file, stderr=err_file)
        p.wait() # TODO catch expectionTimeOut
        in_file.close()
        out_file.close()


    # FALTA DE TESTS
    if len(inputs) == 0:
        print(" --")


    # COMPARACIÓN DE RESULTADOS ---
    outputs = sorted([f for f in os.listdir(directory) if f.endswith(".out")])
    for filename in outputs:
        # Inicialización de rutas
        plain_name = os.path.splitext(filename)[0]
        base_path = os.path.join(directory, plain_name)
        out_path = base_path + ".out"
        expected_path = base_path + ".expected"

        # Comparación
        iguales = True

        out_file = open(out_path, 'r')
        expected_file = open(expected_path, 'r')

        out_line = out_file.readline().rstrip()
        exp_line = expected_file.readline().rstrip()
        while out_line != '' and exp_line != '':
            if out_line != exp_line:
                iguales = False
            out_line = out_file.readline().rstrip()
            exp_line = expected_file.readline().rstrip()
        out_file.close()
        expected_file.close()

        # Mensaje
        if (iguales):
            print(" Test {0}: OK".format(plain_name))
        else:
            print(" Test {0}: FAILED".format(plain_name))
    print("")