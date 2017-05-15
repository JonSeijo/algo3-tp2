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
    auto rutas = recrearRutasDesdeArbol(arbol);

    int costoTotal = obtenerCostoTotal(rutas, costoInicialDestruirTodo);

    if (imprimirOutput) {
        escribirRta(rutas, costoTotal);
    }

    debug();
}

std::set<eje> Problema3::recrearRutasDesdeArbol(std::vector<int> &arbol) {
    // Solo quiero aristas validas, no repetirlas, ni tampoco las que tienen padre -1
    // Las siguientes secuencias son todas validas y representan al mismo arbol
    // [(1, 2), (2, 1)]
    // [(1, -1), (2, 1)]
    // [(2, -1), (1, 2)]
    // De esto, solo quiero quedarme con "(1,2)" o con "(2,1)"

    std::set<eje> rutas;

    for (int i = 1; i <= n; i++) {
        int j = arbol[i];
        if (j == -1) {
            continue;
        }
        auto eje_1 = std::make_pair(i, j);
        auto eje_2 = std::make_pair(j, i);
        // Si el eje no esta en las rutas, lo agrego
        if (std::find(rutas.begin(), rutas.end(), eje_1) == rutas.end()) {
            if (std::find(rutas.begin(), rutas.end(), eje_2) == rutas.end()) {
                rutas.insert(eje_1);
            }
        }
    }
    return rutas;
}

void Problema3::escribirRta(std::set<eje> rutas, int costoTotal) {
    std::cout << costoTotal << " ";
    std::cout << n-1 << " ";   // Pues es un arbol

    for (auto iter = rutas.begin(); iter != rutas.end(); iter++) {
        int i = (*iter).first;
        int j = (*iter).second;
        std::cout << i << " " << j << " ";
    }

    std::cout << "\n";
}

int Problema3::obtenerCostoTotal(std::set<eje> rutas, int costoInicialDestruirTodo) {
    // costoTotal contiene inicialmente el costo de destruir todas las que ya existen
    int costoTotal = costoInicialDestruirTodo;

    for (auto iter = rutas.begin(); iter != rutas.end(); iter++) {
        int i = (*iter).first;
        int j = (*iter).second;
        // Si era negativo se resta (implicito en la suma),
        // Si era positivo, se suma
        costoTotal += costo[i][j];
    }

    return costoTotal;
}


int Problema3::negativizarCostoConstruidas() {
    int costoInicialDestruirTodo = 0;

    // Si la ruta existe, hago que su costo sea negativa
    for (int i = 1; i <= n; i++) {
        for (int j = i+1; j <= n; j++) {
            if (existe[i][j]) {
                costoInicialDestruirTodo += costo[i][j];
                costo[i][j] *= -1;
                costo[j][i] *= -1;
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
    padre[s] = -1;
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
            if ((!visitado[w]) && (costo[v][w] < dist[w])) {
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