#ifndef H_PROBLEMA_3
#define H_PROBLEMA_3

// El main esta en Solucion3.cpp

#include <iostream>
#include <vector>
#include <climits>

// Lo defino asi para no tener overflows inesperados cuando tenga que sumar valores
#define INFINITO (INT_MAX - 100000)

class Problema3 {
    public:
        Problema3() : n(0) {};

        // Lee el input de una unica instancia.
        // Devuelve false si ya no hay input para leer.
        bool leerInput();

        // Resuelvo con los valores que tengo guardados (Pre: leerInput)
        void resolver(bool imprimirOutput);


    private:
        int n;
        // Grafo guardado como matriz de adyacencia pues voy a guardar las ~n^2 aristas posibles
        std::vector<std::vector<int> > existe;
        std::vector<std::vector<int> > costo;

        std::vector<int> primNaive();
        int negativizarCostoConstruidas();
        int obtenerCostoTotal(std::vector<int> arbol, int costoInicialDestruirTodo);
        void escribirRta(std::vector<int> arbol, int costoTotal);

        void debug();
};

#endif