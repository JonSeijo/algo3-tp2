#ifndef H_PROBLEMA_2
#define H_PROBLEMA_2

// El main no está en el problema2,
// sino que habrá un main en solucion.cpp (que llama al problema2)
// y otro main en tiempos.cpp (que llama al problema2)

/* Idea
    Sé que hay al menos algún ciclo. Si tomo el costo máximo y disminuyo los
    peajes en dicha cantidad más uno, entonces todos los pesos quedan
    negativos, por lo que el ciclo que existía queda negativo, y hay un
    abuso. Si disminuyo los peajes en 0, como parto de un grafo sin abuso, no
    tengo abuso. Intuitivamente, el valor máximo que busco está en el medio.
    Como los números del 0 al c están ordenados, puedo hacer búsqueda binaria.

    Hay un detalle, y es que el grafo no necesariamente es fuertemente
    conexo, con lo no podemos elegir cualquier nodo inicial. Para resolver
    este problema, creamos un nuevo nodo y lo contectamos con un eje de ida
    a todos los nodos del grafo. Es en este nuevo grafo es en donde buscamos
    un abuso. 

Algoritmo
    - Parto del rango [1..c+1) y aplico búsqueda binaria. En cada rango no
    trivial, llamo a la función 'hayAbuso' con el elemento en el medio. Si
    da verdadero, busco en la parte superior del rango (con c inclusive), 
    y si da falso, en la parte interior (con c no inclusive).
    - En 'hayAbuso', aplico Ford desde un nodo cualquiera, pero considerando
    el costo de cada eje como el original menos c. Hago n+1 iteraciones
    completas. Si hay un cambio de las distancias en la última iteración,
    tengo un ciclo negativo y hay abuso, de lo contrario no lo hay.
*/

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