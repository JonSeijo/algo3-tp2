#include "Problema1.h"

Problema1::Problema1() {
	return;
}

bool Problema1::leerInput() {
	// n: cant de ciudades
	std::cin >> n;

	if (n == -1) {
		return false;
	}

	std::cin >> m;

	if (m == -1) {
		return false;
	}

	std::cin >> origen >> destino >> k;

	matrizAdy.clear();
	esPremium.clear();

	// n+1 pues las ciudades van de 1 a n
	matrizAdy.resize(n+1, std::vector<int>(n+1, 0));
	esPremium.resize(n+1, std::vector<bool>(n+1, false));

	int mCount = 0;
	while (true) {
		int ciudad1, ciudad2, premium, distancia;
		std::cin >> ciudad1 >> ciudad2;

		if (ciudad1 == -1 && ciudad2 == -1){
			break;
		}

		mCount++;
		if (mCount > m){
			return false;
		}

		std::cin >> premium >> distancia;

		matrizAdy[ciudad1][ciudad2] = distancia;
		matrizAdy[ciudad2][ciudad1] = distancia;

		esPremium[ciudad1][ciudad2] = premium;
		esPremium[ciudad2][ciudad1] = premium;
	}

	return (mCount == m);
}

void Problema1::resolver(bool imprimirOutput) {
	int resultado = dijkstraMutante();

	if (imprimirOutput) {
		std::cout << resultado << std::endl;
	}

	//debug();
}


// Devuelvo un entero que representa la distancia del camino minimo entre origen y destino con a lo sumo k premiums (-1 si no existe)
int Problema1::dijkstraMutante() {
	// Implementacion de DIJKSTRA
	// ----------------------------------------------------

	std::vector<bool> visitado(n*(k+1)+1, false);	//Es k+1 porque k = # de clones y  +1 = el original
	std::vector<int> dist(n*(k+1)+1, INFINITO);		//Idem

	int s = origen;
	for (int w = 1; w <= n; w++) {
		if (matrizAdy[s][w] != 0){
			if (esPremium[s][w]) {
				if (k > 0){	//Puedo utilizar un camino premium en el primer paso si al menos k > 0!
					dist[w+n] = matrizAdy[s][w];
				}
			}else{
				dist[w] = matrizAdy[s][w];
			}
		}
	}

	dist[s] = 0;
	visitado[s] = true;

	/*
	std::cerr << "DIST: ";
	for (int i = 1; i <= n*(k+1); i++) {
		std::cerr << "|" <<  (dist[i] == INFINITO?-1:dist[i]);
	}
	std::cerr << std::endl;

	std::cerr << "VISIT: ";
	for (int i = 1; i <= n*(k+1); i++) {
		std::cerr << "|" <<  visitado[i];
	}
	std::cerr << std::endl;
	*/

	bool finalizado = false;

	// En cada iteracion visito un nodo (ya visite s)
	while (!finalizado) {

		// Tomo el nodo de menor distancia no visitado
		int v = -1;
		int minDist = INFINITO;
		for (int u = 1; u <= n*(k+1); u++) {
			if (!visitado[u] && dist[u] < minDist) {
				v = u;
				minDist = dist[u];
			}
		}


		if (minDist == INFINITO){
			finalizado = true;
			continue;
		}

		//std::cerr << "AGARRO: " << v << " CON DIST: " << minDist << std::endl;

		visitado[v] = true;
		int nivel = (v-1)/n;			//OJO: Es división entera!
		int vOriginal = v - n*nivel;	//El v de nivel 0 (para utilizar la matriz de adyacencia)

		//std::cerr << "NIVEL: " << nivel << " V ORIGINAL: " << vOriginal << std::endl;

		// Para cada vecino de v (pero en nivel 0 para utilizar la matriz de adyacencia)
		for (int w = 1; w <= n; w++) {
			if (matrizAdy[vOriginal][w] != 0){
				if (esPremium[vOriginal][w]) {
					if (nivel == k){	//Si supero el limite de premiums llego a un punto muerto en este paso
						continue;
					}

					int vecinoPremium = w + (nivel+1) * n;	//El vecino pero del siguiente nivel (respecto a v)
					if ( !visitado[vecinoPremium] && dist[vecinoPremium] > dist[v] + matrizAdy[vOriginal][w]){
						dist[vecinoPremium] = dist[v] + matrizAdy[vOriginal][w];
					}
				}else{
					int vecinoComun = w + nivel*n;	//El vecino pero del nivel actual (el nivel de v!)
					if ( !visitado[vecinoComun] && dist[vecinoComun] > dist[v] + matrizAdy[vOriginal][w]){
						dist[vecinoComun] = dist[v] + matrizAdy[vOriginal][w];
					}
				}
			}
		}
	}

	/*
	std::cerr << "RESULTADO DIJKSTRA: ";
	for (int i = 1; i <= n*(k+1); i++) {
		std::cerr << "|" <<  (dist[i]==INFINITO?-1:dist[i]);
	}
	std::cerr << "|" << std::endl;
	*/

	int distanciaMinima = INFINITO;
	for (int i = destino; i <= n*(k+1); i+= n) {
		if (dist[i] < distanciaMinima){
			distanciaMinima = dist[i];
		}
	}
	//std::cerr << "RESULTADO" << distanciaMinima << std::endl;
	return ((distanciaMinima == INFINITO)?-1:distanciaMinima);
}


void Problema1::debug() {
	std::cerr << "n: " << n << "\n\n";

	std::cerr << "adyacencia: \n";
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			std::cerr << matrizAdy[i][j] << " ";
		}
		std::cerr << "\n";
	}


	std::cerr << "\n\nesPremium: \n";
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			std::cerr << esPremium[i][j] << " ";
		}
		std::cerr << "\n";
	}
}
