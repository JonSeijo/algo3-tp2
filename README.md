# algo3-tp2
Tp2 de algo3

## GITIGNORE
Modifiquenlo a gusto para no subir mugre, sobre todo si usan un IDE.
Esta el de TeX que viene por defecto.


## CODESTYLE
Seamos consistentes:
- Indentacion de 4 espacios
- En c++, variables y funciones con camelCase
- En python, variables y funciones con_snake_case


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


## TODO:
Lista de cosas pendientes para hacer.

[X] Crear repo

[X] Completar libretas y mails

[ ] Buscar una caratula mas completa (Faltaria cuadro de correcciones, y ya que estamos fancy, el logo del DC)

[ ] Reemplazar std::vector<std::vector<int> > por un typedef Matriz o algo similar

[ ] Testear problema3.cpp con casos de prueba

[ ] Crear tiempos3.cpp para el problema 3

[ ] Pensar la mejor forma de organizar los .csv para el output del problema3, pensar que queremos medir

[ ] Crear un script de python que ejecute tiempos para una instancia dada

[ ] Hacer introduccion/explicacion del problema3

[ ] DESPUES DE TESTEAR Y ESTAR CONFORMES! -> agregar pseudocodigo de problema3

[ ] Realizar analisis de complejidad de problema3

[ ] Relizar justificacion/demostracion de correctitud para el problema3
