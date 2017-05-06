#include "Problema3.h"

bool Problema3::leerInput() {
    // n: cant de ciudades
    std::cin >> n;

    if (n == -1) {
        return false;
    }

    existe.clear();
    costo.clear();

    // n+1 pues las ciudades van de 1 a n
    existe.resize(n+1, std::vector<int>(n+1, 0));

    // El costo es infinito cuando no hay arista
    costo.resize(n+1, std::vector<int>(n+1, INFINITO));

    for (int i = 0; i < n*(n-1)/2; i++) {
        int c1, c2, e, p;
        std::cin >> c1 >> c2 >> e >> p;

        existe[c1][c2] = e;
        existe[c2][c1] = e;

        costo[c1][c2] = p;
        costo[c2][c1] = p;
    }

    return true;
}

void Problema3::resolver(bool imprimirOutput) {
    // Debo hacer std::cout con la respuesta en el formato correcto
    // Terminar con un \n !!

    // Implementacion usando prim


    // PRE: Armar el grafo completo con costos negativos donde ya existen,
    // y costo de construccion donde no

    std::vector<bool> visitado(n+1, false);
    std::vector<int> dist(n+1, INFINITO);
    std::vector<int> padre(n+1, -1);

    int s = 1; // Tomo cualquiera, en particular el 1

    for (int w = 1; w <= n; w++) {
        if (s != w) {  // Los vecinos de s son todos excepto s
            dist[w] = costo[s][w];
            padre[w] = s;
        }
    }

    dist[s] = 0;
    visitado[s] = true;

    // En cada iteracion visito un nodo (ya visite s)
    for (int repes = 1; repes < n; repes++) {

        // Tomo el nodo de menor distancia no visitado
        int v = -1;
        int minDist = INFINITO;
        for (int u = 1; u <= n; u++) {
            if (!visitado[u] && dist[u] < minDist) {
                v = u;
                minDist = dist[u];
            }
        }

        // Para cada vecino de v (todos excepto v porque es completo)
        for (int w = 1; w <= n; w++) {
            if ((v != w) && (costo[v][w] < dist[w])) {
                dist[w] = costo[v][w];
                padre[w] = v;
            }
        }
    }

    // De Padre tengo que reconstruir el arbol

    debug();
}

void Problema3::debug() {
    std::cout << "n: " << n << "\n\n";

    std::cout << "existe: \n";
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            std::cout << existe[i][j] << " ";
        }
        std::cout << "\n";
    }


    std::cout << "\n\ncosto: \n";
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            std::cout << costo[i][j] << " ";
        }
        std::cout << "\n";
    }
}