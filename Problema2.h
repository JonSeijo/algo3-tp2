#ifndef H_PROBLEMA_2
#define H_PROBLEMA_2

// El main esta en ej2.cpp

#include <iostream>
#include <vector>
#include <list>
#include <climits>

// Lo defino asi para no tener overflows inesperados cuando tenga que sumar valores
#define INFINITO (INT_MAX - 100000)

class Problema2 {
    public:
        // Lee el input de una unica instancia.
        // Devuelve false si ya no hay input para leer.
        bool leerInput();

        // Resuelvo con los valores que tengo guardados (Pre: leerInput)
        void resolver(bool imprimirOutput);


    private:
        int n, m, c;
        std::vector< std::list<int> > grafo; // Listas de adyacencia
        std::vector< std::vector<int> > costo; // Matriz con peso de los ejes

        bool hayAbuso(int resta);

        void debug();
};

#endif