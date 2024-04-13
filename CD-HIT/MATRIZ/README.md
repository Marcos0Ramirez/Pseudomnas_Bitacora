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

## Fecha 8 de abril del 2024

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
-------------------------------------------------------------------------------------------------------------------------------------
Ahora por otra parte, se busca entender como es que se puede concatenar la informacion de los nombres de las columnas
```
#!/bin/bash
n=1
k=20

lista=("1" "2" "3" "4" "5" "6" "7" "8" "9" "10" "a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k")

varia=""
letras=""
while [[ $n -lt 21 ]]; do
        echo "$n"
        if [[ $n -gt 10 ]]; then
                varia="$varia\t$n"
                letras="$letras\t${lista[$n]}" #Llamamos los datos con la posicion y concatenandola, separandola por tabs en expresion regular
        fi
        n=$((n+1))
        echo -e "$varia" > PIza
        echo -e "$letras" >> PIza #Guardamos la info, imprimiendola, leyendola como una expresion regular

done
```
Resultado
```
less PIza
        11      12      13      14      15      16      17      18      19      20
        b       c       d       e       f       g       h       i       j       k
```
Finalmente, podemos poner a disposicion el codigo anexado para generar las columnas
```
#!/bin/bash
saluditos="/Direccion/Descargas_NCBI/CDHIT/MATRIXDATA/salidita.txt"
pizzerola=$(cat "$saluditos" | grep "*" | cut -f 3,4 | head -n 10)

clustercols=""
genecols=""
bacteriacols=""

while C= read -r cols; do
        #echo "$cols"
        namecluster=$(echo "$cols" | cut -f 1)
        #echo "$namecluster"
        clustercols="$clustercols\t$namecluster"
        namegene=$(echo "$cols" | cut -f 2 | grep -o '^[^[]*' | grep -o " .*" | grep -o '[^ ].*')
        #echo "$namegene"
        genecols="$genecols\t$namegene"
        namebacteria=$(echo "$cols" | cut -f 2 | grep -o '\[.*\]')
        #echo "$namebacteria"
        bacteriacols="$bacteriacols\t$namebacteria"
        # echo -e "$bacteriacols"
done <<< "$pizzerola"

echo -e "$clustercols" >> "/Direccion/Descargas_NCBI/CDHIT/MATRIXDATA/columnas.txt"
echo -e "$genecols" >> "/Direccion/Descargas_NCBI/CDHIT/MATRIXDATA/columnas.txt"
echo -e "$bacteriacols" >> "/Direccion/Descargas_NCBI/CDHIT/MATRIXDATA/columnas.txt"
```
Resultado
```
        Cluster 0       Cluster 1       Cluster 2       Cluster 3       Cluster 4       Cluster 5       Cluster 6       Cluster 7       Cluster 8       Cluster 9
        Ga0304784_1247 RIP homotypic interaction motif (RHIM)-containing protein        NZ4DRAFT_03256 arthrofactin-type cyclic lipopeptide synthetase C        NZ4DRAFT_05129 filamentous hemagglutinin        Ga0439903_01_207766_225195 filamentous hemagglutinin    Ga0398577_01_157522_174915 hypothetical protein         C163_0140 surface adhesion protein      Ga0077257_109861 Ca2+-binding protein, RTX toxin-related        Ga0439903_01_4493887_4509570 surface adhesion protein   Ga0398577_01_5612367_5627615 amino acid adenylation domain-containing protein   Q075_02967 non-ribosomal peptide synthase domain TIGR01720/amino acid adenylation domain-containing protein
        [Pseudomonas psychrophila BIGb0477]     [Pseudomonas syringae ICMP 18804]       [Pseudomonas syringae ICMP 18804]       [Pseudomonas sp. ADAK22]        [Pseudomonas synxantha 2-79]    [Pseudomonas sp. FGI182]        [Pseudomonas amygdali pv. tabaci yuexi-1]       [Pseudomonas sp. ADAK22]        [Pseudomonas synxantha 2-79]    [Pseudomonas aeruginosa BL21]
```
Asi para reconocer de cual archivo se a extraido, porque puede ser que al final, haya muchos genomas de organismos de la misma especie y por tanto se puedan repetir y no saber diferenciar.
Los que son los id de las proteinas:
1. Se extrae el numero
2. Se busca en las carpetas por independiente
3. Se extrae el id del individuos y se anexa con el nombre entre corchetes y el id del individuo
4. El id de la proteina se usa para anexar solo la informacion de la idproteina:identidad% en inteseccion con el representativo
5. Asi finalmente se crea otro script relacional, entre el archivo saluditos y la matriz, para imprimir al informacion que se desea en orden.

A continaucion con el codigo, se sustituye la columna 1 por los nombres de los individuos con el id del genoma y el nombre del individuo.
```
head -n 10 salidita.txt | grep -o -E " >[0-9]+" | grep -o '[^ ].*'
```

## Fecha 10 de abril del 2024
para entender como funciona un script para concatenar la informacion idgenoma:nombreorganismo, se realizo esta parte del script
```

```

Primero, guardo registro de como estaba quedando el script
```
#!/bin/bash
# Generacion de columnas
MATRIXDIR="/mnt/c/Users/52477/Desktop/Descargas_NCBI/CDHIT/MATRIXDATA"
saluditos="/mnt/c/Users/52477/Desktop/Descargas_NCBI/CDHIT/MATRIXDATA/salidita.txt" #Salida del archivo donde se agrego el nombre del gen/proteina
pizzerola=$(cat "$saluditos" | grep "*" | cut -f 3,4 | head -n 10)

clustercols=""
genecols=""
bacteriacols=""

while COLUMNAS= read -r cols; do
        #echo "$cols"
        namecluster=$(echo "$cols" | cut -f 1)
        #echo "$namecluster"
        clustercols="$clustercols\t$namecluster"
        namegene=$(echo "$cols" | cut -f 2 | grep -o '^[^[]*' | grep -o " .*" | grep -o '[^ ].*')
        #echo "$namegene"
        genecols="$genecols\t$namegene"
        namebacteria=$(echo "$cols" | cut -f 2 | grep -o '\[.*\]')
        #echo "$namebacteria"
        bacteriacols="$bacteriacols\t$namebacteria"
        # echo -e "$bacteriacols"
done <<< "$pizzerola"

echo -e "$clustercols" > "$MATRIXDIR/columnas.txt"
echo -e "$genecols" >> "$MATRIXDIR/columnas.txt"
echo -e "$bacteriacols" >> "$MATRIXDIR/columnas.txt"



# Aca se generan los nombres de las filas con ´idgenoma:nombreorganismo´
PWD="/mnt/c/Users/52477/Desktop/Descargas_NCBI/IMGPSEUDOMONASGENOMES/"
cd $PWD #Donde se localizan los genomas
ls * | head -n 1 */*faa > "$MATRIXDIR/idgenome_namespecie.txt"
sed '/<==/{N;s/<==\n/ /}' $MATRIXDIR/idgenome_namespecie.txt > $MATRIXDIR/idgenome_namespecie2.txt
mv $MATRIXDIR/idgenome_namespecie2.txt $MATRIXDIR/idgenome_namespecie.txt
cat "$MATRIXDIR/idgenome_namespecie.txt" |
while FILASNAME= read -r name; do
        grep -E
done <<< "$MATRIXDIR/idgenome_namespecie.txt"



# De aqui que ya estan las columnas, ahora toca agregar la informacion.
busqueda=$(grep -o -E " >[0-9]+" $saluditos | grep -o '[^ ].*' | head -n 10)
while FILAS= read -r fila; do
echo "$fila"
ls * | grep -l "$fila" */*faa

done <<< "$busqueda"
```

Ahora, modificamos el script, para que solo ponga el id y que directamente busque solo el nombre del organismo
```
#!/bin/bash
# Generacion de columnas
MATRIXDIR="/mnt/c/Users/52477/Desktop/Descargas_NCBI/CDHIT/MATRIXDATA"
saluditos="/mnt/c/Users/52477/Desktop/Descargas_NCBI/CDHIT/MATRIXDATA/salidita.txt" #Salida del archivo donde se agrego el nombre del gen/proteina
pizzerola=$(cat "$saluditos" | grep "*" | cut -f 3,4 | head -n 10)

clustercols=""
genecols=""
bacteriacols=""

while COLUMNAS= read -r cols; do
        #echo "$cols"
        namecluster=$(echo "$cols" | cut -f 1)
        #echo "$namecluster"
        clustercols="$clustercols\t$namecluster"
        namegene=$(echo "$cols" | cut -f 2 | grep -o '^[^[]*' | grep -o " .*" | grep -o '[^ ].*')
        #echo "$namegene"
        genecols="$genecols\t$namegene"
        namebacteria=$(echo "$cols" | cut -f 2 | grep -o '\[.*\]')
        #echo "$namebacteria"
        bacteriacols="$bacteriacols\t$namebacteria"
        # echo -e "$bacteriacols"
done <<< "$pizzerola"

echo -e "$clustercols" > "$MATRIXDIR/columnas.txt"
echo -e "$genecols" >> "$MATRIXDIR/columnas.txt"
echo -e "$bacteriacols" >> "$MATRIXDIR/columnas.txt"



# Aca se generan los nombres de las filas con ´idgenoma:nombreorganismo´
PWD="/mnt/c/Users/52477/Desktop/Descargas_NCBI/IMGPSEUDOMONASGENOMES/"
cd $PWD #Donde se localizan los genomas
rm $MATRIXDIR/idgenome_namespecie.txt $MATRIXDIR/idgenome_namespecie2.txt
for i in *; do
corchetes=$(head -n 1 $i/*faa | grep -Eo '\[.*\]')
echo "$i"
echo "$corchetes"

echo "$i:$corchetes" >> $MATRIXDIR/idgenome_namespecie.txt
done

# sed '/<==/{N;s/<==\n/ /}' $MATRIXDIR/idgenome_namespecie.txt > $MATRIXDIR/idgenome_namespecie2.txt
# mv $MATRIXDIR/idgenome_namespecie2.txt $MATRIXDIR/idgenome_namespecie.txt
# cat "$MATRIXDIR/idgenome_namespecie.txt" |
# while FILASNAME= read -r name; do
#       grep -E
# done <<< "$MATRIXDIR/idgenome_namespecie.txt"

# De aqui que ya estan las columnas, ahora toca agregar la informacion.
#busqueda=$(grep -o -E " >[0-9]+" $saluditos | grep -o '[^ ].*' | head -n 10)
#while FILAS= read -r fila; do
#echo "$fila"
#ls * | grep -l "$fila" */*faa

#done <<< "$busqueda"
```

## Fecha 11 de abril del 2024
Por el momento, queda de constancia, que la matriz se quiere tener esta connotación
Conjunto de datos muestra
```
0       171aa, >2505553514... at 60.82%         Cluster 1       >2505553514 PphNPS3121_0030.00000010 Non-ribosomal peptide synthetase modules and related proteins [Pseudomonas syringae PphNPS3121]
1       895aa, >2505554354... at 65.59%         Cluster 1       >2505554354 PphNPS3121_0043.00004260 Non-ribosomal peptide synthetase modules and related proteins [Pseudomonas syringae PphNPS3121]
2       1002aa, >2505554355... at 83.93%        Cluster 1       >2505554355 PphNPS3121_0043.00004270 amino acid adenylation domain-containing protein [Pseudomonas syringae PphNPS3121]
3       5929aa, >2549668513... *        Cluster 1       >2549668513 NZ4DRAFT_03256 arthrofactin-type cyclic lipopeptide synthetase C [Pseudomonas syringae ICMP 18804]
4       154aa, >2633064784... at 89.61%         Cluster 1       >2633064784 Ga0077257_10191 AMP-binding enzyme [Pseudomonas amygdali pv. tabaci yuexi-1]
5       313aa, >2633064986... at 86.90%         Cluster 1       >2633064986 Ga0077257_108013 Thioesterase domain-containing protein [Pseudomonas amygdali pv. tabaci yuexi-1]
6       1239aa, >2633064989... at 85.55%        Cluster 1       >2633064989 Ga0077257_108016 amino acid adenylation domain-containing protein [Pseudomonas amygdali pv. tabaci yuexi-1]
7       90aa, >2633064990... at 74.44%  Cluster 1       >2633064990 Ga0077257_108017 arthrofactin-type cyclic lipopeptide synthetase C [Pseudomonas amygdali pv. tabaci yuexi-1]
8       3475aa, >2633065112... at 87.08%        Cluster 1       >2633065112 Ga0077257_108411 arthrofactin-type cyclic lipopeptide synthetase C [Pseudomonas amygdali pv. tabaci yuexi-1]
9       5889aa, >2714614382... at 71.81%        Cluster 1       >2714614382 Ga0124767_1046121 arthrofactin-type cyclic lipopeptide synthetase C [Pseudomonas syringae pv. primulae ICMP3956]
```

Para el cual con respecto a identificar, donde se encuentra el gen/proteina. 
1. Se usa id del gen/proteina
2. Se busca en que genoma se encuentra
3. Finalmente se llama el nombre del genoma, se concatena la informacion en su respectiva columna y fila,
4. Si no hay nada se pone 0, si hay alguno se va sumando con los otros.

```
              | 0    | 1   |
--------------------------------
2505313052    | 0    | 3    |
2517572175    | 0    | 0    |
2548876750    | 0    | 1    |
2554235471    | 0    | 0    |
2630968743    | 0    | 5    |
2713896862    | 0    | 1    |
2785510749    | 1    | 0    |
2923166773    | 0    | 0    |
2972001829    | 0    | 0    |
8011072914    | 0    | 0    |
```
Avance del codigo, hasta la parte de obtener el nombre del archivo donde se encuntra la proteina identificada, solo falta generar la matriz y dividir por cluster
```
#!/bin/bash

DIR="/mnt/c/Users/52477/Desktop/Descargas_NCBI"
MATRIXCDOUT="CDHIT/MATRIXDATA"
DATA="CDHIT/TODOS/clusterprotcatALL2000.clstr"

#ls $DIR/$MATRIXCDOUT
#head -n 10 $DIR/$DATA

# Patrón para identificar el inicio de un nuevo cluster
patron1=">Cluster"
patron2="[0-9]+aa"
ni=0
nfinal=$(grep -E "$patron1" $DIR/$DATA | wc -l)
nfinal=$((nfinal-1))
echo $nfinal
# Iterar sobre el archivo
cd $DIR/IMGPSEUDOMONASGENOMES
while [[ $ni -le $nfinal ]]; do
        limitei=$(grep -o -n -w "Cluster $ni" $DIR/$DATA | grep -Eo "^[0-9]+")
        nf=$((ni+1))
        limitef=$(grep -o -n -w "Cluster $nf" $DIR/$DATA | grep -Eo "^[0-9]+")
        limitei=$((limitei+1))
        limitef=$((limitef-1))
        clusterset=$(sed -n "$limitei,${limitef}p" $DIR/$DATA)
        pizzitas=""
        pizzitas="$pizzitas\t$ni" # Agrega el numero del cluster
        echo "$clusterset" | while M= read -r  lineas; do
                busqueda=$(echo "$lineas" | grep -E -o -w ">[0-9]+") # Toma el id de la proteina para relizar la busqueda en los genomas
                #echo "$busqueda"
                queso=$(grep -l "$busqueda" */*faa | grep -Eo "^[0-9]+") # Hace la busqueda del id del genoma solo el que aparece por primera vez idgenome/idgenome.genes.faa
                pizzitas="$pizzitas\t$queso" # Concatena la informacion, con respecto al cluster y al id de las proteinas
        done <<< "$clusterset"
        echo -e "$pizzitas" expresa la informacion respetando las expresiones regulares.
        ni=$((ni+1))
done
```

Fecha 12 de abril del 2024
El dia de hoy de modifico el codigo de esta forma:
```
        done <<< "$clusterset"
        echo -e "$pizzitas" > "$DIR/$MATRIXCDOUT/clust.tmp"
        echo -e "$pizzitas"
        # head -n 15 "$DIR/$MATRIXCDOUT/clust.tmp"
        for i in *
        do
                reps=$(grep -o "$i" "$DIR/$MATRIXCDOUT/clust.tmp" | wc -l)
                echo "id genoma: $i y se repite: $reps"
        done
        ni=$((ni+1))
done
```
lo que permite identificar, con que frecuencia aparecen los genomas, la cual concuerda con lo esperado. Solo queda concatenar para hacer una matriz
```
19000
2505313052 2517572175 2548876750 2554235471 2630968743 2713896862 2785510749 2923166773 2972001829 8011072914
        0
2785510749
id genoma: 2505313052 y se repite: 0
id genoma: 2517572175 y se repite: 0
id genoma: 2548876750 y se repite: 0
id genoma: 2554235471 y se repite: 0
id genoma: 2630968743 y se repite: 0
id genoma: 2713896862 y se repite: 0
id genoma: 2785510749 y se repite: 1
id genoma: 2923166773 y se repite: 0
id genoma: 2972001829 y se repite: 0
id genoma: 8011072914 y se repite: 0
        1
2505313052
2505313052
2505313052
2548876750
2630968743
2630968743
2630968743
2630968743
2630968743
2713896862
id genoma: 2505313052 y se repite: 3
id genoma: 2517572175 y se repite: 0
id genoma: 2548876750 y se repite: 1
id genoma: 2554235471 y se repite: 0
id genoma: 2630968743 y se repite: 5
id genoma: 2713896862 y se repite: 1
id genoma: 2785510749 y se repite: 0
id genoma: 2923166773 y se repite: 0
id genoma: 2972001829 y se repite: 0
id genoma: 8011072914 y se repite: 0
```
Codigo final, de la ultima parte del comando de clusterizacion hasta la generacion de la matriz
```
#!/bin/bash

DIR="/mnt/c/Users/52477/Desktop/Descargas_NCBI"
MATRIXCDOUT="CDHIT/MATRIXDATA"
DATA="CDHIT/TODOS/clusterprotcatALL2000.clstr"
rm "$DIR/$MATRIXCDOUT/clust.tmp"
#ls $DIR/$MATRIXCDOUT
#head -n 10 $DIR/$DATA

# Patrón para identificar el inicio de un nuevo cluster
patron1=">Cluster"
patron2="[0-9]+aa"
ni=0
nfinal=$(grep -E "$patron1" $DIR/$DATA | wc -l)
nfinal=$((nfinal-1))
echo $nfinal
# Iterar sobre el archivo
cd $DIR/IMGPSEUDOMONASGENOMES
echo "idgenomas" > $DIR/$MATRIXCDOUT/matriz.txt
ls | tr '\s' '\n' >> $DIR/$MATRIXCDOUT/matriz.txt
# cat $DIR/$MATRIXCDOUT/matriz.txt
while [[ $ni -le $nfinal ]]; do
        limitei=$(grep -o -n -w "Cluster $ni" $DIR/$DATA | grep -Eo "^[0-9]+")
        nf=$((ni+1))
        limitef=$(grep -o -n -w "Cluster $nf" $DIR/$DATA | grep -Eo "^[0-9]+")
        limitei=$((limitei+1))
        limitef=$((limitef-1))
        clusterset=$(sed -n "$limitei,${limitef}p" $DIR/$DATA)
        pizzitas=""
        pizzitas="$pizzitas\t$ni"
        while M= read -r  lineas; do
                busqueda=$(echo "$lineas" | grep -E -o -w ">[0-9]+")
                #echo "$busqueda"
                queso=$(grep -l "$busqueda" */*faa | grep -Eo "^[0-9]+")
                pizzitas="$pizzitas\n$queso"
        done <<< "$clusterset"


        echo "$ni" > "$DIR/$MATRIXCDOUT/clust.tmp"
        cont=""
        echo "$ni"
        for i in *
        do
                reps=$(echo -e "$pizzitas" | grep -o "$i" | wc -l)
                cont="$cont\n$reps"
                echo "$i: $reps"
        done
        n=$(ls | tr '\s' '\n' | wc -l)
        #n=$(($n-1))
        cont=$(echo -e "$cont" | tail -n $n)
        echo -e "$cont" >> "$DIR/$MATRIXCDOUT/clust.tmp"
        paste $DIR/$MATRIXCDOUT/matriz.txt $DIR/$MATRIXCDOUT/clust.tmp > $DIR/$MATRIXCDOUT/matriz.tmp && mv $DIR/$MATRIXCDOUT/matriz.tmp $DIR/$MATRIXCDOUT/matriz.txt
        head -n $n $DIR/$MATRIXCDOUT/matriz.txt > $DIR/$MATRIXCDOUT/matriz.tmp && mv $DIR/$MATRIXCDOUT/matriz.tmp $DIR/$MATRIXCDOUT/matriz.txt
        ni=$((ni+1))
done
```
Empezo a las 5:50 pm y termino a las 10:50 pm, por lo que tardo 5 horas en hacer la matriz.
Al final aparecio este mensaje
```
18998
2505313052: 1
2517572175: 0
2548876750: 0
2554235471: 0
2630968743: 0
2713896862: 0
2785510749: 0
2923166773: 0
2972001829: 0
8011072914: 0
matriz.txt: 0
18999
2505313052: 1
2517572175: 0
2548876750: 0
2554235471: 0
2630968743: 0
2713896862: 0
2785510749: 0
2923166773: 0
2972001829: 0
8011072914: 0
matriz.txt: 0
sed: -e expression #1, char 7: unexpected `,'
19000
2505313052: 1
2517572175: 1
2548876750: 1
2554235471: 1
2630968743: 1
2713896862: 1
2785510749: 1
2923166773: 1
2972001829: 1
8011072914: 1
matriz.txt: 0
```
Lo que indica que solo se debe agregar un condicional para el ultimo cluster y termine bien, sin que aparezca el ultimo mensaje.
Parte de la matriz de salida
```
idgenomas       0       1       2       3       4       5       6       7       8
2505313052      0       3       0       0       0       0       1       0       1
2517572175      0       0       0       0       0       1       0       0       0
2548876750      0       1       4       0       0       0       1       0       0
2554235471      0       0       0       0       0       0       0       0       0
2630968743      0       5       2       0       0       0       1       0       0
2713896862      0       1       1       0       0       0       0       0       0
2785510749      1       0       0       0       0       0       0       0       0
2923166773      0       0       0       1       0       0       0       1       0
2972001829      0       0       0       0       1       0       0       0       1
8011072914      0       0       0       0       0       0       0       0       0
```
Fecha 13 de abril del 2024
Para hacer el condicional y funcione bien la extraccion de lineas para el final del archivo, solo se trata de entender como hacer para que en automatico solo saque las ultimas lineas
```
prueba=$(head -n 30 ../CDHIT/TODOS/clusterprotcatALL2000.clstr)
echo "$prueba"
Respuesta
>Cluster 0
0       6388aa, >2785749539... *
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
>Cluster 2
0       5824aa, >2549670384... *
1       389aa, >2549670765... at 97.94%
2       105aa, >2549670769... at 98.10%
3       514aa, >2549670774... at 76.46%
4       4780aa, >2633066528... at 67.68%
5       1072aa, >2633066529... at 88.62%
6       4093aa, >2714616755... at 68.90%
>Cluster 3
0       5809aa, >2923166973... *
>Cluster 4
0       5797aa, >2972001972... *
>Cluster 5
0       5603aa, >2518032096... *
>Cluster 6
0       1547aa, >2505552225... at 99.10%
1       215aa, >2549670875... at 72.56%
```
```
echo "$prueba" | tail -n 1

Respuesta
1       215aa, >2549670875... at 72.56%
```
```
ult=$(echo "$prueba" | tail -n 1)
echo "$prueba" | grep -n "$ult"
```
Respuesta
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/8f9b77da-d01b-43ef-b4ef-e9af1606aa6d)
```
echo "$prueba" | grep -n "$ult" | grep -o "^[0-9]"
Respuesta
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/61b53707-1e2d-4d44-a165-f436f06c37ec)

```
echo "$prueba" | grep -n "$ult" | grep -o "^[0-9]*"
```
Respuesta
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/c4e77dd4-9bd7-4297-a032-ba0aa0a70837)
Finalmente quedo corregido el codigo, aunque sea posible sea unos segundos mas lento en procesar, asegura la correcta recoleccion de los datos para hacer la matriz:
Para ello presentamos el la parte del set de datos a usar con las condiciones iguales al del archivo:
```
>Cluster 0
0       6388aa, >2785749539... *
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
>Cluster 2
0       5824aa, >2549670384... *
1       389aa, >2549670765... at 97.94%
2       105aa, >2549670769... at 98.10%
3       514aa, >2549670774... at 76.46%
4       4780aa, >2633066528... at 67.68%
5       1072aa, >2633066529... at 88.62%
6       4093aa, >2714616755... at 68.90%
>Cluster 3
0       5809aa, >2923166973... *
>Cluster 4
0       5797aa, >2972001972... *
>Cluster 5
0       5603aa, >2518032096... *
>Cluster 6
0       1547aa, >2505552225... at 99.10%
1       215aa, >2549670875... at 72.56%
```
Con el codigo
```
#!/bin/bash

DIR="/mnt/c/Users/52477/Desktop/Descargas_NCBI"
MATRIXCDOUT="CDHIT/MATRIXDATA"
DATA="CDHIT/TODOS/clusterprotcatALL2000.clstr"

#Prueba rapida para el final del codigo
head -n 30 $DIR/$DATA > "$DIR/CDHIT/TODOS/30rengclusterprotcatALL2000.clstr"
DATA="CDHIT/TODOS/30rengclusterprotcatALL2000.clstr"
rm "$DIR/$MATRIXCDOUT/clust2.tmp"
#ls $DIR/$MATRIXCDOUT
#head -n 10 $DIR/$DATA

# Patrón para identificar el inicio de un nuevo cluster
patron1=">Cluster"
patron2="[0-9]+aa"
ni=0
nfinal=$(grep -E "$patron1" $DIR/$DATA | wc -l)
nfinal=$((nfinal-1))
echo $nfinal
# Iterar sobre el archivo
cd $DIR/IMGPSEUDOMONASGENOMES
echo "idgenomas" > $DIR/$MATRIXCDOUT/matriz2.txt
ls | tr '\s' '\n' >> $DIR/$MATRIXCDOUT/matriz2.txt
# cat $DIR/$MATRIXCDOUT/matriz.txt
while [[ $ni -le $nfinal ]]; do
        limitei=$(grep -o -n -w "Cluster $ni" $DIR/$DATA | grep -Eo "^[0-9]+")
        nf=$((ni+1))
        limitef=$(grep -o -n -w "Cluster $nf" $DIR/$DATA | grep -Eo "^[0-9]+")
        limitei=$((limitei+1))
        limitef=$((limitef-1))
        if [ $limitef != "-1" ]; then
        clusterset=$(sed -n "$limitei,${limitef}p" "$DIR/$DATA")
        else
        echo "ultimoski pa"
        ult=$(tail -n 1 $DIR/$DATA)
        limitef=$(grep -n "$ult" $DIR/$DATA | grep -o "^[0-9]*")
        clusterset=$(sed -n "$limitei,${limitef}p" "$DIR/$DATA")
        fi
        pizzitas=""
        pizzitas="$pizzitas\t$ni"
        while M= read -r  lineas; do
                busqueda=$(echo "$lineas" | grep -E -o -w ">[0-9]+")
                #echo "$busqueda"
                queso=$(grep -l "$busqueda" */*faa | grep -Eo "^[0-9]+")
                pizzitas="$pizzitas\n$queso"
        done <<< "$clusterset"


        echo "$ni" > "$DIR/$MATRIXCDOUT/clust2.tmp"
        cont=""
        echo "$ni"
        for i in *
        do
                reps=$(echo -e "$pizzitas" | grep -o "$i" | wc -l)
                cont="$cont\n$reps"
                echo "$i: $reps"
        done
        n=$(ls | tr '\s' '\n' | wc -l)
        #n=$(($n-1))
        cont=$(echo -e "$cont" | tail -n $n)
        echo -e "$cont" >> "$DIR/$MATRIXCDOUT/clust2.tmp"
        paste $DIR/$MATRIXCDOUT/matriz2.txt $DIR/$MATRIXCDOUT/clust2.tmp > $DIR/$MATRIXCDOUT/matriz2.tmp && mv $DIR/$MATRIXCDOUT/matriz2.tmp $DIR/$MATRIXCDOUT/matriz2.txt
        head -n $n $DIR/$MATRIXCDOUT/matriz2.txt > $DIR/$MATRIXCDOUT/matriz2.tmp && mv $DIR/$MATRIXCDOUT/matriz2.tmp $DIR/$MATRIXCDOUT/matriz2.txt
        ni=$((ni+1))
done
echo "$ni"
echo "$nf"
echo "$limitei"
echo "$limitef"
```
Y con salida al correr
```
6
0
2505313052: 0
2517572175: 0
2548876750: 0
2554235471: 0
2630968743: 0
2713896862: 0
2785510749: 1
2923166773: 0
2972001829: 0
8011072914: 0
matriz.txt: 0
1
2505313052: 3
2517572175: 0
2548876750: 1
2554235471: 0
2630968743: 5
2713896862: 1
2785510749: 0
2923166773: 0
2972001829: 0
8011072914: 0
matriz.txt: 0
2
2505313052: 0
2517572175: 0
2548876750: 4
2554235471: 0
2630968743: 2
2713896862: 1
2785510749: 0
2923166773: 0
2972001829: 0
8011072914: 0
matriz.txt: 0
3
2505313052: 0
2517572175: 0
2548876750: 0
2554235471: 0
2630968743: 0
2713896862: 0
2785510749: 0
2923166773: 1
2972001829: 0
8011072914: 0
matriz.txt: 0
4
2505313052: 0
2517572175: 0
2548876750: 0
2554235471: 0
2630968743: 0
2713896862: 0
2785510749: 0
2923166773: 0
2972001829: 1
8011072914: 0
matriz.txt: 0
5
2505313052: 0
2517572175: 1
2548876750: 0
2554235471: 0
2630968743: 0
2713896862: 0
2785510749: 0
2923166773: 0
2972001829: 0
8011072914: 0
matriz.txt: 0
ultimoski pa
6
2505313052: 1
2517572175: 0
2548876750: 1
2554235471: 0
2630968743: 0
2713896862: 0
2785510749: 0
2923166773: 0
2972001829: 0
8011072914: 0
matriz.txt: 0
7
7
29
30
```
Y con la matriz del archivo matriz2.txt
```
idgenomas       0       1       2       3       4       5       6
2505313052      0       3       0       0       0       0       1
2517572175      0       0       0       0       0       1       0
2548876750      0       1       4       0       0       0       1
2554235471      0       0       0       0       0       0       0
2630968743      0       5       2       0       0       0       0
2713896862      0       1       1       0       0       0       0
2785510749      1       0       0       0       0       0       0
2923166773      0       0       0       1       0       0       0
2972001829      0       0       0       0       1       0       0
8011072914      0       0       0       0       0       0       0
```
Ahora solo queda que se genere una bitacora de salida y que agregue fecha y hora de inicio y fecha y hora de termino y con un script que pueda indicar cuales son las direcciones de los archivos y las salidas de trabajo.















