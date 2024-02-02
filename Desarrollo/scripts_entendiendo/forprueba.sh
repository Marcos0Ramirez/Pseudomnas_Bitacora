#!/bin/bash
datos="../DATOS/proka_nombre_accesion_ftp.txt"

ftp=$(cut -f 3 $datos)
n=1
for i in 1 2 3 4 5 6 7 8 9 10
do

	while [ $n -le 5 ]
	do
		echo "$i"
		n=$((n+1))
		[ $n -le 5 ] && break
	done

done 
