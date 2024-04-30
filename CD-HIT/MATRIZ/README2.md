# 20 de abril del 2024
Ahora se vera como desarrollar el script para que corrar mas rapido el analisis y no tenga que estar abriendo los archivos a cada rato y haviendo busquedas tan largas

1. Para ello se piensa crear una tabla con todas las accesiones y que desdes ahi haga la busqueda
2. sustituir sed por otra funcion

```
#!/bin/bash

DIR="direccion/Desktop/Descargas_NCBI"
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

GENOMES="direccion/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="direccion/Descargas_NCBI/CDHIT/MATRIXDATA"

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

echo "while read con grep para busqueda en un segundo archivo inicio a las $io y termino a las $f"
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

GENOMES="Direccion/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="Direccion/Descargas_NCBI/CDHIT/MATRIXDATA"
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

GENOMES="Direccion/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="Direccion/Descargas_NCBI/CDHIT/MATRIXDATA"
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

Al parecer hay id's de proteinas que se repiten en distintos genomas y que por tanto eso hace que en elarchivo temporal aparezcan mas `grep -E "[0-9]+:" temp.temp | wc -l`: 68186 y `grep -E "^[0-9]+" Direccion/Descargas_NCBI/CDHIT/MATRIXDATA/filtclusterprotcatALL2000.clstr | wc -l`: 56287 y por otro se tienen 56292 del archivo `wc -l 200424_grepfaa.txt`

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

Asi si buscamos en el archivo de busqueda `200424_grepfaa.txt` solo se repite un id de uns proteina dos veces y las demas son unicas
```
sort 200424_grepfaa.txt | uniq -c | grep -E "1\s" | wc -l
```
con 56290 y 
```
sort 200424_grepfaa.txt | uniq -c | grep -E "2\s" | wc -l
```
con 1, por tanto no puede ser los archivos de referencia, es mas por el comando y el tipo de busqueda que ofrece. ahora cambiamos el while por un for para intentar
```
#!/bin/bash

GENOMES="Dir/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="Dir/Descargas_NCBI/CDHIT/MATRIXDATA"
rm temp.temp
io=$(date +%H:%M:%S)
for i in $(cat "$WORK/filtclusterprotcatALL2000.clstr")
do
        if [[ "$i" =~ "Cluster" ]]
        then
                echo "$i" >> temp.temp
        else
                awk -v pattern="$i" '$0 ~ pattern' "$WORK/200424_grepfaa.txt" | grep -E "^[0-9]+" >> temp.temp
        fi
done
f=$(date +%H:%M:%S)

echo "for con awk para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las $io y termino a las $f"
```

```
for con awk para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las 15:03:56 y termino a las 15:55:04
real    51m8.429s
user    17m37.156s
sys     40m10.250s
```
Ahora lo intentamos con tan solo el awk sin condicionales
```
#!/bin/bash

GENOMES="Direccion/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="Direccion/Descargas_NCBI/CDHIT/MATRIXDATA"
rm temp2.temp
io=$(date +%H:%M:%S)
while read linea
do
        awk -v pattern="$linea" '$0 ~ pattern' "$WORK/200424_grepfaa.txt" >> temp2.temp
done < "$WORK/filtclusterprotcatALL2000.clstr"
f=$(date +%H:%M:%S)

echo "while read con awk para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las $io y termino a las $f"
```
Resultado con tan solo 68186 lineas quitando los 19000 lineas de los nombres de cluster.
```
while read con awk para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las 16:10:57 y termino a las 17:14:19

real    63m21.833s
user    23m4.578s
sys     33m45.156s
```
Retrocedemos al script anterior del inicio con grep para ver si es porque el rendiemiento de la computadora bajo o si es el script mas lento
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
SALIDA
```
while read con grep para busqueda en un segundo archivo inicio a las 17:37:16 y termino a las 18:14:28

real    52m55.334s
user    2m9.438s
sys     24m18.469s
```
Al parecer si la computadora se realientizo
# Fecha 22 de abril del 2024
El dia de hoy se hara una pequeña modificacion, para ver como actua la busqueda de las accessiones, eliminandolas del archivo `filtclusterprotcatALL2000.clstr` y contandolas, asi como ver que puede hacerse para major crear una tabla o hacer otro filtro para las busquedas y no suceda que con los originales encuentre mas de dos y sea un caos con la conformaicon de la matriz

Ahora modificamos el formato con este script
```
#!/bin/bash

GENOMES="Dir/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="Dir/Descargas_NCBI/CDHIT/MATRIXDATA"
rm /TEMPSALIDA/temp4.temp
filtdata_file=$(cat "$WORK/filtclusterprotcatALL2000.clstr")

io=$(date +%H:%M:%S)
echo $filtdata_file | sed 's/\sCluster/\nCluster/g' | while IFS= read -r linea
do
        n=$(echo "$linea" | grep -E -o "Cluster[0-9]+" | grep -E -o "[0-9]+")
        echo "$linea" | sed -E "s/\s/ Cluster$n:/g" | sed -E 's/(Cluster[0-9]+ )//g' | sed -E 's/\s/\n/g'
done
f=$(date +%H:%M:%S)

echo "while con grep para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las $io y termino a las $f"
```
Con salida

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/c461ba51-98a0-4d1f-8679-0c0edf557f65)

Y esto para ello  ahora usaremos solo las accesiones para hacer la busqeuda, elimindo las lineas que tienen cluster y el numero, asi evitamos que pueda ser que se ocupen los numero de esas lineas y se pueda continuar trabajando.
Este es el script final con nombre `./temporalmat.sh`
```
#!/bin/bash

GENOMES="Dir/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="Dir/Descargas_NCBI/CDHIT/MATRIXDATA"
rm "$WORK/filtclstr_a_tempseek.txt"
filtdata_file=$(cat "$WORK/filtclusterprotcatALL2000.clstr")

io=$(date +%H:%M:%S)
echo $filtdata_file | sed 's/\sCluster/\nCluster/g' | while IFS= read -r linea
do
        n=$(echo "$linea" | grep -E -o "Cluster[0-9]+" | grep -E -o "[0-9]+")
        echo "$linea" | sed -E "s/\s/ Cluster$n:/g" | sed -E 's/(Cluster[0-9]+ )//g' | sed -E 's/\s/\n/g' >> "$WORK/filtclstr_a_tempseek.txt"
done
f=$(date +%H:%M:%S)

echo "while con grep para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las $io y termino a las $f"
```

tiempo de 22 minutos
```
while con grep para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las 08:46:27 y termino a las 09:08:24
```
la salida del archivo que se va usar para hacer las busquedas se va a llamar `filtclstr_a_tempseek.txt` y con ello procedemos a hacer las busquedas y comparaciones para concatenar la informacion.
Ahora se tardo 19 minutos en correr la busqueda dentro de `200424_grepfaa.txt`
```
#!/bin/bash

GENOMES="Direccion/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="Direccion/Descargas_NCBI/CDHIT/MATRIXDATA"

rm "$WORK/temporal.txt"

io=$(date +%H:%M:%S)
awk -F ":" '{print $2}' "$WORK/filtclstr_a_tempseek.txt" | while read linea
do
        echo "$linea"
        grep "$linea" "$WORK/200424_grepfaa.txt" >> "$WORK/temporal.txt"
done
f=$(date +%H:%M:%S)

echo "while read con grep para busqueda en un segundo archivo inicio a las $io y termino a las $f"


while read con grep para busqueda en un segundo archivo inicio a las 09:54:40 y termino a las 10:13:33
```

```
#!/bin/bash

GENOMES="Direccion/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="Dir/Descargas_NCBI/CDHIT/MATRIXDATA"

rm "$WORK/temporalconca.txt"

io=$(date +%H:%M:%S)

var_comparacion=""
idproteinas=$(cat "$WORK/filtclstr_a_tempseek.txt")
echo "$idproteinas" | while read linea
do
        busca=$(echo "$linea" |  awk -F ":" '{print $2}')
        resulta=$(grep -E ":$busca" "$WORK/200424_grepfaa.txt")
        echo -e "$linea\t$resulta"
        var_comparacion="$var_comparacion\n$linea\t$resulta"
        # echo -e "$var_comparacion"
done
echo -e "$var_comparacion" >> "$WORK/temporalconca.txt"
f=$(date +%H:%M:%S)

echo "while read con grep para busqueda en un segundo archivo inicio a las $io y termino a las $f"
```
No funciono este script por que no guardo nada en el archivo
pero se corrigio con este `tmat.sh`
```
#!/bin/bash

GENOMES="DIR/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="DIR/Descargas_NCBI/CDHIT/MATRIXDATA"
rm "$WORK/temporalconca.txt"

io=$(date +%H:%M:%S)
idproteinas=$(cat "$WORK/filtclstr_a_tempseek.txt")
echo "$idproteinas" | while read linea
do
        busca=$(echo "$linea" |  awk -F ":" '{print $2}')
        resulta=$(grep -E ":$busca" "$WORK/200424_grepfaa.txt")
        echo -e "$linea\t$resulta"
        echo -e "$linea\t$resulta" >> "$WORK/temporalconca.txt"
done
f=$(date +%H:%M:%S)

echo "while read con grep para busqueda en un segundo archivo inicio a las $io y termino a las $f"
```
y tiene un total de lineas de 56287 y ninguno se repite, ahora no se. ya se me rompio la chompa como es que ahora si funciona :C

# 23 de abril del 2024
Hoy se vera si ningun dato se repite y to funciona correctamente. Para saber si asi hacer que el codigo corra y solo optimizar la busqueda para que no sea tan lento porque se tardo como 1hr `tmat.sh`

Se quiere crear un script llamado `comp.sh`, pero antes, tenemos los resultados de como funcionaba antes el script y salian los duplicados, salida `temp3.temp`, con esto se vera cuales son los datos duplicados con respecto al que si salio bien, salida `temporalconca.txt`. Y con las accesiones de los duplicados se extraeran del archivo que salen bien. para buscar las diferencias. Los genoams que se duplican y se sacaron de `temporalconca.txt` se guardaran en un archivo llamado `extracciontemporalconca.txt`

Asi por otra parte al buscar en los duplicados, tomamos de ejemplo la proteina `2972001969` y por ejemplo podemos ver que 
```
grep "2972001969" temp3.temp
```
que resulto en 

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/c2e8e6a1-e64b-4857-b41f-cf0025e97f4b)

Y por otra parte en la busqueda
```
grep "2972001969" temporalconca.txt
```
resulta en 

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/8950dee1-8641-4298-869d-5d17934d7b07)

Y por tanto, ¿que puede hacer que la busqueda del codigo anterior pueda hacer que se duplique?
para ello lo que haremos es recurrir al script que hizo la busqueda y duplico algunos y en si al archivo original y ver si hay algo que haga que se duplique.

Bien, de la accesion anterior se busco
```
grep -E "2972001969" 200424_grepfaa.txt
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/c1dc3b7b-2ddb-416d-b1d8-256ba2249014)

```
grep "2972001969" temporalconca.txt
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/2d8864c6-59c8-4fde-990c-c89af9f2b78d)

```
grep "2972001969" 200424_grepfaa.txt
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/bb782db6-8a59-4bcd-aadc-e143b6789865)

```
grep "2972001969" filtclstr_a_tempseek.txt
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/81721645-2a54-455b-863f-e1875513c09d)

```
grep "2972001969" filtclusterprotcatALL2000.clstr
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/bf09edcd-a951-4a2b-be63-0019a8f1cfb7)

```
grep -E ":2972001969" 200424_grepfaa.txt
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/9e458fae-f247-43b7-98ed-cd342b049330)

Finalmente se vio que pasara si se busca la misma accession del genoma como del de la proteina
```
grep -E ":2972001829" 200424_grepfaa.txt
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/eda3dc29-3a04-417b-8fde-b5083d525e6a)

Algo que evidentemente sin la restriccion de las `:` busca todo aquello que tenga el id del genoma que tambien es de al proteina y que por tanto se duplique
```
grep -E "2972001829" 200424_grepfaa.txt
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/3aad210d-43f3-467c-92b2-a049b89248bd)

Con esta premisa, lo unique que se va a hacer es modificar el script mas rapido y se añade lo de cluster para finalmente aplicar un comando para juntar genomas con cluster y asi hacer el conteo: nombre del archivo `ClusterGenome.sh`.
```
#!/bin/bash

GENOMES="Direccion/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="Dirección/Descargas_NCBI/CDHIT/MATRIXDATA"

io=$(date +%H:%M:%S)
time {
rm "$WORK/clugen.txt"
while read linea
do
        busca=$(echo "$linea" |  awk -F ":" '{print $2}')
        resulta=$(grep ":$busca" "$WORK/200424_grepfaa.txt")
        echo -e "$linea\t$resulta" >> "$WORK/clugen.txt"
done < "$WORK/filtclstr_a_tempseek.txt"
}
f=$(date +%H:%M:%S)

echo "while read con grep para busqueda en un segundo archivo inicio a las $io y termino a las $f"
```
Con salida
```
rm: cannot remove 'DIR/Descargas_NCBI/CDHIT/MATRIXDATA/clugen.txt': No such file or directory

real    40m49.257s
user    2m16.047s
sys     32m10.234s
while read con grep para busqueda en un segundo archivo inicio a las 10:16:13 y termino a las 10:57:02
```
Solo se pensaria en usar un comando para que cuente todo aquello que se repita y empezar a contar todos
## 24 de abril del 2024
---------------------------------------------------------------------------------------------------------------------
Conjuncion del script
```
#!/bin/bash
# Buscamos la salida en formato idgenoma:idproteina de las fuentes originales
grep -E -o "^>[0-9]+" */*faa | awk -F "/[0-9]+.genes.faa:>" '{print $1 ":" $2}' > ../CDHIT/MATRIXDATA/200424_grepfaa.txt

# Por aca solo obtenemos las accesiones del analisis en CD-HIT
awk -F ">" '{print $2}' clusterprotcatALL2000.clstr | awk -F "." '{print $1}' > ../MATRIXDATA/filtclusterprotcatALL2000.clstr

# Mantiene el formato Cluster[0-9]+
awk '{gsub(/\s/, "", $0); print}' filtclusterprotcatALL2000.clstr > tmp.tmp && mv tmp.tmp filtclusterprotcatALL2000.clstr

# Con esto hacemos el formato de Cluster[0-9]+:idproteina
GENOMES="Dir/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="Dir/Descargas_NCBI/CDHIT/MATRIXDATA"
rm "$WORK/filtclstr_a_tempseek.txt"
filtdata_file=$(cat "$WORK/filtclusterprotcatALL2000.clstr")

io=$(date +%H:%M:%S)
echo $filtdata_file | sed 's/\sCluster/\nCluster/g' | while IFS= read -r linea
do
        n=$(echo "$linea" | grep -E -o "Cluster[0-9]+" | grep -E -o "[0-9]+")
        echo "$linea" | sed -E "s/\s/ Cluster$n:/g" | sed -E 's/(Cluster[0-9]+ )//g' | sed -E 's/\s/\n/g' >> "$WORK/filtclstr_a_tempseek.txt"
done
f=$(date +%H:%M:%S)

echo "while con grep para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las $io y termino a las $f"



```
--------------------------------------------------------------------------------------------------------------------

Antes de ello pensaba modificar la busqueda a que si se tienen los formatos `idgenomas:idproteina` en el arhivo `200424_grepfaa.txt` y `Cluster[0-9]+:idproteina` del archivo `filtclstr_a_tempseek.txt`.
Eliminar aquellos `idgenomas:idproteina` que no se encuentren con la `idproteina` en `filtclstr_a_tempseek.txt` y despues ordenarlos por `idproteina`.

ANTES UNA PRUEBA, CONCATENAMOS `200424_grepfaa.txt` Y `filtclstr_a_tempseek.txt` PARA HACER UNA BUSQUEDA POR COINCIDENCIA CON GREP, NUEVO ARCHIVO `grepfaa_filtclstr.txt`
```
paste 200424_grepfaa.txt filtclstr_a_tempseek.txt > grepfaa_filtclstr.txt
```
primero los ordenamos
```
awk -F ":" '{print $2 ":" $1}' filtclstr_a_tempseek.txt | sort -n | awk -F ":" '{print $2":"$1}'
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/bd234471-a00b-4f8f-98bc-3e0417eb9711)
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/be3ff70d-22f1-4d53-8e75-54d92d1f5ae9)

```
awk -F ":" '{print $2 ":" $1}' 200424_grepfaa.txt | sort -n | awk -F ":" '{print $2":"$1}'
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/73fd2c59-8ae0-4f71-ab54-9084b6f10a6c)

los gurdamos y finalmente los concatenamos
```
awk -F ":" '{print $2 ":" $1}' filtclstr_a_tempseek.txt | sort -n | awk -F ":" '{print $2":"$1}' > temp && mv temp filtclstr_a_tempseek.txt
awk -F ":" '{print $2 ":" $1}' 200424_grepfaa.txt | sort -n | awk -F ":" '{print $2":"$1}' > temp && mv temp 200424_grepfaa.txt
```
tenemos tamaños numeros de lineas respectivas de `filtclstr_a_tempseek.txt`:56287  y `200424_grepfaa.txt`:56292. Son 5 accesiones que no estan en `filt...` para ello hay que ver si hay alguna opcion en `CDHIT` arroje los que no fueron incluidos en los resultados.

# SOLO COMANDO PRUEBA BASH A PYTHON Y PYTHON A BASH
## 27 de abril del 2024
Por esta parte se buscar como usar codigo en pyhton dentro de un script de bash y asi generar la matriz
```
#!/bin/bash
echo "hola en bash"
# Guardamos una variable aca para ver si funciona
saludo="Que tal! es un gusto saludar, quiero saber si se puede comunicar bash con python"
export saludo
python3 << END
#Codigo python
import os
saludo=os.environ['saludo']
print("hola en python")
print(saludo)
END
```
AHORA QUE COMPROBAMOS EL FUNCIONAMIENTO DE LOS COMANDOS, E INSTALAR LAS LIBRERIAS "NUMPY" Y "´PANDAS". CONSEGUIMOS LA SALIDA
```
#!/bin/bash
echo "hola en bash"
# Guardamos una variable aca para ver si funciona
saludo="Que tal! es un gusto saludar, quiero saber si se puede comunicar bash con python"
export saludo
python3 << END
#Codigo python
import os
saludo=os.environ['saludo']
print("hola en python")
print(saludo)

# Con este saludo, ahora busco generar una matriz en una variable
#veamos con una pequeña
import numpy as np

# Quiero crar una matriz por default con 0's
matriz_ceros = np.zeros((4, 5))
print("matriz")
print(matriz_ceros)

#Por esta parte crearemos un dataframe basico para saber como actua
import pandas as pd

# Suponiendo que queremos un data el cual tienen variables y se quieren añadir
# nombres de las columnas
columnas = ['col1', 'col2', 'col3']
filas = ['1', '2']
marcolectura = pd.DataFrame(0, index=filas, columns=columnas)
print("Dataframe")
print(marcolectura)
END

echo "me despido ahora estoy en bash de nuevo"
```
Con salida

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/8ac81850-9045-492f-a3da-10b51bac061c)


Como no se puede usar una variable python en bash de regreso, mejor la salida de la matriz, la guardo en un archivo y de ahi trabajo con bash
```
#!/bin/bash
echo "hola en bash"
# Guardamos una variable aca para ver si funciona
saludo="Que tal! es un gusto saludar, quiero saber si se puede comunicar bash con python"
export saludo
python3 << END
#Codigo python
import os
saludo=os.environ['saludo']
print("hola en python")
print(saludo)

# Con este saludo, ahora busco generar una matriz en una variable
#veamos con una pequeña
import numpy as np

# Quiero crar una matriz por default con 0's
matriz_ceros = np.zeros((4, 5))
print("matriz")
print(matriz_ceros)

#Por esta parte crearemos un dataframe basico para saber como actua
import pandas as pd

# Suponiendo que queremos un data el cual tienen variables y se quieren añadir
# nombres de las columnas
columnas = ['col1', 'col2', 'col3']
filas = ['1', '2']
marcolectura = pd.DataFrame(0, index=filas, columns=columnas)
print("Dataframe")
print(marcolectura)

#FINALMENTE PARA HACER QUE SE PUEDA EXPORTAR UNA VARIABLE DE PYTHON A BASH HACEMOS
os.environ["DtFr_PYTHONaBASH"] = marcolectura
END

echo "me despido ahora estoy en bash de nuevo" 
echo "EXPORTAMOS EL DATAFRAME PARA USARLA EN BASH, LA CUAL SE NOMBRO COMO DtFr_PYTHONaBASH: $DtFr_PYTHONaBASH"
```
Salida

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/608c3f11-a2f7-48b8-8349-cc765f7a28fe)

# ADAPTAMOS PYTHON EN BASH
```
#!/bin/bash
echo "INICIO PARA FORMAR LAS MATRICES BASH"
DIRMATRIZ="dir/Descargas_NCBI/CDHIT/MATRIXDATA"
cols=$(grep "Clu" $DIRMATRIZ/filtclusterprotcatALL2000.clstr)
export cols
python3 << END
#Codigo python
import os
import pandas as pd

print("Nos encontramos en PYTHON")

# Imprimimos cols que tiene todos los numeros de cluster para saber en que formato trabaja
print(cols)
END

echo "Terminos, ahora estamos en BASH" 
```
Salida

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/8b910fc4-39ff-4946-a7e6-b5767544294c)

Con el codigo avanzado de script de python pidemos proceder a hacer la matriz y el conteo
```
#!/bin/bash
echo "INICIO PARA FORMAR LAS MATRICES BASH"
DIRMATRIZ="DIR/Descargas_NCBI/CDHIT/MATRIXDATA"
GENOMES="DIR/Descargas_NCBI/IMGPSEUDOMONASGENOMES"

paste $DIRMATRIZ/200424_grepfaa.txt $DIRMATRIZ/filtclstr_a_tempseek.txt > $DIRMATRIZ/grepfaa_filtclstr.txt

cols=$(grep "Clu" $DIRMATRIZ/filtclusterprotcatALL2000.clstr)
echo $cols > "$DIRMATRIZ/shtopy_Clust.txt"

filas=$(ls $GENOMES | tr '\n' ' ')
echo -e "$filas" > "$DIRMATRIZ/shtopy_genomes.txt"
python3 - << END
#Codigo python
import os
import pandas as pd
import sys

print("Nos encontramos en PYTHON")

# Imprimimos cols que tiene todos los numeros de cluster para saber en que formato trabaja
with open('DIR/Descargas_NCBI/CDHIT/MATRIXDATA/shtopy_Clust.txt', 'r') as Clus:
    cols = Clus.read().strip()
    cols = cols.split(' ')

with open('DIR/Descargas_NCBI/CDHIT/MATRIXDATA/shtopy_genomes.txt', 'r') as fila:
    fl = fila.read().strip()
    fl = fl.split(' ')
print(cols)
print(fl)

# Hacemos el dataframe
zerocdhit = pd.DataFrame(0, index=fl, columns=cols)
print(zerocdhit)
END

echo "Terminos, ahora estamos en BASH" 
```
Con salida

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/8214a4a5-49a3-4fc3-9712-1720c5aceabc)

Y con el archivo de salida `grepfaa_filtclstr.txt`. Asi podemos considerar el comando para unir estos y usarlos para la matriz en la busqueda con python
Con este comando
```
awk -F ":" '{print $1 ":" $2}' grepfaa_filtclstr.txt > temp.txt
```
Tiene una salida asi

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/e2116708-def7-494e-9efb-cc758ceb806e)

En cambio el comando asi
```
awk -F ":" '{print $2 ":" $1}' grepfaa_filtclstr.txt > temp.txt
```
Salida

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/f7a658a6-b4e7-444c-9632-fae043cee023)

Confirmando que todo esta en orden
A lo cual con una pequeña modificacion aplicamos
```
awk -F ":" '{print $2 ":" $1}' grepfaa_filtclstr.txt | cut -f 2 > temp.txt
```
Salida

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/9dfda655-a626-4d81-9257-37d8825bf8f0)

Ademas con este comando sale cuantos salen 
```
awk -F ":" '{print $2 ":" $1}' grepfaa_filtclstr.txt | cut -f 2 | uniq -c > temp.txt
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/b950ff88-8d56-4a66-8fa9-586aa09cdfbb)

Y podemos aplicar otro comando mas para que quede en orden y solo sea usar un for y obtenga cada llamado y lo ponga como output
```
awk -F ":" '{print $2 ":" $1}' grepfaa_filtclstr.txt | cut -f 2 | uniq -c | awk -F " " '{print $2 ":" $1}'
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/f8a7134f-6374-4736-b5c4-1439796d196c)

Asi lo guardamos
```
awk -F ":" '{print $2 ":" $1}' grepfaa_filtclstr.txt | cut -f 2 | uniq -c | awk -F " " '{print $2 ":" $1}' > inputmatrizcdhit.mtcdhit
```

Aqui terminamos el script funcionando y arrojando la matriz
```
#!/bin/bash
echo "INICIO PARA FORMAR LAS MATRICES BASH"
DIRMATRIZ="Dir/Descargas_NCBI/CDHIT/MATRIXDATA"
GENOMES="Dir/Descargas_NCBI/IMGPSEUDOMONASGENOMES"

paste $DIRMATRIZ/200424_grepfaa.txt $DIRMATRIZ/filtclstr_a_tempseek.txt > $DIRMATRIZ/grepfaa_filtclstr.txt

cols=$(grep "Clu" $DIRMATRIZ/filtclusterprotcatALL2000.clstr)
echo $cols > "$DIRMATRIZ/shtopy_Clust.txt"

filas=$(ls $GENOMES | tr '\n' ' ')
echo -e "$filas" > "$DIRMATRIZ/shtopy_genomes.txt"
python3 - << END
#Codigo python
import os
import pandas as pd
import sys

print("Nos encontramos en PYTHON")

# Imprimimos cols que tiene todos los numeros de cluster para saber en que formato trabaja
with open('Dir/Descargas_NCBI/CDHIT/MATRIXDATA/shtopy_Clust.txt', 'r') as Clus:
    cols = Clus.read().strip()
    cols = cols.split(' ')

with open('Dir/Descargas_NCBI/CDHIT/MATRIXDATA/shtopy_genomes.txt', 'r') as fila:
    fl = fila.read().strip()
    fl = fl.split(' ')
#print(cols)
#print(fl)

# Hacemos el dataframe
zerocdhit = pd.DataFrame(0, index=fl, columns=cols)
#print(zerocdhit)

with open('Dir/Descargas_NCBI/CDHIT/MATRIXDATA/inputmatrizcdhit.mtcdhit', 'r') as entrada:
    input = entrada.read().strip()
    input = input.split('\n')
#print(input)
#print(len(input))
#print(type(input))

n = 0
while n < len(input):
    #print("hola", input[n])
    subconjunto = input[n].split(":")
    #print(subconjunto)
    #print(subconjunto[1], subconjunto[0], subconjunto[2])

    # Ahora si la entrada de los datos para formar la matriz
    zerocdhit.at[ subconjunto[1], subconjunto[0] ] = subconjunto[2]
    n+=1

# Lo guardamos
zerocdhit.to_csv('Dir/Descargas_NCBI/CDHIT/MATRIXDATA/pymatrizcdhit.csv', index=True)

END

echo "Terminos, ahora estamos en BASH" 
```

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/0b6a50f6-45cb-40e5-a210-ae5a6513b212)

Pero no coincide el numero de proteinas por cluster contadas anteriormente, si recordamos las contadas a mano no coinciden con la salida
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

hora buscamos por `Cluster1`, para ver como hacer el conteo con `uniq -c`
```
grep -E "^Cluster1:" inputmatrizcdhit.mtcdhit
```
salida

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/b8a3e7ee-4194-4f45-b43f-d335451d1c45)

usamos este comando para modificar
```
awk -F ":" '{print $2 ":" $1}' grepfaa_filtclstr.txt | cut -f 2 | sort | uniq -c | awk -F " " '{print $2 ":" $1}' | wc -l
53907
```
Y como salia antes
```
awk -F ":" '{print $2 ":" $1}' grepfaa_filtclstr.txt | cut -f 2 | uniq -c | awk -F " " '{print $2 ":" $1}' | wc -l
55924
```
con la modificacion en el archivo vemos que sucede

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/6b13f261-3a27-41ea-9974-e3e3e5c3c89b)

En efecto el sort si ayuda a tener la correccion y funciona muy bien.
Solo otro detalle con la salida del archivo, no aparecen las accesiones, se puede simplemente agregar un nombre a ala columna donde van las accesiones o solo eliminar la opcion de index, que si la eliminamos solo obtenemos esta matriz.

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/85ec7783-1738-49ff-a5e7-04c775a78750)

# 28 de abril del 2024
finalmente. agregamos todo el codigo para que pueda ser entendido y funcional
```
#!/bin/bash
# Buscamos la salida en formato idgenoma:idproteina de las fuentes originales
grep -E -o "^>[0-9]+" */*faa | awk -F "/[0-9]+.genes.faa:>" '{print $1 ":" $2}' > ../CDHIT/MATRIXDATA/200424_grepfaa.txt

# Por aca solo obtenemos las accesiones del analisis en CD-HIT
awk -F ">" '{print $2}' clusterprotcatALL2000.clstr | awk -F "." '{print $1}' > ../MATRIXDATA/filtclusterprotcatALL2000.clstr

# Mantiene el formato Cluster[0-9]+
awk '{gsub(/\s/, "", $0); print}' filtclusterprotcatALL2000.clstr > tmp.tmp && mv tmp.tmp filtclusterprotcatALL2000.clstr

# Con esto hacemos el formato de Cluster[0-9]+:idproteina
GENOMES="Dir/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
WORK="Dir/Descargas_NCBI/CDHIT/MATRIXDATA"
rm "$WORK/filtclstr_a_tempseek.txt"
filtdata_file=$(cat "$WORK/filtclusterprotcatALL2000.clstr")

io=$(date +%H:%M:%S)
echo $filtdata_file | sed 's/\sCluster/\nCluster/g' | while IFS= read -r linea
do
        n=$(echo "$linea" | grep -E -o "Cluster[0-9]+" | grep -E -o "[0-9]+")
        echo "$linea" | sed -E "s/\s/ Cluster$n:/g" | sed -E 's/(Cluster[0-9]+ )//g' | sed -E 's/\s/\n/g' >> "$WORK/filtclstr_a_tempseek.txt"
done
f=$(date +%H:%M:%S)

echo "while con grep para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las $io y termino a las $f"

awk -F ":" '{print $2 ":" $1}' grepfaa_filtclstr.txt | cut -f 2 | sort | uniq -c | awk -F " " '{print $2 ":" $1}' > inputmatrizcdhit.mtcdhit

#!/bin/bash
echo "INICIO PARA FORMAR LAS MATRICES BASH"
DIRMATRIZ="DIR/Descargas_NCBI/CDHIT/MATRIXDATA"
GENOMES="DIR/Descargas_NCBI/IMGPSEUDOMONASGENOMES"

paste $DIRMATRIZ/200424_grepfaa.txt $DIRMATRIZ/filtclstr_a_tempseek.txt > $DIRMATRIZ/grepfaa_filtclstr.txt

cols=$(grep "Clu" $DIRMATRIZ/filtclusterprotcatALL2000.clstr)
echo $cols > "$DIRMATRIZ/shtopy_Clust.txt"

filas=$(ls $GENOMES | tr '\n' ' ')
echo -e "$filas" > "$DIRMATRIZ/shtopy_genomes.txt"
python3 - << END
#Codigo python
import os
import pandas as pd
import sys

print("Nos encontramos en PYTHON")

# Imprimimos cols que tiene todos los numeros de cluster para saber en que formato trabaja
with open('DIR/Descargas_NCBI/CDHIT/MATRIXDATA/shtopy_Clust.txt', 'r') as Clus:
    cols = Clus.read().strip()
    cols = cols.split(' ')

with open('DIR/Descargas_NCBI/CDHIT/MATRIXDATA/shtopy_genomes.txt', 'r') as fila:
    fl = fila.read().strip()
    fl = fl.split(' ')
#print(cols)
#print(fl)

# Hacemos el dataframe
zerocdhit = pd.DataFrame(0, index=fl, columns=cols)
#print(zerocdhit)

with open('DIR/Descargas_NCBI/CDHIT/MATRIXDATA/inputmatrizcdhit.mtcdhit', 'r') as entrada:
    input = entrada.read().strip()
    input = input.split('\n')
#print(input)
#print(len(input))
#print(type(input))

n = 0
while n < len(input):
    #print("hola", input[n])
    subconjunto = input[n].split(":")
    #print(subconjunto)
    #print(subconjunto[1], subconjunto[0], subconjunto[2])

    # Ahora si la entrada de los datos para formar la matriz
    zerocdhit.at[ subconjunto[1], subconjunto[0] ] = subconjunto[2]
    n+=1

# Lo guardamos
zerocdhit.to_csv('DIR/Descargas_NCBI/CDHIT/MATRIXDATA/pymatrizcdhit.csv')

END

echo "Terminos, ahora estamos en BASH" 
```


Codigo con correcciones en las rutas des escritorios y el orden de operacion del codigo
```
#!/bin/bash
io=$(date +%H:%M:%S)
time{
echo "INICIO PARA FORMAR LAS MATRICES BASH"
DIRMATRIZ="DIR/Descargas_NCBI/CDHIT/MATRIXDATA"
GENOMES="DIR/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
OUTCDHIT="DIR/Descargas_NCBI/CDHIT/TODOS"

# Buscamos la salida en formato idgenoma:idproteina de las fuentes originales para concatenarlos en un solo archivo.
grep -E -o "^>[0-9]+" $GENOMES/*/*faa | awk -F "/[0-9]+.genes.faa:>" '{print $1 ":" $2}' > $DIRMATRIZ/200424_grepfaa.txt

# Por aca solo obtenemos las accesiones del analisis en CD-HIT
awk -F ">" '{print $2}' $OUTCDHIT/clusterprotcatALL2000.clstr | awk -F "." '{print $1}' > $DIRMATRIZ/filtclusterprotcatALL2000.clstr

# Mantiene el formato, pero cambiamos de "Cluster [0-9]+" a "Cluster[0-9]+" del filtrado de la salida de "CDHIT"
awk '{gsub(/\s/, "", $0); print}' $DIRMATRIZ/filtclusterprotcatALL2000.clstr > $DIRMATRIZ/tmp.tmp && mv $DIRMATRIZ/tmp.tmp $DIRMATRIZ/filtclusterprotcatALL2000.clstr

# Con esto hacemos el formato de Cluster[0-9]+:idproteina
rm "$DIRMATRIZ/filtclstr_a_tempseek.txt"
filtdata_file=$(cat "$DIRMATRIZ/filtclusterprotcatALL2000.clstr")
echo $filtdata_file | sed 's/\sCluster/\nCluster/g' | while IFS= read -r linea
do
        n=$(echo "$linea" | grep -E -o "Cluster[0-9]+" | grep -E -o "[0-9]+")
        echo "$linea" | sed -E "s/\s/ Cluster$n:/g" | sed -E 's/(Cluster[0-9]+ )//g' | sed -E 's/\s/\n/g' >> "$DIRMATRIZ/filtclstr_a_tempseek.txt"
done

# Despues de concatenar en "200424_grepfaa.txt" en formato "idgenoma:idproteina" y en "filtclstr_a_tempseek.txt" en formato "Cluster[0-9]+:idproteina"
# Simplemente pasamos a juntarlos "idgenoma:idproteina" y "Cluster[0-9]+:idproteina"
paste $DIRMATRIZ/200424_grepfaa.txt $DIRMATRIZ/filtclstr_a_tempseek.txt > $DIRMATRIZ/grepfaa_filtclstr.txt

# Para este ultimo lo pasamos a formato "Cluster[0-9]+:idgenoma:No.Repeticiones" (importante sort y despues uniq -c en ese orden)
awk -F ":" '{print $2 ":" $1}' $DIRMATRIZ/grepfaa_filtclstr.txt | cut -f 2 | sort | uniq -c | awk -F " " '{print $2 ":" $1}' > $DIRMATRIZ/inputmatrizcdhit.mtcdhit

# Antes creamos unas variables para introducirlas a codigo en PYTHON
# extraemos todos los Cluster[0-9]+
cols=$(grep "Cluster" $DIRMATRIZ/filtclusterprotcatALL2000.clstr)
echo $cols > "$DIRMATRIZ/shtopy_Clust.txt"

# Extraemos todos los genomas que fueron usados.
filas=$(ls $GENOMES | tr '\n' ' ')
echo -e "$filas" > "$DIRMATRIZ/shtopy_genomes.txt"

python3 - << END
#Codigo python
import os
import pandas as pd
import sys
print("Nos encontramos en PYTHON")

# Imprimimos cols que tiene todos los numeros de cluster para saber en que formato trabaja
with open('DIR/Descargas_NCBI/CDHIT/MATRIXDATA/shtopy_Clust.txt', 'r') as Clus:  # Se guarda en una variable Clus
    cols = Clus.read().strip()                                                                          # Los datos los guarda con otro tipo de variable para trabajar
    cols = cols.split(' ')                                                                              # Quita los espacios para convertir el set de Cluster en una lista gigante

# Llamamos el archivo con las accesiones de los genomas.
with open('DIR/Descargas_NCBI/CDHIT/MATRIXDATA/shtopy_genomes.txt', 'r') as fila:    # Se guarda en una variable fila
    fl = fila.read().strip()                                                                                # Los datos los guarda con otro tipo de variable para trabajar
    fl = fl.split(' ')                                                                                      # Quita los espacios para convertir el set de genomas en una lista

# Hacemos el dataframe lleno de ceros.
zerocdhit = pd.DataFrame(0, index=fl, columns=cols)

# Llamamos al archivo de entrada con formato "Cluster[0-9]+:idgenoma:No.Repeticiones" para generar el conteo y guardarlo en la matriz.
with open('DIR/Descargas_NCBI/CDHIT/MATRIXDATA/inputmatrizcdhit.mtcdhit', 'r') as entrada:   # Se guarda en una variable entrada
    input = entrada.read().strip()                                                                                  # Los datos los guarda con otro tipo de variable para trabajar
    input = input.split('\n')                                                                                       # Quita los espacios para convertir el set de entrada en una lista gigante

# Comienza el conteo desde 0, para hacer el llamado del dato inicial
n = 0
while n < len(input):
    subconjunto = input[n].split(":")                                   # Como hace el llamado por linea, quita ":" para crear micro listas
    # Ahora si la entrada de los datos para formar la matriz
    zerocdhit.at[ subconjunto[1], subconjunto[0] ] = subconjunto[2]     # Ahora con las microlistas, con
                                                                        # subconjunto[1] nombra la accesion genoma, 
                                                                        # subconjunto[0] llama Cluster y 
                                                                        # subconjunto[2] en esa interseccion agrega el numero de veces que aparece
    n+=1                                                                # Permite continuar con el siguiente microset

# Ya con las modificaciones, se guarda la matriz.
zerocdhit.to_csv('DIR/Descargas_NCBI/CDHIT/MATRIXDATA/pymatrizcdhit.csv')

END

echo "Terminos, ahora estamos en BASH"
} 
f=$(date +%H:%M:%S)

echo "while con grep para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las $io y termino a las $f"
```
Con esto terminamos de darle el toque con el nombramiento de los archivos por default, para que solo se piense en el nombre de entrada y salida.
Asi, solo probamos como hacer que puedan ponerse las direcciones
```
#!/bin/bash

direccionbash="DIR/Desktop/ITRASIG"
otrdireccion="DIR/Desktop/SABE"
 
export direccionbash otrdireccion 

python3 - << END
import os

direccionbash = os.environ.get('direccionbash')
otrdireccion = os.environ.get('otrdireccion')

input_file = os.path.join(direccionbash, 'entradaoutput.txt')
input_file2 = os.path.join(otrdireccion, 'saludo.txt')

with open(input_file, 'r') as ffile:
	input = ffile.read().strip()

with open(input_file2, 'r') as sal:
	input2 = sal.read().strip()

print(input)
print(input2)
END
```
Y funciona para la salida.

Asi el codigo final
```
#!/bin/bash

##### SIEMPRE DE PREFERENCIA RUTA COMPLETA #####
outfilecdhit="clusterprotcatALL2000.clstr"      # Colocar aqui el nombre del archivo que tiene la salida con el outfile ".clstr"
OUTCDHIT="DIR/Descargas_NCBI/CDHIT/TODOS"            # Coloque la direccion donde se encuentra la salida de cd-hit

inputmatrizfile="inputmatrizcdhit.mtcdhit"
outputmatrizfile="pymatrizcdhit.csv"            # Coloca el nombre de salida para la matriz en ".csv"
DIRMATRIZ="DIR/Descargas_NCBI/CDHIT/MATRIXDATA"      # Coloque la direccion donde se arrojara las salidas de procesamiento para la matriz

GENOMES="DIR/Descargas_NCBI/IMGPSEUDOMONASGENOMES"   # Coloque la direccion donde esta el conjunto de genomas a procesar.

# DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT
concatimgenome="200424_grepfaa.txt"             # Nombre del archivo donde va la salida en formato idgenoma:idproteina
filtrado="filtclusterprotcatALL2000.clstr"      # Aqui va el nombre de la salida del archivo que solo tiene el cluster y sus accesiones respectivas de las proteinas respetando el original
clu_prot="filtclstr_a_tempseek.txt"             # En este archivo ya con el "filtrado" simplemente se les da formato "Cluster[0-9]+:idproteina"
pegaconcaclu="grepfaa_filtclstr.txt"            # Resultado de concatenar "$concatimgenome" y "$clu_prot" para despues usarlo y generar el input para python
solonamecluster="shtopy_Clust.txt"              # Aqui solo se concatena todos los cluster
onlynamegenomes="shtopy_genomes.txt"            # Solo van los nombres de los genomas
# DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT

io=$(date +%H:%M:%S)
time{
echo "INICIO PARA FORMAR LA MATRIZ BASH"

# Buscamos la salida en formato idgenoma:idproteina de las fuentes originales para concatenarlos en un solo archivo.
grep -E -o "^>[0-9]+" $GENOMES/*/*faa | awk -F "/[0-9]+.genes.faa:>" '{print $1 ":" $2}' > $DIRMATRIZ/$concatimgenome

# Por aca solo obtenemos las accesiones del analisis en CD-HIT
awk -F ">" '{print $2}' $OUTCDHIT/$outfilecdhit | awk -F "." '{print $1}' > $DIRMATRIZ/$filtrado

# Mantiene el formato, pero cambiamos de "Cluster [0-9]+" a "Cluster[0-9]+" del filtrado de la salida de "CDHIT"
awk '{gsub(/\s/, "", $0); print}' $DIRMATRIZ/$filtrado > $DIRMATRIZ/tmp.tmp && mv $DIRMATRIZ/tmp.tmp $DIRMATRIZ/$filtrado

# Con esto hacemos el formato de Cluster[0-9]+:idproteina
rm "$DIRMATRIZ/$clu_prot"
filtdata_file=$(cat "$DIRMATRIZ/$filtrado")
echo $filtdata_file | sed 's/\sCluster/\nCluster/g' | while IFS= read -r linea
do
        n=$(echo "$linea" | grep -E -o "Cluster[0-9]+" | grep -E -o "[0-9]+")
        echo "$linea" | sed -E "s/\s/ Cluster$n:/g" | sed -E 's/(Cluster[0-9]+ )//g' | sed -E 's/\s/\n/g' >> "$DIRMATRIZ/$clu_prot"
done

# Despues de concatenar en "$concatimgenome" en formato "idgenoma:idproteina" y en "$clu_prot" en formato "Cluster[0-9]+:idproteina"
# Simplemente pasamos a juntarlos "idgenoma:idproteina" y "Cluster[0-9]+:idproteina"
paste $DIRMATRIZ/$concatimgenome $DIRMATRIZ/$clu_prot > $DIRMATRIZ/$pegaconcaclu

# Para este ultimo lo pasamos a formato "Cluster[0-9]+:idgenoma:No.Repeticiones" (importante sort y despues uniq -c en ese orden)
awk -F ":" '{print $2 ":" $1}' $DIRMATRIZ/$pegaconcaclu | cut -f 2 | sort | uniq -c | awk -F " " '{print $2 ":" $1}' > $DIRMATRIZ/$inputmatrizfile

# Antes creamos unas variables para introducirlas a codigo en PYTHON
# extraemos todos los Cluster[0-9]+
cols=$(grep "Cluster" $DIRMATRIZ/$filtrado)
echo $cols > "$DIRMATRIZ/$solonamecluster"

# Extraemos todos los genomas que fueron usados.
filas=$(ls $GENOMES | tr '\n' ' ')
echo -e "$filas" > "$DIRMATRIZ/$onlynamegenome"

# EXPORTANDO PARA PYTHON
export DIRMATRIZ solonamecluster inputmatrizfile outputmatrizfile

python3 - << END
#Codigo python
import os
import pandas as pd
import sys
print("Nos encontramos en PYTHON")

# LLAMAMOS LAS VARIABLES DE LAS DIRECCIONES Y ARCHIVOS QUE NECESITAMOS
DIRMATRIZ = os.environ.get('DIRMATRIZ')

solonamecluster = os.environ.get('solonamecluster')
listclust = os.path.join(DIRMATRIZ, solonamecluster)

onlynamegenomes = os.environ.get('onlynamegenomes')
listgenome = os.path.join(DIRMATRIZ, onlynamegenomes)

inputmatrizfile = os.environ.get('inputmatrizfile')
inputmtz = os.path.join(DIRMATRIZ, inputmatrizfile)

outputmatrizfile = os.environ.get('outputmatrizfile')
outputmtz = os.path.join(DIRMATRIZ, outputmatrizfile)


# Imprimimos cols que tiene todos los numeros de cluster para saber en que formato trabaja
with open(listclust, 'r') as Clus:  # Se guarda en una variable Clus
    cols = Clus.read().strip()                                                                          # Los datos los guarda con otro tipo de variable para trabajar
    cols = cols.split(' ')                                                                              # Quita los espacios para convertir el set de Cluster en una lista gigante

# Llamamos el archivo con las accesiones de los genomas.
with open(listgenome, 'r') as fila:    # Se guarda en una variable fila
    fl = fila.read().strip()                                                                                # Los datos los guarda con otro tipo de variable para trabajar
    fl = fl.split(' ')                                                                                      # Quita los espacios para convertir el set de genomas en una lista

# Hacemos el dataframe lleno de ceros.
zerocdhit = pd.DataFrame(0, index=fl, columns=cols)

# Llamamos al archivo de entrada con formato "Cluster[0-9]+:idgenoma:No.Repeticiones" para generar el conteo y guardarlo en la matriz.
with open(inputmtz, 'r') as entrada:   # Se guarda en una variable entrada
    input = entrada.read().strip()                                                                                  # Los datos los guarda con otro tipo de variable para trabajar
    input = input.split('\n')                                                                                       # Quita los espacios para convertir el set de entrada en una lista gigante

# Comienza el conteo desde 0, para hacer el llamado del dato inicial
n = 0
while n < len(input):
    subconjunto = input[n].split(":")                                   # Como hace el llamado por linea, quita ":" para crear micro listas
    # Ahora si la entrada de los datos para formar la matriz
    zerocdhit.at[ subconjunto[1], subconjunto[0] ] = subconjunto[2]     # Ahora con las microlistas, con
                                                                        # subconjunto[1] nombra la accesion genoma, 
                                                                        # subconjunto[0] llama Cluster y 
                                                                        # subconjunto[2] en esa interseccion agrega el numero de veces que aparece
    n+=1                                                                # Permite continuar con el siguiente microset

# Ya con las modificaciones, se guarda la matriz.
zerocdhit.to_csv(outputmtz)

END

echo "Terminos, ahora estamos en BASH"
} 
f=$(date +%H:%M:%S)

echo "while con grep para busqueda en un segundo archivo y almacena nombre cluster en segundo archivo inicio a las $io y termino a las $f"
```
Queda comprobar si funciona y corregir.
 Salida
```

./testpysh.sh: line 23: time{: command not found
INICIO PARA FORMAR LA MATRIZ BASH
rm: cannot remove 'DIR/Descargas_NCBI/CDHIT/MATRIXDATA/testpysh_filtchangeformat.clustidp': No such file or directory
./testpysh.sh: line 58: DIR/Descargas_NCBI/CDHIT/MATRIXDATA/: Is a directory
Nos encontramos en PYTHON
Traceback (most recent call last):
  File "<stdin>", line 14, in <module>
  File "/usr/lib/python3.8/posixpath.py", line 90, in join
    genericpath._check_arg_types('join', a, *p)
  File "/usr/lib/python3.8/genericpath.py", line 152, in _check_arg_types
    raise TypeError(f'{funcname}() argument must be str, bytes, or '
TypeError: join() argument must be str, bytes, or os.PathLike object, not 'NoneType'
Terminos, ahora estamos en BASH
./testpysh.sh: line 121: syntax error near unexpected token `}'
./testpysh.sh: line 121: `} '
```
El comando con el que empezamos, guarda toda la direccion y no solo el nombre de las carpetas que tiene id de los genomas

Se elimino el comando `time{}`

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/d1ec9db2-db36-43eb-8045-8339cbab0037)

Para ello se modificara.
```
grep -E -o "^>[0-9]+" $GENOMES/*/*faa | grep -E -w -o "[0-9]+/[0-9]+.*" | awk -F "/[0-9]+.genes.faa:>" '{print $1 ":" $2}' > $DIRMATRIZ/$concatimgenome
```

Salio este resultado

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/27e27e33-6855-4233-8446-b7ca176cc786)

Pero entro a python y de ahi ya no continuo. al parecer no se encuentra una variable exportada
```
# EXPORTANDO PARA PYTHON
export DIRMATRIZ solonamecluster inputmatrizfile outputmatrizfile

python3 - << END
#Codigo python
import os
import pandas as pd
import sys
print("Nos encontramos en PYTHON")

# LLAMAMOS LAS VARIABLES DE LAS DIRECCIONES Y ARCHIVOS QUE NECESITAMOS
DIRMATRIZ = os.environ.get('DIRMATRIZ')

solonamecluster = os.environ.get('solonamecluster')
listclust = os.path.join(DIRMATRIZ, solonamecluster)

onlynamegenomes = os.environ.get('onlynamegenomes')
listgenome = os.path.join(DIRMATRIZ, onlynamegenomes)

inputmatrizfile = os.environ.get('inputmatrizfile')
inputmtz = os.path.join(DIRMATRIZ, inputmatrizfile)

outputmatrizfile = os.environ.get('outputmatrizfile')
outputmtz = os.path.join(DIRMATRIZ, outputmatrizfile)
```

```
# Buscamos la salida en formato idgenoma:idproteina de las fuentes originales para concatenarlos en un solo archivo.
grep -E -o "^>[0-9]+" $GENOMES/*/*faa | grep -E -w -o "[0-9]+/[0-9]+.*" | awk -F "/[0-9]+.genes.faa:>" '{print $1 ":" $2}' > $DIRMATRIZ/$concatimgenome

# Por aca solo obtenemos las accesiones del analisis en CD-HIT
awk -F ">" '{print $2}' $OUTCDHIT/$outfilecdhit | awk -F "." '{print $1}' > $DIRMATRIZ/$filtrado

# Mantiene el formato, pero cambiamos de "Cluster [0-9]+" a "Cluster[0-9]+" del filtrado de la salida de "CDHIT"
awk '{gsub(/\s/, "", $0); print}' $DIRMATRIZ/$filtrado > $DIRMATRIZ/tmp.tmp && mv $DIRMATRIZ/tmp.tmp $DIRMATRIZ/$filtrado

# Con esto hacemos el formato de Cluster[0-9]+:idproteina
rm "$DIRMATRIZ/$clu_prot"
filtdata_file=$(cat "$DIRMATRIZ/$filtrado")
echo $filtdata_file | sed 's/\sCluster/\nCluster/g' | while IFS= read -r linea
do
        n=$(echo "$linea" | grep -E -o "Cluster[0-9]+" | grep -E -o "[0-9]+")
        echo "$linea" | sed -E "s/\s/ Cluster$n:/g" | sed -E 's/(Cluster[0-9]+ )//g' | sed -E 's/\s/\n/g' >> "$DIRMATRIZ/$clu_prot"
done

# Despues de concatenar en "$concatimgenome" en formato "idgenoma:idproteina" y en "$clu_prot" en formato "Cluster[0-9]+:idproteina"
# Simplemente pasamos a juntarlos "idgenoma:idproteina" y "Cluster[0-9]+:idproteina"
paste $DIRMATRIZ/$concatimgenome $DIRMATRIZ/$clu_prot > $DIRMATRIZ/$pegaconcaclu

# Para este ultimo lo pasamos a formato "Cluster[0-9]+:idgenoma:No.Repeticiones" (importante sort y despues uniq -c en ese orden)
awk -F ":" '{print $2 ":" $1}' $DIRMATRIZ/$pegaconcaclu | cut -f 2 | sort | uniq -c | awk -F " " '{print $2 ":" $1}' > $DIRMATRIZ/$inputmatrizfile

# Antes creamos unas variables para introducirlas a codigo en PYTHON
# extraemos todos los Cluster[0-9]+
cols=$(grep "Cluster" $DIRMATRIZ/$filtrado)
echo $cols > "$DIRMATRIZ/$solonamecluster"
```




















