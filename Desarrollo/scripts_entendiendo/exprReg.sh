#!/bin/bash
datox="../DATOS/proka_nombre_accesion_ftp.txt"

cp $datox "../DATOS/copiadatospara_exprRegsh.txt"

datos="../DATOS/copiadatospara_exprRegsh.txt"
longitud=$(wc -l < $datos)
ftp=$(cut -f 3 $datos)

puro=$(echo "$ftp" | awk 'NR>=2 && NR<=$longitud {print $1}')

echo "$puro" | sed -E "s/GCA/GCF/g" | sed -E "s/ftp:/http:/g" | sed -E "s/(GCF_(.*))/\1\/\1_genomic.fna.gz/g" > ../DATOS/filtGolpe.txt
head -n 5 ../DATOS/filtGolpe.txt

filtr="../DATOS/filtGolpe.txt"
http=$(cut -f 1 $filtr)
cd ../RESULTADOS/
n=1
for i in $http
do

        while [ $n -le 2 ]
        do
		echo "$i"		
		wget $i
                n=$((n+1))
                [ $n -le 2 ] && break
        done

done


ls ./
rm genomic*
