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
### ***NO.3CODE <INICIO>
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




#### ***NO.3CODE <INICIO>

