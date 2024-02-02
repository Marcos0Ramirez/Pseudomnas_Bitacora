29 de enero del 2024
### ***NO.1CODE <INICIO>***
> El trabajo fue hecho en computadora local
- Desarrollo del script, se llevo a acabo al entender com filtrar los datos, preguntandole a ChatGPT.
Para ello descargarmos un archivo con toda la informacion de los individuos

```
$ wget http://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/prokaryotes.txt
```
En donde se procedio a entender como era el archivo, para ello en secuencia.
1. Se abrio el archivo
2. Se leyo y reviso el formato
3. Se reviso solo algunas filas
4. Se reviso las columnas
5. Entender como cortar las columnas y extraerlas
6. Fijar el comando para guardarlo

```
    8  mkdir Descargas_NCBI
    9  cd Descargas_NCBI/
   10  wget http://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/prokaryotes.txt
   11  less wget http://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/prokaryotes.txt
   12  ls
   13  less prokaryotes.txt
   14  cut -d 't' -f 2 prokaryotes.txt
   15  head -n 5 prokaryotes.txt | cut -f 1
   16  head -n 5 prokaryotes.txt | cut -f 2
   17  head -n 5 prokaryotes.txt | cut -f 2 3
   18  head -n 5 prokaryotes.txt | cut -f 2&3
   19  head -n 5 prokaryotes.txt | cut -f 2, 3
   20  head -n 5 prokaryotes.txt | cut -f 2,3
   21  head -n 1 prokaryotes.txt
   22  head -n 5 prokaryotes.txt | cut -f 1,19,21
```

Este es el comando se va a usar para filtrar solo los datos necesarios, claro modificado.

```
head -n 5 prokaryotes.txt | cut -f 1,19,21
```

Aqui los comandos
```
   25  cut -f 1,19,21 prokaryotes.txt > proka_nombre_accesion_ftp.txt
   26  ls
   27  less proka_nombre_accesion_ftp.txt
```
Y los resultados
```
#Organism/Name  Assembly Accession      FTP Path
Campylobacter jejuni subsp. jejuni NCTC 11168 = ATCC 700819     GCA_000009085.1 ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/009/085/GCA_000009085.1_ASM908v1
Pseudomonas fluorescens GCA_900215245.1 ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/900/215/245/GCA_900215245.1_IMG-taxon_2617270901_annotated_assembly
Xanthomonas campestris pv. raphani      GCA_013388375.1 ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/013/388/375/GCA_013388375.1_ASM1338837v1
Salmonella enterica subsp. enterica serovar Typhimurium str. LT2        GCA_000006945.2 ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/006/945/GCA_000006945.2_ASM694v2
.
.
.
```
Regresamos al Word Bitacora en la computadora local...
#### ***NO.1CODE <FINAL>***

-----------------------------------------------------------------------------------------------------------------------------
 Con este codigo se pretende, imprimir las accesiones para ver si funcionan las varaiables
### ***NO.2CODE <INICIO>***
```
#!/bin/bash
Access="Accessions.txt"
Se extrae la primera columna
access=$(awk -F ',' '{print $1}' "$Access")

# Imprimir las accesiones
echo "Accesiones: $access"
```
#### ***NO.2CODE <FINAL>***

30 de enero del 2024
### ***NO.3CODE <INICIO>***
```
#!/bin/bash
Access="Accessions.txt"
Se extrae la primera columna
access=$(awk -F ',' '{print $1}' "$Access")

# Imprimir las accesiones
echo "Accesiones: $access"
# Se busca con awk y se almacenan los resuldados, sobreescribiendolos, sin borrar los ya encontrados
awk '/access/ { print $0 }' ../proka_nombre_accesion_ftp.txt >> ../RESULTADOS/resultados_accesiones_buscadas.txt
```
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
Al final no funciono el codigo anterior, por lo que se opto por usar un codigo mas simple y optimo
1. El cual, en Accessions.txt se tienen las accesiones en una columna
2. Se comparan en el archivo nuevo, para el cual solo se tienen las columnas necesarias
3. finalmente, guarda los resultados que tuvieron match en otra carpeta
4. Se puede disponer del archivo

```
#!/bin/bash

# Archivos
accessions="../DATOS/Accessions.txt"
busca="../DATOS/proka_nombre_accesion_ftp.txt"
guarda="../RESULTADOS/resultados_accesiones_buscadas.txt"

# Buscar y almacenar los resultados en el archivo
grep -F -f "$accessions" "$busca" > "$guarda"

# Mostrar archivo
more "$guarda"
```
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

#### ***NO.3CODE <FIN>***

#### ***NO.4CODE <INICIO>***
## 31 de enero del 2024
5. Despues el archivo, pretende guardar las direcciones FTP (para ello se probo, el comando cut y for para infresarlo a expresiones regulares y cambiar el url y descarlarlo desde ahi
```
#!/bin/bash
datos="../DATOS/proka_nombre_accesion_ftp.txt"

ftp=$(cut -f 3 $datos)

for i in "$ftp"
do
n=0
        while [ n < 10 ]
        do
                echo "$i"
                ((n++))
        done
done
```
(Algunas partes de los comandos fueron consultados con ChatGPT y asegurados con pruebas que funcionara)
1. No funciono, pero se econtro otra forma de poder hacer la delimitacion de las impresiones para trabajar solo con eso
2. Para ello se tiene que eliminar del corte de las columnas los encabezados que son los que aparecen primero
```
#!/bin/bash
# Llamamos al archivo, para manipularlo
datos="../DATOS/proka_nombre_accesion_ftp.txt"

# Tomamos la medida del numero de lineas o equivalente al numero posible de archivos (porque tambien contempla los que no tienen datos o "-").
longitud=$(wc -l < $datos)
# Ahora se extraen los datos de la columna 3, del archivo ya filtrado y se le tomas los que solo tienen las direcciones FTP
ftp=$(cut -f 3 $datos)

#Ahora que tenemos el conteo, ahora podemos delimitar la informacion, sin tomar en cuenta el encabezado y de ahi partir a considerar todas las demas secuencias
# Finalmente se toma la variable ftp, porque es demasiada grande y se imprime como un texto, donde ahora se puede aplicar awk, para que busque desde ahi y no tenga que soportar la variable con todos los datos, y finalmente se delimita de quitando los dos primeros, que son los titulos y contemplando hasta el ultimo FTP.
puro=$(echo "$ftp" | awk 'NR>=2 && NR<=$longitud {print $1}')

n=0
for i in $puro
do

        while [ $n -le 5 ] # Al parecer aqui no se contempla el limite de la suma
        do
                echo "$i" # Aqui se imprime y se espera que tome la linea de comandos
                n=$((n+1)) # Va sumando y guardando el conteo para la siguiente iteración
                [ $n -le 5 ] && break # Hasta aqui, se continua el conteo.
        done

done
```
Codigo sin descripción
```
#!/bin/bash
datos="../DATOS/proka_nombre_accesion_ftp.txt"

longitud=$(wc -l < $datos)
ftp=$(cut -f 3 $datos)

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
```
#### ***NO.4CODE <FIN>***

#### ***NO.5CODE <INICIO>***
Para este punto creamos el script: *exprReg.sh* para lograr la modificacion del archivo, y hacer que podamos el cambio de los datos. Antes de eso, realizamos una copia del archivo para que pueda ser manipulado el segundo, sin modificar el primero.


```
#!/bin/bash
datox="../DATOS/proka_nombre_accesion_ftp.txt"

cp $datox "../DATOS/copiadatospara_exprRegsh.txt"

datos="../DATOS/copiadatospara_exprRegsh.txt"
longitud=$(wc -l < $datos)
ftp=$(cut -f 3 $datos)

puro=$(echo "$ftp" | awk 'NR>=2 && NR<=$longitud {print $1}')

echo "$puro" > ../DATOS/FTP_filtrado.txt
# head -n 5 ../DATOS/FTP_filtrado.txt
sed -E "s/GCA/GCF/g" ../DATOS/FTP_filtrado.txt > ../DATOS/FTP_filtrado-GCA-GCF.txt
# head -n 5 ../DATOS/FTP_filtrado-GCA-GCF.txt
sed -E "s/ftp:/http:/g" ../DATOS/FTP_filtrado-GCA-GCF.txt > ../DATOS/FTP_filtrado-GCA-GCF_FTP-HTTP.txt
head -n 5 ../DATOS/FTP_filtrado-GCA-GCF_FTP-HTTP.txt
sed -E "s/(GCF_(.*))/\1\/\1_genomic.fna.gz/g" ../DATOS/FTP_filtrado-GCA-GCF_FTP-HTTP.txt > ../DATOS/FTP_filtrado-GCA-GCF_FTP-HTTP_null-genomic.txt
head -n 5 ../DATOS/FTP_filtrado-GCA-GCF_FTP-HTTP_null-genomic.txt

filtr="../DATOS/FTP_filtrado-GCA-GCF_FTP-HTTP_null-genomic.txt"
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
```
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Codigo final, script llamado *descargafnagz.sh*, y consta del codigo siguiente
Explicacion:
1. Consulta de un archivo llamado *Accessions.txt*
2. Lo compara con la tabla *proka_nombre_accesion_ftp.txt*
3. Guarda los datos solicitados en *resultados_accesiones_buscadas.txt*
4. Trabaja a partir de ahi.
```
#!/bin/bash

# Archivos
accessions="../DATOS/ACCESIONES/Accessions.txt"
busca="../DATOS/BASEDATOS_NAFTP/proka_nombre_accesion_ftp.txt"
guarda="../RESULTADOS/BUSQUEDAS/resultados_accesiones_buscadas.txt"

# Buscar y almacenar los resultados en el archivo
grep -F -f "$accessions" "$busca" > "$guarda"

# Mostrar archivo
head -n 5 "$guarda"
# Guarda la longitud de la cantidad de registros y ademas concatena todos losdatos de las FTP para manipularlas
longitud=$(wc -l < $guarda)
ftp=$(cut -f 3 $guarda)

# Elimina  el titulo de la columna extraida
puro=$(echo "$ftp" | awk 'NR>=2 && NR<=$longitud {print $1}')

# Manipula cada uno de los datos para hacerlos visibles a la descarga
echo "$puro" | sed -E "s/GCA/GCF/g" | sed -E "s/ftp:/http:/g" | sed -E "s/(GCF_(.*))/\1\/\1_genomic.fna.gz/g" > ../RESULTADOS/BUSQUEDAS/http_GCF.txt

# Guarda la direccion de donde estan las actuales HTTP que eran FTP. Asi como los muestra para ver que se cumplio el comando.
filtr="../RESULTADOS/BUSQUEDAS/http_GCF.txt"
http=$(cut -f 1 $filtr)
head -n 5 $filtr

# Entra a esta carpeta para depositar aqui las secuencias
cd ../RESULTADOS/GENOMAS

# Empezamos la descarga de cada unas de las accesiones.
n=1
for i in $http
do
        echo "$i"
        wget $i
done

# Muestra los datos extraidos.
ls ./
```
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
#### ***NO.5CODE <FIN>***
