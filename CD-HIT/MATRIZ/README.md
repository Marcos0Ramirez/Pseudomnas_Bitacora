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
Pasos en reversa para saber que es lo que pasa
```
grep -o -n -w "Cluster 1" ../CDHIT/TODOS/clusterprotcatALL2000.clstr | grep -Eo "^[0-9]+"

Resultado:
3
```

```
grep -o -n -w "Cluster 1" ../CDHIT/TODOS/clusterprotcatALL2000.clstr | grep -Eo "[0-9]+"

Resultado:
3
1
```

```
grep -o -n -w "Cluster 1" ../CDHIT/TODOS/clusterprotcatALL2000.clstr
Resultado:
3:Cluster 1 # Donde solo marca Cluster 1
```

```
grep -o -n "Cluster 1" ../CDHIT/TODOS/clusterprotcatALL2000.clstr
Resultado:
3:Cluster 1
41:Cluster 1
47:Cluster 1
49:Cluster 1
61:Cluster 1
66:Cluster 1
69:Cluster 1
71:Cluster 1
73:Cluster 1
75:Cluster 1
```

```
grep -n "Cluster 1" ../CDHIT/TODOS/clusterprotcatALL2000.clstr
3:>Cluster 1
41:>Cluster 10
47:>Cluster 11
49:>Cluster 12
61:>Cluster 13
66:>Cluster 14
69:>Cluster 15
71:>Cluster 16
73:>Cluster 17
75:>Cluster 18
```

```
grep "Cluster 1" ../CDHIT/TODOS/clusterprotcatALL2000.clstr
>Cluster 1
>Cluster 10
>Cluster 11
>Cluster 12
>Cluster 13
>Cluster 14
>Cluster 15
>Cluster 16
>Cluster 17
>Cluster 18
```
Ahora con el comando mas desarrollado, podemos extraer la informaicon comodamente, por marcos de referencia:
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
ni=0
nfinal=$(grep -E "$patron1" $archivo | wc -l)
nfinal=$((nfinal-1))
echo $nfinal
# Iterar sobre el archivo

while [[ $ni -le $nfinal ]]; do
        limitei=$(grep -o -n -w "Cluster $ni" ../CDHIT/TODOS/clusterprotcatALL2000.clstr | grep -Eo "^[0-9]+")
        nf=$((ni+1))
        limitef=$(grep -o -n -w "Cluster $nf" ../CDHIT/TODOS/clusterprotcatALL2000.clstr | grep -Eo "^[0-9]+")
        echo "$(sed -n "$limitei,${limitef}p" ../CDHIT/TODOS/clusterprotcatALL2000.clstr)"
        echo "$limitei,$limitef"
        ni=$((ni+1))
done
```
Resultado
```
>Cluster 12
0       4336aa, >2505553445... at 72.97%
1       4342aa, >2556075010... *
2       4317aa, >2518035654... at 69.63%
3       4336aa, >2549669578... at 72.90%
4       4336aa, >2633068181... at 73.02%
5       2897aa, >2714614118... at 74.87%
6       1447aa, >2714617557... at 69.32%
7       4328aa, >2785750798... at 71.93%
8       4298aa, >2923169007... at 66.71%
9       4298aa, >2972005913... at 66.59%
10      4332aa, >8011076810... at 75.28%
>Cluster 13
49,61
>Cluster 13
0       627aa, >2633065110... at 64.43%
1       2092aa, >2714614383... at 61.52%
2       4301aa, >2923167232... at 88.51%
3       4303aa, >2972005190... *
>Cluster 14
61,66
>Cluster 14
0       4227aa, >2923168233... *
1       3796aa, >2972004192... at 75.37%
>Cluster 15
```

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
ni=0
nfinal=$(grep -E "$patron1" $archivo | wc -l)
nfinal=$((nfinal-1))
echo $nfinal
# Iterar sobre el archivo

while [[ $ni -le $nfinal ]]; do
        limitei=$(grep -o -n -w "Cluster $ni" ../CDHIT/TODOS/clusterprotcatALL2000.clstr | grep -Eo "^[0-9]+")
        nf=$((ni+1))
        limitef=$(grep -o -n -w "Cluster $nf" ../CDHIT/TODOS/clusterprotcatALL2000.clstr | grep -Eo "^[0-9]+")
        limitef=$((limitef-1))
        echo "$(sed -n "$limitei,${limitef}p" ../CDHIT/TODOS/clusterprotcatALL2000.clstr)"
        echo "$limitei,$limitef"
        ni=$((ni+1))
done
```
Resultado
```
>Cluster 0
0       6388aa, >2785749539... *
1,2
>Cluster 1
0       171aa, >2505553514... at 60.82%
1       895aa, >2505554354... at 65.59%
2       1002aa, >2505554355... at 83.93%
3       5929aa, >2549668513... *
4       154aa, >2633064784... at 89.61%
5       313aa, >2633064986... at 86.90%
6       1239aa, >2633064989... at 85.55%
7       90aa, >2633064990... at 74.44%
8       3475aa, >2633065112... at 87.08%
9       5889aa, >2714614382... at 71.81%
3,13
>Cluster 2
0       5824aa, >2549670384... *
1       389aa, >2549670765... at 97.94%
2       105aa, >2549670769... at 98.10%
3       514aa, >2549670774... at 76.46%
4       4780aa, >2633066528... at 67.68%
5       1072aa, >2633066529... at 88.62%
6       4093aa, >2714616755... at 68.90%
14,21
>Cluster 3
0       5809aa, >2923166973... *
22,23
```
Ahora se va a buscar concatenar cada salida en un archivo y se va a separar cada resuldado de cluster por columna separado por tabs
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
ni=0
nfinal=$(grep -E "$patron1" $archivo | wc -l)
nfinal=$((nfinal-1))
echo $nfinal
# Iterar sobre el archivo

while [[ $ni -le $nfinal ]]; do
        limitei=$(grep -o -n -w "Cluster $ni" ../CDHIT/TODOS/clusterprotcatALL2000.clstr | grep -Eo "^[0-9]+")
        nf=$((ni+1))
        limitef=$(grep -o -n -w "Cluster $nf" ../CDHIT/TODOS/clusterprotcatALL2000.clstr | grep -Eo "^[0-9]+")
        limitef=$((limitef-1))
        clusterset=$(sed -n "$limitei,${limitef}p" ../CDHIT/TODOS/clusterprotcatALL2000.clstr)

        echo "$limitei,$limitef"
        ni=$((ni+1))
done
```

------------------------------------------------------------------------------------------------------------------------
Codigo final hasta el dia de hoy, continuamos con la modificacion de el para adaptar los genes y los nombres de las especies a la matriz
```
#!/bin/bash

# Nombre del archivo de entrada
archivo="../CDHIT/TODOS/clusterprotcatALL2000.clstr"
rm ../CDHIT/MATRIXDATA/clusterfile.txt
rm ../CDHIT/MATRIXDATA/filegenes.txt
rm ../CDHIT/MATRIXDATA/mapruclusterfile.txt
rm ../CDHIT/MATRIXDATA/salidita.txt
# Patrón para identificar el inicio de un nuevo cluster
patron1=">Cluster"
patron2="[0-9]+aa"
ni=0
nfinal=$(grep -E "$patron1" $archivo | wc -l)
nfinal=$((nfinal-1))
echo $nfinal
# Iterar sobre el archivo

while [[ $ni -le $nfinal ]]; do
        limitei=$(grep -o -n -w "Cluster $ni" ../CDHIT/TODOS/clusterprotcatALL2000.clstr | grep -Eo "^[0-9]+")
        nf=$((ni+1))
        limitef=$(grep -o -n -w "Cluster $nf" ../CDHIT/TODOS/clusterprotcatALL2000.clstr | grep -Eo "^[0-9]+")
        limitei=$((limitei+1))
        limitef=$((limitef-1))
        clusterset=$(sed -n "$limitei,${limitef}p" ../CDHIT/TODOS/clusterprotcatALL2000.clstr)
        echo "Cluster $ni" >> ../CDHIT/MATRIXDATA/salidita.txt
        echo "Cluster $ni"
        echo "$clusterset" | while M= read -r  lineas; do
                # echo "$lineas"
                busqueda=$(echo "$lineas" | grep -E -o -w ">[0-9]+")
                #echo "$lineas  $busqueda"
                genes=$(grep "$busqueda" ../CDHIT/TODOS/fromscriptall.genes.faa | head -n 1)
                echo "$lineas   Cluster $ni     $genes"
                echo "Cluster $ni" >> ../CDHIT/MATRIXDATA/salidita.txt
                echo "$lineas   Cluster $ni     $genes" >>  ../CDHIT/MATRIXDATA/salidita.txt
        done
        echo "$limitei,$limitef"
        ni=$((ni+1))
done
```
Salida
```
rm: cannot remove '../CDHIT/MATRIXDATA/clusterfile.txt': No such file or directory
rm: cannot remove '../CDHIT/MATRIXDATA/filegenes.txt': No such file or directory
rm: cannot remove '../CDHIT/MATRIXDATA/mapruclusterfile.txt': No such file or directory
19000
Cluster 0
0       6388aa, >2785749539... *        Cluster 0       >2785749539 Ga0304784_1247 RIP homotypic interaction motif (RHIM)-containing protein [Pseudomonas psychrophila BIGb0477]
2,2
Cluster 1
0       171aa, >2505553514... at 60.82% Cluster 1       >2505553514 PphNPS3121_0030.00000010 Non-ribosomal peptide synthetase modules and related proteins [Pseudomonas syringae PphNPS3121]
1       895aa, >2505554354... at 65.59% Cluster 1       >2505554354 PphNPS3121_0043.00004260 Non-ribosomal peptide synthetase modules and related proteins [Pseudomonas syringae PphNPS3121]
2       1002aa, >2505554355... at 83.93%        Cluster 1       >2505554355 PphNPS3121_0043.00004270 amino acid adenylation domain-containing protein [Pseudomonas syringae PphNPS3121]
3       5929aa, >2549668513... *        Cluster 1       >2549668513 NZ4DRAFT_03256 arthrofactin-type cyclic lipopeptide synthetase C [Pseudomonas syringae ICMP 18804]
4       154aa, >2633064784... at 89.61% Cluster 1       >2633064784 Ga0077257_10191 AMP-binding enzyme [Pseudomonas amygdali pv. tabaci yuexi-1]
5       313aa, >2633064986... at 86.90% Cluster 1       >2633064986 Ga0077257_108013 Thioesterase domain-containing protein [Pseudomonas amygdali pv. tabaci yuexi-1]
6       1239aa, >2633064989... at 85.55%        Cluster 1       >2633064989 Ga0077257_108016 amino acid adenylation domain-containing protein [Pseudomonas amygdali pv. tabaci yuexi-1]
7       90aa, >2633064990... at 74.44%  Cluster 1       >2633064990 Ga0077257_108017 arthrofactin-type cyclic lipopeptide synthetase C [Pseudomonas amygdali pv. tabaci yuexi-1]
8       3475aa, >2633065112... at 87.08%        Cluster 1       >2633065112 Ga0077257_108411 arthrofactin-type cyclic lipopeptide synthetase C [Pseudomonas amygdali pv. tabaci yuexi-1]
9       5889aa, >2714614382... at 71.81%        Cluster 1       >2714614382 Ga0124767_1046121 arthrofactin-type cyclic lipopeptide synthetase C [Pseudomonas syringae pv. primulae ICMP3956]
4,13
Cluster 2
0       5824aa, >2549670384... *        Cluster 2       >2549670384 NZ4DRAFT_05129 filamentous hemagglutinin [Pseudomonas syringae ICMP 18804]
1       389aa, >2549670765... at 97.94% Cluster 2       >2549670765 NZ4DRAFT_05511 Large exoproteins involved in heme utilization or adhesion [Pseudomonas syringae ICMP 18804]
2       105aa, >2549670769... at 98.10% Cluster 2       >2549670769 NZ4DRAFT_05515 filamentous hemagglutinin [Pseudomonas syringae ICMP 18804]
3       514aa, >2549670774... at 76.46% Cluster 2       >2549670774 NZ4DRAFT_05520 Haemagluttinin repeat-containing protein [Pseudomonas syringae ICMP 18804]
4       4780aa, >2633066528... at 67.68%        Cluster 2       >2633066528 Ga0077257_1099228 filamentous hemagglutinin [Pseudomonas amygdali pv. tabaci yuexi-1]
5       1072aa, >2633066529... at 88.62%        Cluster 2       >2633066529 Ga0077257_1099229 filamentous hemagglutinin family N-terminal domain-containing protein [Pseudomonas amygdali pv. tabaci yuexi-1]
6       4093aa, >2714616755... at 68.90%        Cluster 2       >2714616755 Ga0124767_11768 filamentous hemagglutinin [Pseudomonas syringae pv. primulae ICMP3956]
15,21
```
------------------------------------------------------------------------------------------------------------------------
Al final de cuando termina el archivo es asi
```
>Cluster 18996
0       25aa, >2714618651... *
>Cluster 18997
0       24aa, >2505557456... *
>Cluster 18998
0       22aa, >2505554779... *
>Cluster 18999
0       21aa, >2505555143... *
>Cluster 19000
0       21aa, >2505557421... *
```
Al terminar el comando, marca un error en sed con una coma ',' inesperada (toca ver dentro del scrript para corregir)
Ademas tardo cerca de 1 h con 40 min.
```
Cluster 18996
0       25aa, >2714618651... *  Cluster 18996   >2714618651 Ga0124767_12761 hypothetical protein [Pseudomonas syringae pv. primulae ICMP3956]
Cluster 18997
0       24aa, >2505557456... *  Cluster 18997   >2505557456 PphNPS3121_0084.00000080 hypothetical protein [Pseudomonas syringae PphNPS3121]
Cluster 18998
0       22aa, >2505554779... *  Cluster 18998   >2505554779 PphNPS3121_0047.00001090 hypothetical protein [Pseudomonas syringae PphNPS3121]
Cluster 18999
0       21aa, >2505555143... *  Cluster 18999   >2505555143 PphNPS3121_0051.00000010 hypothetical protein [Pseudomonas syringae PphNPS3121]
Cluster 19000
        Cluster 19000   >2505552086 PphNPS3121_0001.00000010 1-acyl-sn-glycerol-3-phosphate acyltransferase [Pseudomonas syringae PphNPS3121]
```

### Fecha 7 de abril del 2024
Hoy, pondremos en orden
1. Numero del cluster como fila 1
2. Secuencias representativas, como columna, representante del cluster como fila 2
3. Aquellos individuos que compaginen con el representante como nombre de la fila
4. El cruce entre la secuencia representante e individuo, el id de la proteina asi como el porcentaje de identidad
    a. Y si es el caso de que haya secuencias del mismo organismo en un mismo cluster se concatenan como (id:identity% id2:identity2)
Trabajamos con el archivo de salida
```
head -n 10 salidita.txt | cut -f 4
        Resultado
Cluster 1
>2505553514 PphNPS3121_0030.00000010 Non-ribosomal peptide synthetase modules and related proteins [Pseudomonas syringae PphNPS3121]
>2505554354 PphNPS3121_0043.00004260 Non-ribosomal peptide synthetase modules and related proteins [Pseudomonas syringae PphNPS3121]
>2505554355 PphNPS3121_0043.00004270 amino acid adenylation domain-containing protein [Pseudomonas syringae PphNPS3121]
>2549668513 NZ4DRAFT_03256 arthrofactin-type cyclic lipopeptide synthetase C [Pseudomonas syringae ICMP 18804]
>2633064784 Ga0077257_10191 AMP-binding enzyme [Pseudomonas amygdali pv. tabaci yuexi-1]
>2633064986 Ga0077257_108013 Thioesterase domain-containing protein [Pseudomonas amygdali pv. tabaci yuexi-1]
>2633064989 Ga0077257_108016 amino acid adenylation domain-containing protein [Pseudomonas amygdali pv. tabaci yuexi-1]
---------------------------------------------------------------------------------------------------------------------------------------------------
head -n 10 salidita.txt | cut -f 4 | grep -v -E ">[0-9]+"
        Resultado
Cluster 0
Cluster 1
---------------------------------------------------------------------------------------------------------------------------------------------------
head -n 10 salidita.txt | cut -f 4 | grep -E -w "[[:alnum:]]+ ["
        Resultado
grep: Invalid regular expression
---------------------------------------------------------------------------------------------------------------------------------------------------
head -n 10 salidita.txt | cut -f 4 | grep -E -w "^[[:alnum:]]+"
        Resultado
Cluster 0
Cluster 1 #Solo selecciona las palabras 'Cluster'
---------------------------------------------------------------------------------------------------------------------------------------------------
head -n 10 salidita.txt | cut -f 4 | grep -E -w "[a-zA-Z]+"
        Resultado
Cluster 1
>2505553514 PphNPS3121_0030.00000010 Non-ribosomal peptide synthetase modules and related proteins [Pseudomonas syringae PphNPS3121]
>2505554354 PphNPS3121_0043.00004260 Non-ribosomal peptide synthetase modules and related proteins [Pseudomonas syringae PphNPS3121]
>2505554355 PphNPS3121_0043.00004270 amino acid adenylation domain-containing protein [Pseudomonas syringae PphNPS3121]
>2549668513 NZ4DRAFT_03256 arthrofactin-type cyclic lipopeptide synthetase C [Pseudomonas syringae ICMP 18804]
>2633064784 Ga0077257_10191 AMP-binding enzyme [Pseudomonas amygdali pv. tabaci yuexi-1]
>2633064986 Ga0077257_108013 Thioesterase domain-containing protein [Pseudomonas amygdali pv. tabaci yuexi-1]
>2633064989 Ga0077257_108016 amino acid adenylation domain-containing protein [Pseudomonas amygdali pv. tabaci yuexi-1]
#Solo selecciona lo que son las palabras, mas no los numeros y corchetes o aquellos que parezcan codigos
---------------------------------------------------------------------------------------------------------------------------------------------------
```
```
head -n 10 salidita.txt | cut -f 4 | grep -E -w "[[a-zA-Z]+ [[:alnum:]]+"
```
Resultado
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/7636affb-aaa0-4250-93ad-eb9b38060e3f)
```
head -n 10 salidita.txt | cut -f 4 | grep -E -w "[[a-zA-Z]+ [[:alnum:]]+]"
```
Resultado
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/97492bcc-b290-4417-8451-23fff1ab2cde)

```
head -n 10 salidita.txt | cut -f 4 | grep -o '\[.*\]'
```
Resultado
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/679cf6f1-3241-44e0-8c23-aef5df1128ee)
```
head -n 10 salidita.txt | cut -f 4 | grep -v '\[.*\]'
```
Resultado
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/a483bdac-a439-4b96-90e1-a70abaf06190)
```
head -n 10 salidita.txt | cut -f 4 | grep -o '* \[.*\]'
head -n 10 salidita.txt | cut -f 4 | grep -o '[0-9]+ .* \['
head -n 10 salidita.txt | cut -f 4 | grep -o '[0-9]^ .* \['
head -n 10 salidita.txt | cut -f 4 | grep -o '^[0-9] .* \['
head -n 10 salidita.txt | cut -f 4 | grep -o '[[0-9][0-9]] .* \['
head -n 10 salidita.txt | cut -f 4 | grep -o '>[0-9]+ .* \['
head -n 10 salidita.txt | cut -f 4 | grep -o '>[0-9]+ .*. \['
```
Resultado
nada jaja
```
head -n 10 salidita.txt | cut -f 4 | grep -o '.* \['
```
Resultado
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/667017de-db17-4ca0-8954-ffbc53b8636d)
```
head -n 10 salidita.txt | cut -f 4 | grep -o '^.* \['
```
Resultado
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/1ca23d4d-b588-4c28-962a-f8f55daf9937)
```
head -n 10 salidita.txt | cut -f 4 | grep -o '7 .* \['
```
Resultado
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/714bfa6a-6c0d-4a7d-962b-8e618dbd7cab)
```
head -n 10 salidita.txt | cut -f 4 | grep -o '[0-9] .* \['
```
Resultado
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/a1ed7f40-3f48-4ea5-bfdd-34b226873929)

```
head -n 10 salidita.txt | cut -f 4 | grep -o '[0-9][0-9] .* \['
```
Resultado
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/51be8cfc-3101-4de7-84a0-b0b823527b28)

```
head -n 10 salidita.txt | cut -f 4 | grep -o ' .* \['
head -n 10 salidita.txt | cut -f 4 | grep -o ' .*. \['
head -n 10 salidita.txt | cut -f 4 | grep -o ' .*.. \['
head -n 10 salidita.txt | cut -f 4 | grep -o ' .*... \['
head -n 10 salidita.txt | cut -f 4 | grep -o ' ..*... \['
```
Resultado
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/29be6d6f-6d6c-4c67-bf07-379bec0ce972)
```
head -n 10 salidita.txt | cut -f 4 | grep -o '  .* \['
```
Resultado
nada jaja, se parece al de arriba, pero aparece nadota

```
head -n 10 salidita.txt | grep "*" | cut -f 4 | grep -o '^[^[]*'
```
Resultado
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/ba51732a-d6a3-4f3c-aca3-21dd717dd3b8)

```
head -n 10 salidita.txt | grep "*" | cut -f 4 | grep -o '[^[]*'
```
Resultado
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/daa8d617-7c41-4f0c-ad6e-22e6693b41bc)

```
head -n 10 salidita.txt | grep "*" | cut -f 4 | grep -o '^[^[]*' | grep " .*"
```
Resultado
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/2e8cdc65-6043-4063-b60d-78bac99bd142)


```
head -n 10 salidita.txt | grep "*" | cut -f 4 | grep -o '^[^[]*' | grep -o " .*"
```
Resultado
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/9ced872f-1b52-4d71-a78b-a2b577e19631)


```
head -n 10 salidita.txt | grep "*" | cut -f 4 | grep -o '^[^[]*' | grep -o " .*" | grep -o '[^ ].*'
```
Resultado
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/3abfd96a-88ea-4739-b21d-04328b820177)
Porfin se le pudo quitar el espacio que estaba antes del texto, esto gracias a ChatGPT, se puede anexar este comando, para filtrar la informacion y colocarla como columnas.

```

```
Resultado


```

```
Resultado



