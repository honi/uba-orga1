#!/bin/sh

# logisim $1 -tty table > resultados.txt
java -jar ../../logisim.jar $1 -tty table > resultados.txt
echo "Resultados guardados en resultados.txt"
echo "Se encontro que `diff -qs expected.txt resultados.txt`."
   ( echo "A   \tB   \tOP\tN\tZ\tV\tC\tRES" > diff.txt & diff expected.txt resultados.txt >> diff.txt;
   if [ $? -ne 0 ]
   then
	   echo "Revisa el archivo diff.txt para ver las diferencias con el resultado esperado."
   else
      echo "El Taller parece funcionar!"
   fi
   )
