#ifndef H_PROBLEMA_3
#define H_PROBLEMA_3

// El main esta en Solucion1.cpp

#include <iostream>
#include <vector>
#include <climits>

// Lo defino asi para no tener overflows inesperados cuando tenga que sumar valores
#define INFINITO (INT_MAX - 100000)

class Problema1 {
	public:
		Problema1();

		// Lee el input de una unica instancia.
		// Devuelve false si ya no hay input para leer.
		bool leerInput();

		// Resuelvo con los valores que tengo guardados (Pre: leerInput)
		void resolver(bool imprimirOutput);


	private:
		int n;
		int m;
		int k;
		int origen;
		int destino;
		// Grafo guardado como matriz de adyacencia pues voy a guardar las ~n^2 aristas posibles
		std::vector<std::vector<int> > matrizAdy;
		std::vector<std::vector<bool> > esPremium;

		int dijkstraCustom();

		void debug();
};

#endif
