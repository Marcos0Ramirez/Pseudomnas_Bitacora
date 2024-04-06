# Informacion de proceso para la creacion de la matriz
### Fecha 04 de abril del 2024
---------------------------------------------------------------------------------------------------------------------

Por esta parte, se procedio a generar un script para leer las lineas de un archivo y que imprima las lineas con determinadas caracteristicas
Para este punto, se pidio a `ChatGPT` que realizace un script que funcione para hacer determinada accion. Para este punto genero este script

```
#!/bin/bash

# Nombre del archivo de entrada
archivo="datos.txt"

# Patrón para identificar el inicio de un nuevo cluster
patron="^>Cluster"

# Iterar sobre el archivo
while IFS= read -r linea; do
    # Comprobar si la línea coincide con el patrón
    if [[ $linea =~ $patron ]]; then
        # Imprimir la línea
        echo "$linea"
    fi
done < "$archivo"
```
Para el cual se procedio a tratar de entender como es que funciona el comando read -r
```
1113  cd /mnt/c/Users/52477/Desktop/Descargas_NCBI/
 1114  l
 1115  cd CRUDOS/
 1116  ls
 1117  cd ..
 1118  ls
 1119  cd Codigo/
 1120  ls
 1121  less cdscriptpseudomonas.sh
 1122  cut --helo
 1123  cut --help
 1124  cat --help
 1125  cut -f 1 ../CDHIT/TODOS/clusterprotcatALL2000.clstr
 1126  cut -f 2 ../CDHIT/TODOS/clusterprotcatALL2000.clstr | head -n 10
 1127  cut -f 3 ../CDHIT/TODOS/clusterprotcatALL2000.clstr | head -n 10
 1128  cut -f 4 ../CDHIT/TODOS/clusterprotcatALL2000.clstr | head -n 10
 1129  cut -f 5 ../CDHIT/TODOS/clusterprotcatALL2000.clstr | head -n 10
 1130  cut -f 2,3 ../CDHIT/TODOS/clusterprotcatALL2000.clstr | head -n 10
 1131  cut -f 1,2 ../CDHIT/TODOS/clusterprotcatALL2000.clstr | head -n 10
 1132  cut -f 1,2 ../CDHIT/TODOS/clusterprotcatALL2000.clstr | head -n 30
 1133  cut -f 2 ../CDHIT/TODOS/clusterprotcatALL2000.clstr | grep ">" | head -n 30
 1134  grep --help
 1135  cd /mnt/c/Users/52477/Desktop/Descargas_NCBI/Codigo/
 1136  cut -f 2 ../CDHIT/TODOS/clusterprotcatALL2000.clstr | grep ">" | head -n 30
 1137  grep --help
 1138  cut -f 2 ../CDHIT/TODOS/clusterprotcatALL2000.clstr | grep -oE ">[0-9]+" | head -n 30
 1139  cut -f 2 ../CDHIT/TODOS/clusterprotcatALL2000.clstr | grep -oE "[0-9]+aa" | head -n 30
 1140  cut -f 2,3 ../CDHIT/TODOS/clusterprotcatALL2000.clstr | grep -oE "[0-9]+aa" | head -n 30
 1141  cut -f 1,2 ../CDHIT/TODOS/clusterprotcatALL2000.clstr | grep -oE "[0-9]+aa" | head -n 30
 1142  less ../CDHIT/TODOS/clusterprotcatALL2000.clstr
 1143  grep -oE "[0-9]+aa" ../CDHIT/TODOS/clusterprotcatALL2000.clstr | head -n 30
 1144  read --help
 1145  grep -oE "[0-9]+aa" ../CDHIT/TODOS/clusterprotcatALL2000.clstr | read -r | head -n 30
 1146  grep -oE "[0-9]+aa" ../CDHIT/TODOS/clusterprotcatALL2000.clstr | head -n 30
 1147  read -r ../CDHIT/TODOS/clusterprotcatALL2000.clstr | head -n 30
 1148  read ../CDHIT/TODOS/clusterprotcatALL2000.clstr | head -n 30
 1149  ls
 1150  ls -lha ../CDHIT/TODOS/clusterprotcatALL2000.clstr
 1151  nano matrxcdhitscript.sh
 1152  ./matrxcdhitscript.sh
 1153  nano matrxcdhitscript.sh
 1154  ./matrxcdhitscript.sh
 1155  nano matrxcdhitscript.sh
 1156  ./matrxcdhitscript.sh
 1157  nano matrxcdhitscript.sh
 1158  ./matrxcdhitscript.sh
 1159  nano matrxcdhitscript.sh
 1160  ./matrxcdhitscript.sh
 1161  nano matrxcdhitscript.sh
 1162  ./matrxcdhitscript.sh
 1163  nano matrxcdhitscript.sh
 1164  read -r li ../CDHIT/TODOS/clusterprotcat.clstr
 1165  nano matrxcdhitscript.sh
 1166  read "hola amigos"
 1167  echo "hola"
 1168  read cad
 1169  read
 1170  if [[ $cad == "hola" ]]; then echo "saludillos"; else echo "chales carnal"; fi
 1171  read cad
 1172  if [[ $cad == "hola" ]]; then echo "saludillos"; else echo "chales carnal"; fi
 1173  read cad
 1174  if [[ $cad == "hola" ]]; then echo "saludillos: $cad" ; else echo "chales carnal: $cad"; fi
 1175  read cad
 1176  if [[ $cad == "hola" ]]; then echo "saludillos: $cad" ; else echo "chales carnal: $cad"; fi
 1177  if [[ $cad =~ "hola" ]]; then echo "saludillos: $cad" ; else echo "chales carnal: $cad"; fi
 1178  nano matrxcdhitscript.sh
 1179  read -r l
 1180  echo $l
 1181  read -r l; echo "hola"
 1182  read -r l; echo "hola"; fi
 1183  read -r l; echo "hola"; done
 1184  read -r l; do echo "hola"; done
 1185  for i in hola capsun; do read -r palabras; echo $i; done
 1186  for i in hola capsun; do read -r palabras | echo $i; done
 1187  for i in hola capsun; do echo $i | read -r palabras; done
 1188  ifdnsoi
 1189  ls
 1190  grep ">" ../CDHIT/TODOS/allgenes.clstr
 1191  grep ">" ../CDHIT/TODOS/allgenes.clstr  | cut -f 1
 1192  grep ">" ../CDHIT/TODOS/allgenes.clstr  | cut -f 1 |cat
 1193  grep ">" ../CDHIT/TODOS/allgenes.clstr  | cut -f 1 | cat
 1194  grep ">" ../CDHIT/TODOS/allgenes.clstr  | cut -f 1 | cat > fila.txt
 1195  ls
 1196  less fila.txt
 1197  for i in cat fila.txt; do echo "hola: $i"; done
 1198  for i in $(cat fila.txt); do echo "hola: $i"; done
 1199  history > historial4abril.txt
 1200  ls
 1201  more historial4abril.txt
 1202  history | tail -n 500 > historial4abril.txt
 1203  more historial4abril.txt
 1204  history | tail -n 100 > historial4abril.txt
 ```

Para este punto se sabe que `read -r variable` donde genera una variable y en ella almacena los datos que se pretenden guardar
Ahora se vera como hacer para que el script
1. Tome todas las lineas cluster y por aparte en otra variable genes que pertencen a determinado cluster
2. Detecte que cada que se inicia un nuevo `>Cluster [0-9]+` considere en un nuevo set de datos los genes que tiene por pertencia
3. De los genes que tiene en el cluster perteneciente, busque a que individuo pertence
4. Concatenar el nombre del organismo en cada fila y los datos de (id del gen y identidad) los coloque en interseccion con el cluster perteneciente
5. Localizar los demas genes de otros clusters y concatenar en donde ya esta el organismo o crear un nuevo fila con los nuevos datos.


### Fecha 05 de abril del 2024
Hasta el momento se sabe que el bucle while, cuando evalua los if's, los hace de manera simultanea, lo que indica que si colocamos un `echo "$n"` al inicio y al final (antes y despues de los if's):
```
#!/bin/bash

# Nombre del archivo de entrada
archivo="../CDHIT/TODOS/clusterprotcatALL2000.clstr"
rm ../CDHIT/MATRIXDATA/clusterfile.txt
rm ../CDHIT/MATRIXDATA/filegenes.txt
rm ../CDHIT/MATRIXDATA/mapruclusterfile.txt
# Patrón para identificar el inicio de un nuevo cluster
patron1=">Cluster"
patron2="[0-9]+aa"
n=1
# Iterar sobre el archivo
while IFS= read -r linea; do
        echo "$n"
    # Comprobar si la línea coincide con el patrón
        #echo "$linea"
    if [[ $linea =~ $patron1 ]]; then
        # Imprimir la línea
        echo "$linea" >> ../CDHIT/MATRIXDATA/mapruclusterfile.txt
         echo "$linea"
    fi
        if [[ $linea =~ $patron2 ]]; then
                # Imprimir la línea
                echo "$linea $n"
                n=$((n+1))
                echo "$linea" >> ../CDHIT/MATRIXDATA/mapruclusterfile.txt
        fi
        echo "$n"

done < "$archivo" | head -n 50
```

sucede esto
```
1
>Cluster 0
1
1
0       6388aa, >2785749539... * 1
2
2
>Cluster 1
2
2
0       171aa, >2505553514... at 60.82% 2
3
3
1       895aa, >2505554354... at 65.59% 3
4
4
2       1002aa, >2505554355... at 83.93% 4
5
5
3       5929aa, >2549668513... * 5
6
6
4       154aa, >2633064784... at 89.61% 6
7
7
5       313aa, >2633064986... at 86.90% 7
8
8
6       1239aa, >2633064989... at 85.55% 8
9
9
7       90aa, >2633064990... at 74.44% 9
10
10
8       3475aa, >2633065112... at 87.08% 10
11
11
9       5889aa, >2714614382... at 71.81% 11
12
12
>Cluster 2
12
12
0       5824aa, >2549670384... * 12
13
13
1       389aa, >2549670765... at 97.94% 13
14
14
2       105aa, >2549670769... at 98.10% 14
```

Si solo usamos el del inicio, resulta
```
1
>Cluster 0
1
0       6388aa, >2785749539... * 1
2
>Cluster 1
2
0       171aa, >2505553514... at 60.82% 2
3
1       895aa, >2505554354... at 65.59% 3
4
2       1002aa, >2505554355... at 83.93% 4
5
3       5929aa, >2549668513... * 5
6
4       154aa, >2633064784... at 89.61% 6
7
5       313aa, >2633064986... at 86.90% 7
8
6       1239aa, >2633064989... at 85.55% 8
9
7       90aa, >2633064990... at 74.44% 9
10
8       3475aa, >2633065112... at 87.08% 10
11
9       5889aa, >2714614382... at 71.81% 11
12
>Cluster 2
12
0       5824aa, >2549670384... * 12
13
1       389aa, >2549670765... at 97.94% 13
14
2       105aa, >2549670769... at 98.10% 14
15
3       514aa, >2549670774... at 76.46% 15
16
4       4780aa, >2633066528... at 67.68% 16
17
5       1072aa, >2633066529... at 88.62% 17
18
6       4093aa, >2714616755... at 68.90% 18
19
>Cluster 3
19
0       5809aa, >2923166973... * 19
20
>Cluster 4
20
0       5797aa, >2972001972... * 20
```
Y si solo ponemos al final, sucede esto
```
>Cluster 0
1
0       6388aa, >2785749539... * 1
2
>Cluster 1
2
0       171aa, >2505553514... at 60.82% 2
3
1       895aa, >2505554354... at 65.59% 3
4
2       1002aa, >2505554355... at 83.93% 4
5
3       5929aa, >2549668513... * 5
6
4       154aa, >2633064784... at 89.61% 6
7
5       313aa, >2633064986... at 86.90% 7
8
6       1239aa, >2633064989... at 85.55% 8
9
7       90aa, >2633064990... at 74.44% 9
10
8       3475aa, >2633065112... at 87.08% 10
11
9       5889aa, >2714614382... at 71.81% 11
12
>Cluster 2
12
0       5824aa, >2549670384... * 12
13
1       389aa, >2549670765... at 97.94% 13
14
2       105aa, >2549670769... at 98.10% 14
15
3       514aa, >2549670774... at 76.46% 15
16
4       4780aa, >2633066528... at 67.68% 16
17
5       1072aa, >2633066529... at 88.62% 17
18
6       4093aa, >2714616755... at 68.90% 18
19
>Cluster 3
19
0       5809aa, >2923166973... * 19
20
>Cluster 4
20
0       5797aa, >2972001972... * 20
21
```
Lo que indica que entra al bucle `while` imprime el numero, entra a evaluar el `if` y despues de evaluarlo, vuelve a imprimir el numero estando fuera, para reiniciar de nuevo el bucle, pero al parecer lo hace de manera indiscriminada del orden en el que esten colocados los comandos.

¿Como solucionar esto y que solo los numeros se coloquen de esta forma?
```
>Cluster 0
1
0       6388aa, >2785749539... * 1
>Cluster 1
0       171aa, >2505553514... at 60.82% 2
1       895aa, >2505554354... at 65.59% 3
2       1002aa, >2505554355... at 83.93% 4
3       5929aa, >2549668513... * 5
4       154aa, >2633064784... at 89.61% 6
5       313aa, >2633064986... at 86.90% 7
6       1239aa, >2633064989... at 85.55% 8
7       90aa, >2633064990... at 74.44% 9
8       3475aa, >2633065112... at 87.08% 10
9       5889aa, >2714614382... at 71.81% 11
2
...
```
Fecha 6 de abril del 2024
COn el comando 
```
grep -o -n -w "Cluster 1" ../CDHIT/TODOS/clusterprotcatALL2000.clstr | grep -Eo "^[0-9]+"
```
```
las opciones
-o | solo da los match
-n | da el numero de linea
-w | imprime la coincidencia exacta
para el segundo grep
-E | Usa las expresiones regulares
-o | solo da el match
^[0-9]+ | permite que solo sea la primera coincidencia
```
