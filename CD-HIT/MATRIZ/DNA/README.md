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
