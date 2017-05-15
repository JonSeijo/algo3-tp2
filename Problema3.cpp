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
    costo.resize(n+1, std::vector<int>(n+1, 0));

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

    // Auxiliar para almacenar el arbol rta
    std::vector<int> arbol;

    // Convierto los costos de las ya existentes a negativos, para priorizar su eleccion
    // Guardo cuanto costaria destruir las que ya existen
    int costoInicialDestruirTodo = negativizarCostoConstruidas();

    // De Padre tengo que reconstruir el arbol y los armar los costos
    arbol = primNaive();

    int costoTotal = obtenerCostoTotal(arbol, costoInicialDestruirTodo);

    if (imprimirOutput) {
        escribirRta(arbol, costoTotal);
    }

    debug();
}

void Problema3::escribirRta(std::vector<int> arbol, int costoTotal) {
    std::cout << costoTotal << " ";

    std::cout << n-1 << " ";   // Pues es un arbol

    for (int i = 1; i <= n; i++) {
        int j = arbol[i];
        // Son rutas bidireccionales, por lo que esto muestra todas las rutas una unica vez
        if (i < j){
            std::cout << i << " " << j << " ";
        }
    }

    std::cout << "\n";
}

int Problema3::obtenerCostoTotal(std::vector<int> arbol, int costoInicialDestruirTodo) {
    // costoTotal contiene inicialmente el costo de destruir todas las que ya existen
    int costoTotal = costoInicialDestruirTodo;
    for (int i = 1; i <= n; i++) {
        int j = arbol[i];
        // Arista (i, j) está en el AGM

        // Si ya existia, como el costo de las que existen estaba sumado entonces lo restao
        // Si no existia, no lo estaba contando asi que lo sumo (costo de construir es positivo)
        costoTotal += costo[i][j];
    }

    return costoTotal;
}


int Problema3::negativizarCostoConstruidas() {
    int costoInicialDestruirTodo = 0;

    // Si la ruta existe, hago que su costo sea negativa
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (existe[i][j]) {
                costoInicialDestruirTodo += costo[i][j];
                costo[i][j] *= -1;
            }
        }
    }

    return costoInicialDestruirTodo;
}

// Devuelvo un vector que representa el AGM de la instancia actual
std::vector<int> Problema3::primNaive() {
    // Implementacion usando Prim
    // ----------------------------------------------------

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

        visitado[v] = true;

        // Para cada vecino de v (todos excepto v porque es completo)
        for (int w = 1; w <= n; w++) {
            if (dist[w] == -1) {
                continue;
            }
            if ((v != w) && (costo[v][w] < dist[w])) {
                dist[w] = costo[v][w];
                padre[w] = v;
            }
        }
    }

    return padre;
}


void Problema3::debug() {
    std::cerr << "n: " << n << "\n\n";

    std::cerr << "existe: \n";
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            std::cerr << existe[i][j] << " ";
        }
        std::cerr << "\n";
    }


    std::cerr << "\n\ncosto: \n";
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            std::cerr << costo[i][j] << " ";
        }
        std::cerr << "\n";
    }
}