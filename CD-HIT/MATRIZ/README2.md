# 20 de abril del 2024
Ahora se vera como desarrollar el script para que corrar mas rapido el analisis y no tenga que estar abriendo los archivos a cada rato y haviendo busquedas tan largas

1. Para ello se piensa crear una tabla con todas las accesiones y que desdes ahi haga la busqueda
2. sustituir sed por otra funcion

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

En este momento se pretende entender como es que se puede extraer y guardarlos en una variable para trabajar con ello podemos guardar todas lad porteinas
Trabajamos dentro de la carpta donde estan los genomas
```
grep -E ">" */*faa > ../CDHIT/MATRIXDATA/200424_grepfaa.txt
Resultado
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/bec1e382-0918-478a-831b-52d4197205b8)

Asi se guarda y podemos usar solo lo que necesitamos, las accesiones
```
grep -E -o ">[0-9]+" */*faa > ../CDHIT/MATRIXDATA/200424_grepfaa.txt
Resultado
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/b74df911-cc88-45a1-911c-071b3e1aebb8)

```
grep -E -o ">[0-9]+" */*faa | awk -F "/[0-9]+.genes.faa:>" '{print $1 ":" $2}'
Resultado
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/0711ea3c-38aa-4ab8-b21c-02d5bec4c7bd)

Lugar donde se guarda la salida
```
grep -E -o ">[0-9]+" */*faa | awk -F "/[0-9]+.genes.faa:>" '{print $1 ":" $2}' > ../CDHIT/MATRIXDATA/200424_grepfaa.txt
```

```
Asi permite que la busqueda solo tenga las accesiones id del genoma y de la proteina
Y por otra parte awk, con -F excluye lo que se encuentra en el patron y asi permite que la infor que este entre ellos se dividan en nuevos y sean impresos separados por ":"
```

Asi por otra parte con la tabla de salida de CD-HIT clusterprotcatALL2000.clstr:
```
awk -F ">" '{print $2}' clusterprotcatALL2000.clstr
Resultado
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/66ae443b-10fd-4154-bd28-669690640026)

```
awk -F ">" '{print $2}' clusterprotcatALL2000.clstr | awk -F "." '{print $1}'
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/af344cfc-13b6-4f6e-a9a5-c44801b9faed)

Asi con la salida de esta busqueda, podemos trabajar
```
awk -F ">" '{print $2}' clusterprotcatALL2000.clstr | awk -F "." '{print $1}' > ../MATRIXDATA/filtclusterprotcatALL2000.clstr
```
Y establecer como va a ser el conteo para guardarlo en la matriz
Por otra parte, vemos como actuaria `for` para leer las lineas de `filtclusterprotcatALL2000.clstr`
```
for i in $(cat filtclusterprotcatALL2000.clstr); do echo $i; done
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/f8bb1bca-04c3-4bf8-aafc-764b9859ac3c)

Pero ahora lo que hacemos es quita el espacio para que aparezca asi
```
awk '{gsub(/\s/, "", $0); print}' filtclusterprotcatALL2000.clstr
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/692c174d-0df2-46c3-ab43-980b90d78af8)

Asi para guardarlo en el mismo archivo, solo lo movemos
```
awk '{gsub(/\s/, "", $0); print}' filtclusterprotcatALL2000.clstr > tmp.tmp && mv tmp.tmp filtclusterprotcatALL2000.clstr
```
Finalmente solo para comprobar que tanto tiempo puee tardar con hacer busquedas con un `for` y `grep`.
```
date +%H:%M:%S && for i in $(cat filtclusterprotcatALL2000.clstr); do grep "$i" 200424_grepfaa.txt | grep -E "^[0-9]+" >> tmp.tmp; done && date +%H:%M:%S
```
Si tenemos un total de lineas `grep -v -c "Cluster" filtclusterprotcatALL2000.clstr`: `56287`
Con un inicio de horas `23:37:04` y termino a las `00:17:50`, pero al final corrio con `wc -l ../CDHIT/MATRIXDATA/tmp.tmp`: `68186` lo que tal vez fue porque dentro del archivo `filtclusterprotcatALL2000.clstr` tambien se encuentra `Cluster[0-9]+` algun numero, por lo que puede buscar coincidencias con respecto a los numeros, pero faltara ver que show con el comando y ver si es mas rapido con `awk`. Tiempo aprox 40 min.

Asi podemos agregar un `if` al script para que detecte los Cluster y empiece a contar linea por linea.

## Fecha 21 de abril del 2024
Hoy se vio que es mas rapido de trabajar y se desarrollo un script para medir el tiempo y ver cual es mar rapido si `awk` o `for`
```
#!/bin/bash

GENOMES="/mnt/c/Users/52477/Desktop/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="/mnt/c/Users/52477/Desktop/Descargas_NCBI/CDHIT/MATRIXDATA"

io=$(date +%H:%M:%S)
awk '/[0-9]+/' $WORK/filtclusterprotcatALL2000.clstr
f=$(date +%H:%M:%S)

ig=$(date +%H:%M:%S)
for i in $(cat $WORK/filtclusterprotcatALL2000.clstr); do echo $i; done
fg=$(date +%H:%M:%S)

echo "awk inicio a las $io y termino a las $f"
echo "for inicio a las $ig y termino a las $fg"
```
Con tiempos de termino 
```
awk inicio a las 10:06:19 y termino a las 10:06:36
for inicio a las 10:06:36 y termino a las 10:06:59
```
y por tanto `awk` es mas rapido con 17 segundos y `for` con 20 segundos
Ahora con awk y con un resultado igual al anteiorr con las busquedas por `for` se obtuvieron a la mitad de tiempo 
```
#!/bin/bash

GENOMES="Direccion/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="Dirección/Descargas_NCBI/CDHIT/MATRIXDATA"

io=$(date +%H:%M:%S)
while read linea
do
    grep "$linea" "$WORK/200424_grepfaa.txt" >> temp.temp
done < "$WORK/filtclusterprotcatALL2000.clstr"
f=$(date +%H:%M:%S)

echo "while read con awk para busqueda en un segundo archivo inicio a las $io y termino a las $f"
```
asi
```
while read con grep para busqueda en un segundo archivo inicio a las 10:50:06 y termino a las 11:11:37
```

Ahora con pequeñas modificaciones para que pueda responder a agregar Cluster en el archivo temporal
```
#!/bin/bash

GENOMES="Direccion/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="Direccion/Descargas_NCBI/CDHIT/MATRIXDATA"
rm temp.temp
io=$(date +%H:%M:%S)
while read linea
do
        if [[ $linea =~ "Cluster" ]]
        then
                echo "$linea" >> temp.temp
        fi
        grep "$linea" "$WORK/200424_grepfaa.txt" >> temp.temp
done < "$WORK/filtclusterprotcatALL2000.clstr"
f=$(date +%H:%M:%S)

echo "while read con grep para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las $io y termino a las $f"
```
Por esta parte funciona agregar, pero sigue haciendo proceso de mas, por lo que es posible que este tomando info de los numero de CLuster y los use para buscar en las similitudes de numeros y por tanto aparezcan de mas, si tenemos del archivo `filtclusterprotcatALL2000.clstr` 75288 lineas y con la salida final de 
`temp.temp` tenemos un total de 87187 con 23 minutos
```
while read con grep para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las 11:42:52 y termino a las 12:05:22
```

Finalmente de corregir con un condicional bien estructurado, se rompio record a la hora de correr el script y termino muy pronto con menos de un minuto
```
#!/bin/bash

GENOMES="Direccion/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="Direccion/Descargas_NCBI/CDHIT/MATRIXDATA"
rm temp.temp
io=$(date +%H:%M:%S)
while read linea
do
        if [[ $linea =~ "Cluster" ]]
        then
                echo "$linea" >> temp.temp
        else
                echo "$linea" "$WORK/200424_grepfaa.txt" >> temp.temp
        fi
done < "$WORK/filtclusterprotcatALL2000.clstr"
f=$(date +%H:%M:%S)

echo "while read con grep para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las $io y termino a las $f"
```
Resultado
```
while read con grep para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las 12:09:37 y termino a las 12:10:09
```
## OLVIDEN ESO, ME EQUIVOQUE EN ELSE, EN LUGAR DE ECHO VA GREP
Aca corregido
Ahora agregando el comando para hacer que solo de el numero de id del genoma
```
#!/bin/bash

GENOMES="Direccion/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="Direccion/Descargas_NCBI/CDHIT/MATRIXDATA"
rm temp.temp
io=$(date +%H:%M:%S)
while read linea
do
        if [[ $linea =~ "Cluster" ]]
        then
                echo "$linea" >> temp.temp
        else
                grep "$linea" "$WORK/200424_grepfaa.txt" >> temp.temp
        fi
done < "$WORK/filtclusterprotcatALL2000.clstr"
f=$(date +%H:%M:%S)

echo "while read con grep para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las $io y termino a las $f"
```
nunca termino
Ahora solo con un pequeño set de datos, veremos que esta pasando
```
#!/bin/bash

GENOMES="/mnt/c/Users/52477/Desktop/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="/mnt/c/Users/52477/Desktop/Descargas_NCBI/CDHIT/MATRIXDATA"
rm temp.temp
io=$(date +%H:%M:%S)
head -n 100 "$WORK/filtclusterprotcatALL2000.clstr" | while read linea
do
        if [[ $linea =~ "Cluster" ]]
        then
                echo "$linea" >> temp.temp
        else
                awk -v pattern="$linea" '$0 ~ pattern' "$WORK/200424_grepfaa.txt" >> temp.temp
        fi
done
f=$(date +%H:%M:%S)

echo "while read con awk para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las $io y termino a las $f"
```
Con un total de tiempo y el cual `temp.temp` resulta en 100 líneas 
```
while read con awk para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las 12:55:11 y termino a las 12:55:14
```
Ahora lo intentamos con todos, pero en modo de tunel con los datos
```
#!/bin/bash

GENOMES="/mnt/c/Users/52477/Desktop/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="/mnt/c/Users/52477/Desktop/Descargas_NCBI/CDHIT/MATRIXDATA"
rm temp.temp
io=$(date +%H:%M:%S)
cat "$WORK/filtclusterprotcatALL2000.clstr" | while read linea
do
        if [[ $linea =~ "Cluster" ]]
        then
                echo "$linea" >> temp.temp
        else
                awk -v pattern="$linea" '$0 ~ pattern' "$WORK/200424_grepfaa.txt" >> temp.temp
        fi
done
f=$(date +%H:%M:%S)

echo "while read con awk para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las $io y termino a las $f"
```
Con salida
```
while read con awk para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las 12:56:27 y termino a las 13:46:37
```
COn un total de lineas de 87187 se tardo 50 minutos.

Al parecer hay id's de proteinas que se repiten en distintos genomas y que por tanto eso hace que en elarchivo temporal aparezcan mas `grep -E "[0-9]+:" temp.temp | wc -l`: 68186 y `grep -E "^[0-9]+" /mnt/c/Users/52477/Desktop/Descargas_NCBI/CDHIT/MATRIXDATA/filtclusterprotcatALL2000.clstr | wc -l`: 56287 y por otro se tienen 56292 del archivo `wc -l 200424_grepfaa.txt`

```
sort temp.temp | uniq -c
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/faba1b7b-b772-458e-b37e-687b16f7ce62)

El primer numero describe cuantas veces aparece

Asi buscamos los que se repitan y los contamos
```
sort temp.temp | uniq -c | grep -E "2\s" | wc -l
```
aparecen 11897, por lo que en la busqueda sihay valores repetidos

ahora veremos como es que resulta en el archivo filtrado
```
sort filtclusterprotcatALL2000.clstr | uniq -c | grep -E "2\s" | wc -l
```
No hay duplicados, por tanto tiene que ver con la busqueda que haga linea por linea.
