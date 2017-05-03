CPP=g++
FLAGS= -std=c++11

all: solucion3

tiempos: tiempos.cpp
	$(CPP) $(FLAGS) -o $@ $<

solucion3: Solucion3.cpp Problema3.cpp
	$(CPP) $(FLAGS) -o  $@ Problema3.cpp $<

%.o: %.cpp
	$(CPP) $(FLAGS) -c -o $@ $<

clean:
	rm -f *.o
	rm tiempos
	rm solucion3
