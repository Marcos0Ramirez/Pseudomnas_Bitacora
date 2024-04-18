# Codigo para correr en el cluster
### Fecha 18 de abril del 2024
```
#!/bin/bash

DIR="/mnt/c/Users/52477/Desktop/Descargas_NCBI"
MATRIXCDOUT="CDHIT/MATRIXDATA"
DATA="CDHIT/TODOS/clusterprotcatALL2000.clstr"

#Prueba rapida para el final del codigo
head -n 30 $DIR/$DATA > "$DIR/CDHIT/TODOS/30rengclusterprotcatALL2000.clstr"
DATA="CDHIT/TODOS/30rengclusterprotcatALL2000.clstr"
rm "$DIR/$MATRIXCDOUT/clust2.tmp"

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
        cont=$(echo -e "$cont" | tail -n $n)
        echo -e "$cont" >> "$DIR/$MATRIXCDOUT/clust2.tmp"
        paste $DIR/$MATRIXCDOUT/matriz2.txt $DIR/$MATRIXCDOUT/clust2.tmp > $DIR/$MATRIXCDOUT/matriz2.tmp && mv $DIR/$MATRIXCDOUT/matriz2.tmp $DIR/$MATRIXCDOUT/matriz2.txt
        head -n $n $DIR/$MATRIXCDOUT/matriz2.txt > $DIR/$MATRIXCDOUT/matriz2.tmp && mv $DIR/$MATRIXCDOUT/matriz2.tmp $DIR/$MATRIXCDOUT/matriz2.txt
        ni=$((ni+1))
done
```
