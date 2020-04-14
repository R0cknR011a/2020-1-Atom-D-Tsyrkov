lib_matrix.so: matrix.o
	gcc -fPIC -shared -o lib_matrix.so matrix.o
matrix.o: matrix.c
	gcc -c -fPIC matrix.c
clean:
	rm *.o lib_matrix.so
