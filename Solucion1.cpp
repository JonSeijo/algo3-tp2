#include "Problema1.h"

int main() {
    Problema1 problema;
    bool leyoInputCorrectamente = problema.leerInput();
    if (leyoInputCorrectamente) {
        problema.resolver(true);
    }
}
