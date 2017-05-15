import os #listdir, path.join
import subprocess # Popen, communicate
import sys # exit
import filecmp # cmp


def print_mensaje(plain_name, is_ok):
    if (is_ok):
        print(" Test {0}: OK".format(plain_name))
    else:
        print(" Test {0}: FAILED".format(plain_name))


# Grafo como LISTA DE ADYACENCIA
def dfs(grafo, actual, visitados):
    visitados[actual] = True
    for hijo in grafo[actual]:
        if not visitados[hijo]:
            dfs(grafo, hijo, visitados)


# Pre: desde i=0, rutas[i] y rutas[i+1] son los dos extremos de una ruta
# Como m = n-1 (porque r_out = r_exp para esta etapa)
# Basta ver que "rutas" sea conexo. Lo veo con un dfs.
# Antes armo una lista de adyacencia para recorrer el grafo facilmente
def es_arbol(rutas, cant_nodos):
    m = int((len(rutas)/2))

    if (m != int(cant_nodos) - 1):
        print("\n\n m != n-1", end='')
        return False

    # No hay ningun vertice 0, comienza de 1
    lista_adyacencia = [[] for i in range(m+2)]

    # muevo i de 2 en 2
    for i in range(0, len(rutas), 2):
        r1 = int(rutas[i])
        r2 = int(rutas[i+1])
        lista_adyacencia[r1].append(r2)

    visitados = [False for i in range(m+2)]
    dfs(lista_adyacencia, 1, visitados)

    todos_visitados = True
    for i in range(1, len(visitados)):
        if not visitados:
            todos_visitados = False

    return todos_visitados

"""
En el problema 3 no hay una unica solucion posible para un valor minimo,
pueden haber diferentes combinaciones de rutas a contruir/destruir que den el mismo valor
asi como tambien hay que tener en cuenta que son rutas bidireccionales.

Considero que la solucion es correcta si:
- p_out = p_expected
- r_out = r_expected
- Las rutas de out forman un arbol
    : forman arbol si m = n-1  y si es conexo (dfs en O(n))
"""
def testear_problema_3(out_file, expected_file):
    # El output es una unica linea larga
    out_line = out_file.readline()
    exp_line = expected_file.readline()

    # Spliteo por espacios
    out_line = out_line.split()
    exp_line = exp_line.split()

    #print(out_line)

    if (out_line[0] != exp_line[0]):
        print("\n p_out: " + str(out_line[0]) + " !=  p_exp: " + str(exp_line[0]))
        print(out_line)
        return False

    if (out_line[1] != exp_line[1]):
        print("\n r_out: " + str(out_line[1]) + " !=  r_exp: " + str(exp_line[1]))
        print(out_line)
        return False

    if (not es_arbol(out_line[2:], int(exp_line[1]) + 1)):
        print("\n solucion NO es un arbol")
        print(out_line)
        return False

    return True


print("")

for nro in (1, 2, 3):

    # PREPARACION ---
    directory = "./tests/problema" + str(nro)
    executable = "./solucion" + str(nro)

    # Intro
    print("PROBLEMA " + str(nro))

    # Verificacion de la existencia del ejecutable
    if not os.path.isfile(executable):
        print(" Warning: no existe ejecutable en la ruta {}".format(executable))
        print(" Continuando...\n")
        continue

    # Limpieza de salidas viejas
    outputs = [f for f in os.listdir(directory) if f.endswith(".out")]
    for filename in outputs:
        os.remove(os.path.join(directory, filename))


    # GENERACION DE SALIDAS ---
    inputs = sorted([f for f in os.listdir(directory) if f.endswith(".in")])
    for filename in inputs:
        # Inicializacion de rutas
        base_path = os.path.join(directory, os.path.splitext(filename)[0])
        in_path = base_path + ".in"
        out_path = base_path + ".out"
        expected_path = base_path + ".expected"

        # Verificacion de que el '.expected' correspondiente existe
        if not os.path.isfile(expected_path):
            print("Warning: el archivo {} no tiene un '.expected' correspondiente".format(filename))
            continue

        # Ejecucion del programa
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


    # COMPARACION DE RESULTADOS ---
    outputs = sorted([f for f in os.listdir(directory) if f.endswith(".out")])
    for filename in outputs:
        # Inicializacion de rutas
        plain_name = os.path.splitext(filename)[0]
        base_path = os.path.join(directory, plain_name)
        out_path = base_path + ".out"
        expected_path = base_path + ".expected"

        # Comparacion
        test_ok = True

        out_file = open(out_path, 'r')
        expected_file = open(expected_path, 'r')

        # En el problema3, hay varias combinaciones de rutas posibles, no esta bien chequear igualdad de rutas
        # Ver comentarios al respecto en definicion de funcion
        if (nro == 3):
            test_ok = testear_problema_3(out_file, expected_file)
        else:
            out_line = out_file.readline().rstrip()
            exp_line = expected_file.readline().rstrip()

            while out_line != '' and exp_line != '':
                if out_line != exp_line:
                    test_ok = False
                out_line = out_file.readline().rstrip()
                exp_line = expected_file.readline().rstrip()

        # Cierro archivos en todos los casos
        out_file.close()
        expected_file.close()

        # Mensaje
        print_mensaje(plain_name, test_ok)

    print("")