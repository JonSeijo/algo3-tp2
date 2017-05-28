#include "Problema3.h"

int main() {
    Problema3 problema;
    bool leyoInputCorrectamente = problema.leerInput();
    if (leyoInputCorrectamente) {
        problema.resolver(true);
    }
}