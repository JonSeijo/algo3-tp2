CPP=g++
FLAGS= -std=c++11 -g -Wall

all: solucion1 solucion2 solucion3 tiempo1 tiempo2 tiempo3

solucion1: Solucion1.cpp Problema1.cpp Problema1.h
	$(CPP) $(FLAGS) -o  $@ Problema1.cpp $<

solucion2: Solucion2.cpp Problema2.cpp Problema2.h
	$(CPP) $(FLAGS) -o  $@ Problema2.cpp $<

solucion3: Solucion3.cpp Problema3.cpp Problema3.h
	$(CPP) $(FLAGS) -o  $@ Problema3.cpp $<

tiempo1: Tiempo1.cpp Problema1.cpp Problema1.h
	$(CPP) $(FLAGS) -o  $@ Problema1.cpp $<

tiempo2: Tiempo2.cpp Problema2.cpp Problema2.h
	$(CPP) $(FLAGS) -o  $@ Problema2.cpp $<

tiempo3: Tiempo3.cpp Problema3.cpp Problema3.h
	$(CPP) $(FLAGS) -o  $@ Problema3.cpp $<

%.o: %.cpp
	$(CPP) $(FLAGS) -c -o $@ $<

clean:
	rm -f *.o
	rm -f tiempos
	rm -f solucion1
	rm -f solucion2
	rm -f solucion3
