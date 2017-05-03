#include "Problema3.h"

int main() {
    Problema3 problema;
    while (problema.leerInput()) {
        problema.resolver(true);
    }
}