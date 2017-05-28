CPP=g++
FLAGS= -std=c++11 -g -Wall

all: problema1 problema2 problema3

problema1: Solucion1.cpp Problema1.cpp Problema1.h
	$(CPP) $(FLAGS) -o  $@ Problema1.cpp $<

problema2: Solucion2.cpp Problema2.cpp Problema2.h
	$(CPP) $(FLAGS) -o  $@ Problema2.cpp $<

problema3: Solucion3.cpp Problema3.cpp Problema3.h
	$(CPP) $(FLAGS) -o  $@ Problema3.cpp $<

%.o: %.cpp
	$(CPP) $(FLAGS) -c -o $@ $<

clean:
	rm -f *.o
	rm -f problema1
	rm -f problema2
	rm -f problema3

