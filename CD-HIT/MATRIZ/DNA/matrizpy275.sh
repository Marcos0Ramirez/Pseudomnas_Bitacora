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
#$ -N Fast_MatrixCDHIT_py275
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
#$ -o ../matrizpy275cdhit_output.$JOB_ID.out # Salida estandar
#$ -e ../matrizpy275cdhit_output.$JOB_ID.err # Archivo con los errores
#
# If modules are needed, source modules environment (Do not delete the next line):
#  Con el gato, ya no necesitamos algun modulo de ambiente.
#
# Add any modules you might require:

#
# Write your commands in the next line

##### SIEMPRE DE PREFERENCIA RUTA COMPLETA #####
outfilecdhit="pseudocluster.clstr"                              # Colocar aqui el nombre del archivo que tiene la salida con el outfile ".clstr"
OUTCDHIT="DIR/DONDE/SE/ENCUENTRA/EL/CD-HIT/ANALYSIS"            # Coloque la direccion donde se encuentra la salida de cd-hit

outputmatrizfile="cdhit_clustermatriz.csv"                      # Coloca el nombre de salida para la matriz en ".csv"
DIRMATRIZ="DIR/DONDE/SE/DEPOSITARA/LA/MATRIZ"                   # Coloque la direccion donde se arrojara las salidas de procesamiento para la matriz

GENOMES="DIR/DONDE/ESTAN/LOS/GENOMAS"   # Coloque la direccion donde esta el conjunto de genomas a procesar.

# DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT
idgen_idprot="a_genomasproteinas.idgidp"              # idgenoma:idproteina SALIDA
filtrado="b_cambio_clustnidp.cdhitpy"                   # Aqui va el nombre de la salida del archivo que solo tiene el cluster y sus accesiones respectivas de las proteinas respetando el original
cluster_idprot="c_clusteridproteina.clustidp"                 # En este archivo ya con el "filtrado" simplemente se les da formato "Cluster[0-9]+:idproteina"
solonamecluster="d_clusters.txt"                        # Aqui solo se concatena todos los cluster
onlynamegenomes="e_genomes.txt"                         # Solo van los nombres de los genomas

PYTHON="python2"                                        # Ruta en la que se encuentra la version de python.
# DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT # DEFAULT

io=$(date +%H:%M:%S)
start_time=$(date +%s)
echo "INICIO PARA FORMAR LA MATRIZ BASH"

# Buscamos la salida en formato idgenoma:idproteina de las fuentes originales para concatenarlos en un solo archivo.
######## Comprobado que funciona correctamente esta parte del codigo con la discrimiacion de cluster y id de proteinas
grep -E -o "^>[0-9]+" $GENOMES/*/*faa | grep -E -w -o "[0-9]+/[0-9]+.*" | awk -F "/[0-9]+.genes.faa:>" '{print $1 ":" $2}' > $DIRMATRIZ/$idgen_idprot

# Cambiamos el formato original del archivo de salida de CD-HIT para solo quedarnos con Cluster[0-9]+\nidp1\n...\nidpk
awk -F ">" '{print $2}' $OUTCDHIT/$outfilecdhit | awk -F "." '{print $1}' > $DIRMATRIZ/$filtrado

# Mantiene el formato, pero cambiamos de "Cluster [0-9]+" a "Cluster[0-9]+" del filtrado de la salida de "CDHIT"
awk '{gsub(/\s/, "", $0); print}' $DIRMATRIZ/$filtrado > $DIRMATRIZ/tmp.tmp && mv $DIRMATRIZ/tmp.tmp $DIRMATRIZ/$filtrado

# Con esto hacemos el formato de Cluster[0-9]+:idproteina
rm "$DIRMATRIZ/$cluster_idprot"
filtdata_file=$(cat "$DIRMATRIZ/$filtrado")
echo $filtdata_file | sed 's/\sCluster/\nCluster/g' | while IFS= read -r linea
do
        n=$(echo "$linea" | grep -E -o "Cluster[0-9]+" | grep -E -o "[0-9]+")
        echo "$linea" | sed -E "s/\s/ Cluster$n:/g" | sed -E 's/(Cluster[0-9]+ )//g' | sed -E 's/\s/\n/g' >> "$DIRMATRIZ/$cluster_idprot"
done

# Antes de concatenar, vamos a ordenar por accesion de proteina tanto el archivo que tiene la variable "idgen_idprot" y "cluster_idprot"
awk -F ":" '{print $2 ":" $1}' "$DIRMATRIZ/$idgen_idprot" | sort -n | awk -F ":" '{print $2":"$1}' > "$DIRMATRIZ/temp" && mv "$DIRMATRIZ/temp" "$DIRMATRIZ/$idgen_idprot"
awk -F ":" '{print $2 ":" $1}' "$DIRMATRIZ/$cluster_idprot" | sort -n | awk -F ":" '{print $2":"$1}' > "$DIRMATRIZ/temp" && mv "$DIRMATRIZ/temp" "$DIRMATRIZ/$cluster_idprot"

# Antes creamos unas variables para introducirlas a codigo en PYTHON
# extraemos todos los Cluster[0-9]+
cols=$(grep "Cluster" $DIRMATRIZ/$filtrado)
echo $cols > "$DIRMATRIZ/$solonamecluster"

# Extraemos todos los genomas que fueron usados.
filas=$(ls $GENOMES | tr '\n' ' ')
echo -e "$filas" > "$DIRMATRIZ/$onlynamegenomes"

# EXPORTANDO PARA PYTHON
export DIRMATRIZ solonamecluster onlynamegenomes idgen_idprot cluster_idprot outputmatrizfile

$PYTHON - << END

import re
import os
import pandas as pd
import sys

solonamecluster = os.environ.get('solonamecluster')
listclust = os.path.join(DIRMATRIZ, solonamecluster)

onlynamegenomes = os.environ.get('onlynamegenomes')
listgenome = os.path.join(DIRMATRIZ, onlynamegenomes)

idgen_idprot = os.environ.get('idgen_idprot')
catgenopro = os.path.join(DIRMATRIZ, idgen_idprot)

cluster_idprot = os.environ.get('cluster_idprot')
clusterprot = os.path.join(DIRMATRIZ, cluster_idprot)

outputmatrizfile = os.environ.get('outputmatrizfile')
outputmtz = os.path.join(DIRMATRIZ, outputmatrizfile)

#from collections import Counter
# Imprimimos cols que tiene todos los numeros de cluster para saber en que formato trabaja
with open(listclust, 'r') as Clus:  # Se guarda en una variable Clus
    cols = Clus.read().strip()      # Los datos los guarda con otro tipo de variable para trabajar
    cols = cols.split(' ')          # Quita los espacios para convertir el set de Cluster en una lista gigante

# Llamamos el archivo con las accesiones de los genomas.
with open(listgenome, 'r') as fila:    # Se guarda en una variable fila
    fl = fila.read().strip()           # Los datos los guarda con otro tipo de variable para trabajar
    fl = fl.split(' ')                 # Quita los espacios para convertir el set de genomas en una lista

with open(catgenopro, 'r') as entrada1:   # para idg:idp
    input1 = entrada1.read().strip()      # Los datos los guarda con otro tipo de variable para trabajar
    idgidp = input1.split('\n')           # Quita los espacios para convertir el set de entrada en una lista gigante

lista1 = idgidp.split("\n")      #Creamos la lista para mostrar los idg:idp que se van a eliminar

with open(clusterprot, 'r') as entrada2:   # para cluster:idp
    input2 = entrada2.read().strip()       # Los datos los guarda con otro tipo de variable para trabajar
    clustidp = input2.split('\n')          # Quita los espacios para convertir el set de entrada en una lista gigante

idpgenomas = re.findall(r"(?<=:)(\d+)", idgidp)
cdhitidp = re.findall(r"Cluster\d+:(\d+)\n", clustidp)

genomas = re.findall(r"(\d+):", idgidp)
cluster = re.findall(r"Cluster\d+", clustidp)

#Creacion de la matriz
zerocdhit = pd.DataFrame(0, index=fl, columns=cols)
zerocdhit = zerocdhit.rename_axis("Genomas")

print("Si no concuerdan el numero de id's de proteinas de los extraidos en genomas: ", len(idpgenomas), "y los usados por CD-HIT", len(cdhitidp))
print("entonces ... ")
clustergenoma=[]
frecuencia={}
n = 0
while n < len(cdhitidp):
        if idpgenomas[n] != cdhitidp[n]:
                print("eliminamos idgenoma:idproteina", lista1.pop(n), "de la proteina", idpgenomas.pop(n))
                genomas.pop(n)
                print("comprobamos que los siguientes esten correctos", "idgidp: ", idpgenomas[n], "cluster:idp: ", cdhitidp[n])
        else:
                clustergenoma.append(str(cluster[n]) + ':' + str(genomas[n]))
                if clustergenoma[n] in frecuencia:
                        frecuencia[clustergenoma[n]] += 1
                else:
                        frecuencia[clustergenoma[n]] = 1
                coordenadas=clustergenoma[n].split(":")
                zerocdhit.at[ coordenadas[1], coordenadas[0] ] = frecuencia[clustergenoma[n]]
                n+=1

print("Esperando que salga el mismo numero de id de proteinas tanto de los genomas: ", len(idpgenomas), "como de los usados por CD-HIT: ", len(cdhitidp))

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
