#include "Problema1.h"

int main() {
	Problema1 problema;
	while (problema.leerInput()) {
		problema.resolver(true);
	}
}
