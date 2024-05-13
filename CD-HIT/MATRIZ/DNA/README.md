# Codigo para correr en el cluster
### Fecha 18 de abril del 2024
```
#!/bin/bash
# Use current working directory
#$ -cwd
#
# Join stdout and stderr
#$ -j y
#
# Run job through bash shell
#$ -S /bin/bash
#
#You can edit the scriptsince this line
#
# Your job name
#$ -N MatrixCDHIT
#
# Send an email after the job has finished
#$ -m e
#$ -M marcosu...
#
#
# Resources of compute
# -pe 8
# -l mem=10
#
# output files to run
#
#$ -o ../matrizcdhit_output.$JOB_ID.out # Salida estandar
#$ -e ../matrizcdhit_output.$JOB_ID.err # Archivo con los errores
#
# If modules are needed, source modules environment (Do not delete the next line):
#  Con el gato, ya no necesitamos algun modulo de ambiente.
#
# Add any modules you might require:

#
# Write your commands in the next line

DIR="Direccion/Pseudomonas"
MATRIXCDOUT="WORK/ANALYSIS_CDHIT/MATRIXCDHIT"
DATA="WORK/ANALYSIS_CDHIT/RESULTSCLUSTERCDHIT/pseudocluster.clstr"

#Prueba rapida para el final del codigo
rm "$DIR/$MATRIXCDOUT/clust.tmp"

# Patrón para identificar el inicio de un nuevo cluster
patron1=">Cluster"
patron2="[0-9]+aa"
ni=0
nfinal=$(grep -E "$patron1" $DIR/$DATA | wc -l)
nfinal=$((nfinal-1))
echo $nfinal

# Iterar sobre el archivo
cd $DIR/PSEUDOMONAS_GENOMAS
echo "idgenomas" > $DIR/$MATRIXCDOUT/cdmatrizhit.txt
ls | tr '\s' '\n' >> $DIR/$MATRIXCDOUT/cdmatrizhit.txt
while [[ $ni -le $nfinal ]]; do
        limitei=$(grep -o -n -w "Cluster $ni" $DIR/$DATA | grep -Eo "^[0-9]+")
        nf=$((ni+1))
        limitef=$(grep -o -n -w "Cluster $nf" $DIR/$DATA | grep -Eo "^[0-9]+")
        limitei=$((limitei+1))
        limitef=$((limitef-1))
        if [ $limitef != "-1" ]; then
        clusterset=$(sed -n "$limitei,${limitef}p" "$DIR/$DATA")
        else
        ult=$(tail -n 1 $DIR/$DATA)
        limitef=$(grep -n "$ult" $DIR/$DATA | grep -o "^[0-9]*")
        clusterset=$(sed -n "$limitei,${limitef}p" "$DIR/$DATA")
        fi
        pizzitas=""
        pizzitas="$pizzitas\t$ni"
        while M= read -r  lineas; do
                busqueda=$(echo "$lineas" | grep -E -o -w ">[0-9]+")
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
        cont=$(echo -e "$cont" | tail -n $n)
        echo -e "$cont" >> "$DIR/$MATRIXCDOUT/clust.tmp"
        paste $DIR/$MATRIXCDOUT/cdmatrizhit.txt $DIR/$MATRIXCDOUT/clust.tmp > $DIR/$MATRIXCDOUT/cdmatrizhit.tmp && mv $DIR/$MATRIXCDOUT/cdmatrizhit.tmp $DIR/$MATRIXCDO$
        head -n $n $DIR/$MATRIXCDOUT/cdmatrizhit.txt > $DIR/$MATRIXCDOUT/cdmatrizhit.tmp && mv $DIR/$MATRIXCDOUT/cdmatrizhit.tmp $DIR/$MATRIXCDOUT/cdmatrizhit.txt
        ni=$((ni+1))
done
```
Empezo a correr el script a las 07:17:26 del 18 de abril del 2024

# Actualizado 5 de mayo del 2024
Aqui el script para utilizar en DNA con un 93% mas de rapidez que el anterior
```
#!/bin/bash
# Use current working directory
#$ -cwd
#
# Join stdout and stderr
#$ -j y
#
# Run job through bash shell
#$ -S /bin/bash
#
#You can edit the scriptsince this line
#
# Your job name
#$ -N MatrixCDHIT
#
# Send an email after the job has finished
#$ -m e
#$ -M marcosu...
#
#
# Resources of compute
# -pe 8
# -l mem=10
#
# output files to run
#
#$ -o ../matrizcdhit_output.$JOB_ID.out # Salida estandar
#$ -e ../matrizcdhit_output.$JOB_ID.err # Archivo con los errores
#
# If modules are needed, source modules environment (Do not delete the next line):
#  Con el gato, ya no necesitamos algun modulo de ambiente.
#
# Add any modules you might require:

#
# Write your commands in the next line

##### SIEMPRE DE PREFERENCIA RUTA COMPLETA #####
outfilecdhit="clusterprotcatALL2000.clstr"                # Colocar aqui el nombre del archivo que tiene la salida con el outfile ".clstr"
OUTCDHIT="DIR/Descargas_NCBI/CDHIT/TODOS"            # Coloque la direccion donde se encuentra la salida de cd-hit

inputmatrizfile="testpysh_inputmatrizcdhit.mtcdhit"       # El nombre del archivo que se genera en automatico, input para generar la matriz
outputmatrizfile="testpysh_pymatrizcdhit.csv"             # Coloca el nombre de salida para la matriz en ".csv"
DIRMATRIZ="DIR/Descargas_NCBI/CDHIT/MATRIXDATA"      # Coloque la direccion donde se arrojara las salidas de procesamiento para la matriz

GENOMES="DIR/Descargas_NCBI/IMGPSEUDOMONASGENOMES"   # Coloque la direccion donde esta el conjunto de genomas a procesar.

# DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT
concatimgenome="testpysh_genomasproteinas.idgidp"         # Nombre del archivo donde va la salida en formato idgenoma:idproteina
filtrado="testpysh_filtclstr.cdhitpy"                     # Aqui va el nombre de la salida del archivo que solo tiene el cluster y sus accesiones respectivas de las proteinas respetando el original
clu_prot="testpysh_filtchangeformat.clustidp"             # En este archivo ya con el "filtrado" simplemente se les da formato "Cluster[0-9]+:idproteina"
pegaconcaclu="testpysh_concat.idgidpclustidp"             # Resultado de concatenar "$concatimgenome" y "$clu_prot" para despues usarlo y generar el input para python
solonamecluster="testpysh_clusters.txt"                   # Aqui solo se concatena todos los cluster
onlynamegenomes="testpysh_genomes.txt"                    # Solo van los nombres de los genomas
# DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT

io=$(date +%H:%M:%S)
start_time=$(date +%s)
echo "INICIO PARA FORMAR LA MATRIZ BASH"

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

# Antes de concatenar, vamos a ordenar por accesion de proteina tanto el archivo que tiene la variable "concatimgenome" y "clu_prot"
awk -F ":" '{print $2 ":" $1}' "$DIRMATRIZ/$concatimgenome" | sort -n | awk -F ":" '{print $2":"$1}' > "$DIRMATRIZ/temp" && mv "$DIRMATRIZ/temp" "$DIRMATRIZ/$concatimgenome"
awk -F ":" '{print $2 ":" $1}' "$DIRMATRIZ/$clu_prot" | sort -n | awk -F ":" '{print $2":"$1}' > "$DIRMATRIZ/temp" && mv "$DIRMATRIZ/temp" "$DIRMATRIZ/$clu_prot"

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
echo -e "$filas" > "$DIRMATRIZ/$onlynamegenomes"

# EXPORTANDO PARA PYTHON
export DIRMATRIZ solonamecluster onlynamegenomes inputmatrizfile outputmatrizfile

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
zerocdhit = zerocdhit.rename_axis("Genomas")

# Llamamos al archivo de entrada con formato "Cluster[0-9]+:idgenoma:No.Repeticiones" para generar el conteo y guardarlo en la matriz.
with open(inputmtz, 'r') as entrada:   # Se guarda en una variable entrada
    input = entrada.read().strip()                                                                                  # Los datos los guarda con otro tipo de variable para trabajar
    input = input.split('\n')                                                                                       # Quita los espacios para convertir el set de entrada en una lista gigante

# Comienza el conteo desde 0, para hacer el llamado del dato inicial

n = 0
while n < len(input):
    subconjunto = input[n].split(":")                                   # Como hace el llamado por linea, quita ":" para crear micro listas
    # print(subconjunto)
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

f=$(date +%H:%M:%S)
end_time=$(date +%s)
elapsed_time=$(($end_time - $start_time))
hours=$((elapsed_time / 3600))
minutes=$(( (elapsed_time % 3600) / 60 ))
seconds=$((elapsed_time % 60))

echo "El script inicio a las $io y termino a las $f. Con un tiempo transcurrido: $hours horas, $minutes minutos, $seconds segundos."
```
Falta actualizar en el cluster

# 12 de mayo del 2024
Procedemos a avanzar con la generacion de la matriz, pero usando `PYTHON 2.7.5` (antes asgurando que si funciona la llamada de la version y la funcion de la version con un pequeño script.
```
#!/bin/bash
# Use current working directory
#$ -cwd
#
# Join stdout and stderr
#$ -j y
#
# Run job through bash shell
#$ -S /bin/bash
#
#You can edit the scriptsince this line
#
# Your job name
#$ -N Fast_MatrixCDHIT
#
# Send an email after the job has finished
#$ -m e
#$ -M marcos...
#
#
# Resources of compute
# -pe 8
# -l mem=10
#
# output files to run
#
#$ -o ../fast_matrizcdhit_output.$JOB_ID.out # Salida estandar
#$ -e ../fast_matrizcdhit_output.$JOB_ID.err # Archivo con los errores
#
# If modules are needed, source modules environment (Do not delete the next line):
#  Con el gato, ya no necesitamos algun modulo de ambiente.
#
# Add any modules you might require:

#
# Write your commands in the next line

##### SIEMPRE DE PREFERENCIA RUTA COMPLETA #####
outfilecdhit="pseudocluster.clstr"                                # Colocar aqui el nombre del archivo que tiene la salida con el outfile ".clstr"
OUTCDHIT="DIR/Descargas_NCBI/CDHIT/TODOS"            # Coloque la direccion donde se encuentra la salida de cd-hit

inputmatrizfile="testpysh_inputmatrizcdhit.mtcdhit"       # El nombre del archivo que se genera en automatico, input para generar la matriz
outputmatrizfile="testpysh_pymatrizcdhit.csv"             # Coloca el nombre de salida para la matriz en ".csv"
DIRMATRIZ="DIR/Descargas_NCBI/CDHIT/MATRIXDATA"      # Coloque la direccion donde se arrojara las salidas de procesamiento para la matriz

GENOMES="DIR/Descargas_NCBI/IMGPSEUDOMONASGENOMES"   # Coloque la direccion donde esta el conjunto de genomas a procesar.

# DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT
concatimgenome="testpysh_genomasproteinas.idgidp"         # Nombre del archivo donde va la salida en formato idgenoma:idproteina
filtrado="testpysh_filtclstr.cdhitpy"                     # Aqui va el nombre de la salida del archivo que solo tiene el cluster y sus accesiones respectivas de las proteinas respetando el original
clu_prot="testpysh_filtchangeformat.clustidp"             # En este archivo ya con el "filtrado" simplemente se les da formato "Cluster[0-9]+:idproteina"
pegaconcaclu="testpysh_concat.idgidpclustidp"             # Resultado de concatenar "$concatimgenome" y "$clu_prot" para despues usarlo y generar el input para python
solonamecluster="testpysh_clusters.txt"                   # Aqui solo se concatena todos los cluster
onlynamegenomes="testpysh_genomes.txt"                    # Solo van los nombres de los genomas

PYTHON="/usr/local/bin/python275"                         # Ruta en la que se encuentra la version de python.
# DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT

io=$(date +%H:%M:%S)
start_time=$(date +%s)
echo "INICIO PARA FORMAR LA MATRIZ BASH"

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

# Antes de concatenar, vamos a ordenar por accesion de proteina tanto el archivo que tiene la variable "concatimgenome" y "clu_prot"
awk -F ":" '{print $2 ":" $1}' "$DIRMATRIZ/$concatimgenome" | sort -n | awk -F ":" '{print $2":"$1}' > "$DIRMATRIZ/temp" && mv "$DIRMATRIZ/temp" "$DIRMATRIZ/$concatimgenome"
awk -F ":" '{print $2 ":" $1}' "$DIRMATRIZ/$clu_prot" | sort -n | awk -F ":" '{print $2":"$1}' > "$DIRMATRIZ/temp" && mv "$DIRMATRIZ/temp" "$DIRMATRIZ/$clu_prot"

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
echo -e "$filas" > "$DIRMATRIZ/$onlynamegenomes"

# EXPORTANDO PARA PYTHON
export DIRMATRIZ solonamecluster onlynamegenomes inputmatrizfile outputmatrizfile

$PYTHON - << END
#Codigo python
import os
import pandas as pd
import sys
print("Nos encontramos en PYTHON2.7.5")

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
zerocdhit = zerocdhit.rename_axis("Genomas")

# Llamamos al archivo de entrada con formato "Cluster[0-9]+:idgenoma:No.Repeticiones" para generar el conteo y guardarlo en la matriz.
with open(inputmtz, 'r') as entrada:   # Se guarda en una variable entrada
    input = entrada.read().strip()                                                                                  # Los datos los guarda con otro tipo de variable para trabajar
    input = input.split('\n')                                                                                       # Quita los espacios para convertir el set de entrada en una lista gigante

# Comienza el conteo desde 0, para hacer el llamado del dato inicial

n = 0
while n < len(input):
    subconjunto = input[n].split(":")                                   # Como hace el llamado por linea, quita ":" para crear micro listas
    # print(subconjunto)
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

f=$(date +%H:%M:%S)
end_time=$(date +%s)
elapsed_time=$(($end_time - $start_time))
hours=$((elapsed_time / 3600))
minutes=$(( (elapsed_time % 3600) / 60 ))
seconds=$((elapsed_time % 60))

echo "El script inicio a las $io y termino a las $f. Con un tiempo transcurrido: $hours horas, $minutes minutos, $seconds segundos."
```
