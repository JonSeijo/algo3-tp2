#include <iostream>
#include <vector>
#include <assert.h>

#include "Problema2.h"

/* Idea
    Sé que hay al menos algún ciclo. Si tomo el costo máximo y disminuyo los
    peajes en dicha cantidad más uno, entonces todos los pesos quedan
    negativos, por lo que el ciclo que existía queda negativo, y hay un
    abuso. Si disminuyo los peajes en 0, como parto de un grafo sin abuso, no
    tengo abuso. Intuitivamente, el valor máximo que busco está en el medio.
    Como los números del 0 al c están ordenados, puedo hacer búsqueda binaria.

    Hay un detalle, y es que el grafo no necesariamente es fuertemente
    conexo, con lo no podemos elegir cualquier nodo inicial. Para resolver
    este problema, creamos un nuevo nodo y lo contectamos con un eje de ida
    a todos los nodos del grafo. Es en este nuevo grafo es en donde buscamos
    un abuso.

Algoritmo
    - Parto del rango [1..c+1) y aplico búsqueda binaria. En cada rango no
    trivial, llamo a la función 'hayAbuso' con el elemento en el medio. Si
    da verdadero, busco en la parte superior del rango (con c inclusive),
    y si da falso, en la parte interior (con c no inclusive).
    - En 'hayAbuso', aplico Ford desde un nodo cualquiera, pero considerando
    el costo de cada eje como el original menos c. Hago n+1 iteraciones
    completas. Si hay un cambio de las distancias en la última iteración,
    tengo un ciclo negativo y hay abuso, de lo contrario no lo hay.
*/

void Problema2::resolver(bool imprimirOutput) {
    // Búsqueda del máximo en [0..c+2)
    int d = 0; // d inclusive
    int h = c+2; // h no inclusive
    while (h - d > 1) {
        int m = (h + d)/2;
        if (!hayAbuso(m)) {
            d = m;
        } else {
            h = m;
        }
    }

    // Output
    if (imprimirOutput) {
        std::cout << d << "\n";
    }
}

bool Problema2::leerInput() {
    std::cin >> n; // Cantidad de ciudades
    std::cin >> m; // Cantidad de rutas

    if (n == -1) {
        return false;
    }

    grafo.clear();
    costo.clear();

    // n+1 pues las ciudades van de 1 a n
    // el 0 lo reservo para el nuevo nodo
    grafo.resize(n+1);
    costo.resize(n+1, std::vector<int>(n+1, 0));

    // Información de entrada
    c = 0; // c es el máximo costo de peaje
    for (int i = 0; i < m; i++) {
        int c1, c2, p;
        std::cin >> c1 >> c2 >> p;

        grafo[c1].push_back(c2);
        costo[c1][c2] = p;

        c = p > c ? p : c;
    }

    // Aristas salientes del nodo agregado
    for (int i = 1; i <= n; i++) {
        grafo[0].push_back(i);
        costo[0][i] = 0;
    }

    return true;
}

bool Problema2::hayAbuso(int resta) {
    // Vamos a partir desde el 0, que por construcción sabemos que alcanza
    // todos los ciclos que existan, en cualquier grafo
    std::vector<int> dist(n+1);
    for (int i = 0; i <= n; i++) {
        dist[i] = INFINITO;
    }
    dist[0] = 0;

    // Cálculo de caminos mínimos
    for (int i = 1; i <= n+1; i++) { // iteraciones
        for (int nodo = 0; nodo <= n; nodo++) {
            for (auto it = grafo[nodo].begin(); it != grafo[nodo].end(); it++) {
                int vecino = *it;
                int peso = costo[nodo][vecino] - resta;
                if (dist[vecino] > dist[nodo] + peso) {
                    dist[vecino] = dist[nodo] + peso;
                }
            }
        }
    }

    // Checkeo de ciclo negativo
    for (int nodo = 0; nodo <= n; nodo++) {
        for (auto it = grafo[nodo].begin(); it != grafo[nodo].end(); it++) {
            int vecino = *it;
            int peso = costo[nodo][vecino] - resta;
            if (dist[vecino] > dist[nodo] + peso) {
                return true;
            }
        }
    }
    return false;
}


void Problema2::debug() {
    std::cerr << "n: " << n << "   m: " << m << "   c: " << c << "\n\n";

    std::cerr << "grafo: \n";
    for (int i = 0; i <= n; i++) {
        std::cerr << i << ": ";
        for (auto it = grafo[i].begin(); it != grafo[i].end(); it++) {
            std::cerr << *it << " ";
        }
        std::cerr << "\n";
    }


    std::cerr << "\n\ncosto: \n";
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= n; j++) {
            std::cerr << costo[i][j] << " ";
        }
        std::cerr << "\n";
    }
}