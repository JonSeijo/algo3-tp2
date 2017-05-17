# algo3-tp2
Tp2 de algo3

## GITIGNORE
Modifiquenlo a gusto para no subir mugre, sobre todo si usan un IDE.
Está el de TeX que viene por defecto.


## CODESTYLE
Seamos consistentes:
- Indentación de 4 espacios
- En c++, variables y funciones con camelCase
- En python, variables y funciones con snake_case


## C++
Se incluye un MakeFile (precario) para una rapida compilación. Ejecutar ```make``` en consola y magia.

La idea es que cada problema esté en una clase aparte, y sean los SolucionX.cpp / TiempoX.cpp los que tengan el main, y llamen a los problemas.
- SolucionX.cpp deberia poder tomar un .txt por entrada estandar y resolver todos las instancias que se le pasen, imprimiendo solo el output correspondiente.
- TiempoX.cpp deberia poder tomar instancias por entrada estandar e imprimir solo el tiempo que le toma resolver cada instancia. Mas adelante tenemos que ver bien cuales son los datos que vamos a querer obtener (ademas de los tiempos, ejemplo el n, o la cantidad de aristas, nose)

Idealmente seguir el formato de Solucion3.cpp y Problema3 pero esto es perfectamente discutible en caso que haya formas mejores.


## INFORME

En el directorio principal, para compilar y ver el pdf resultante ejecutar:
```
python makepdf.py
```
Puede pasarsele un parametro opcional P, numero de pagina en el cual queres que se abra el pdf (Util posta!).
Por ejemplo:

```
python makepdf.py --p=3
```

## EXPERIMENTOS + GRAFICOS

(necesario python3)

El experimentador es el encargado de ejecutar programa e ir guardando los tiempos .csv
El graficador es quien carga los .csv y grafica los promedios

Dividi los experimentadores y graficadores por problemas, porque no se que tan diferentes van a ser.
Si van a ser masomenos iguales, puedo tratar de unirlos

(Usar flag -h en experimentador para ver una lista de opciones)

```
python3 experimentador3.py -todos
```
```
python3 graficador3.py
```


## TODO:
Lista de cosas pendientes para hacer.

[X] Crear repo

[X] Completar libretas y mails

[x] Crear tiempos3.cpp para el problema 3

[x] Pensar la mejor forma de organizar los .csv para el output del problema3, pensar que queremos medir

[x] Crear un script de python que ejecute tiempos para una instancia dada

[x] Hacer introduccion/explicacion del problema3

[x] Agregar pseudocodigo de problema3

[X] En el problema 3 revisar que el primer eje de 'arbol' luego de hacer Prim es probable que sea inválido

[ ] Buscar una carátula mas completa (Faltaria cuadro de correcciones, y ya que estamos fancy, el logo del DC)

[ ] Reemplazar std::vector<std::vector<int> > por un typedef Matriz o algo similar

[ ] Testear problema3.cpp con casos de prueba

[ ] Realizar analisis de complejidad de problema3

[ ] Relizar justificacion/demostracion de correctitud para el problema3
