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
rm: cannot remove '/mnt/c/Users/52477/Desktop/Descargas_NCBI/CDHIT/MATRIXDATA/clugen.txt': No such file or directory

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
grep -E -o ">[0-9]+" */*faa | awk -F "/[0-9]+.genes.faa:>" '{print $1 ":" $2}' > ../CDHIT/MATRIXDATA/200424_grepfaa.txt

```
--------------------------------------------------------------------------------------------------------------------
