#include "Problema2.h"

int main() {
    Problema2 problema;
    while (problema.leerInput()) {
        problema.resolver(true);
    }
}