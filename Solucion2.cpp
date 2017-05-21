#include "Problema2.h"

int main() {
    Problema2 problema;
    bool leyoInputCorrectamente = problema.leerInput();
    if (leyoInputCorrectamente) {
        problema.resolver(true);
    }
}