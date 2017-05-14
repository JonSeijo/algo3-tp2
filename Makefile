CPP=g++
FLAGS= -std=c++11

all: solucion2 solucion3

tiempos: tiempos.cpp
	$(CPP) $(FLAGS) -o $@ $<

solucion2: Solucion2.cpp Problema2.cpp
	$(CPP) $(FLAGS) -o  $@ Problema2.cpp $<

solucion3: Solucion3.cpp Problema3.cpp
	$(CPP) $(FLAGS) -o  $@ Problema3.cpp $<

%.o: %.cpp
	$(CPP) $(FLAGS) -c -o $@ $<

clean:
	rm -f *.o
	rm tiempos
	rm solucion2
	rm solucion3
