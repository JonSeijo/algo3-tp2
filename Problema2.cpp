#include "Problema2.h"

void Problema2::resolver(bool imprimirOutput) {
    // Búsqueda del máximo
    int d = 0;
    int h = c+2; // h no inclusive, miro el rango [0..c+1]
    while (h - d > 1) {
        int m = (h - d)/2;
        if (hayAbuso(m)) {
            d = m;
        } else {
            h = m;
        }
    }

    // Output
    if (imprimirOutput) {
        std::cout << d << "\n";
    }

    debug();
}

bool Problema2::leerInput() {
    std::cin >> n; // Cantidad de ciudades
    std::cin >> m; // Cantidad de rutas

    grafo.clear();
    costo.clear();

    // n+1 pues las ciudades van de 1 a n
    // el 0 lo reservo para el nuevo nodo
    grafo.resize(n+1);
    costo.resize(n+1, std::vector<int>(n+1, 0));

    // Información de entrada
    int c = 0; // c es el máximo costo de peaje
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
    for (int i = 0; i < n; i++) { // iteraciones
        for (int nodo = 0; nodo <= n; nodo++) {
            for (auto it = grafo[nodo].begin(); it != grafo[nodo].end(); it++) {
                int vecino = *it;
                int peso = costo[nodo][vecino];
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
            int peso = costo[nodo][vecino];
            if (dist[vecino] > dist[nodo] + peso) {
                return true;
            }
        }
    }
    return false;
}


void Problema2::debug() {
    std::cout << "n: " << n << "   m: " << m << "   c: " << c << "\n\n";

    std::cout << "grafo: \n";
    for (int i = 0; i <= n; i++) {
        std::cout << i << ": ";
        for (auto it = grafo[i].begin(); it != grafo[i].end(); it++) {
            std::cout << *it << " ";
        }
        std::cout << "\n";
    }


    std::cout << "\n\ncosto: \n";
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= n; j++) {
            std::cout << costo[i][j] << " ";
        }
        std::cout << "\n";
    }
}