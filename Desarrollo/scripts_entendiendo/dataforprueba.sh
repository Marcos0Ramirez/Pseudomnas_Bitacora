#!/bin/bash
datos="../DATOS/proka_nombre_accesion_ftp.txt"

longitud=$(wc -l < $datos)
ftp=$(cut -f 3 $datos)

#Ahora que tenemos el conteo, ahora podemos delimitar la informacion, sin tomar en cuenta el encabezado y de ahi partir a considerar todas las demas secuencias
puro=$(echo "$ftp" | awk 'NR>=2 && NR<=$longitud {print $1}')

n=0
for i in $puro
do

        while [ $n -le 5 ]
        do
                echo "$i"
                n=$((n+1))
                [ $n -le 5 ] && break
        done

done
