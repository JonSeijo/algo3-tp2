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

Problema3::resolver() {

}