# Manejo de datos local, para analizarlos
Para el dia 22 de marzo del 2024
se utilizo el comando siguiente
```
vsearch --cluster_fast ../../CDHIT/TODOS/fromscriptall.genes.faa --id 0.6 --centroids vsearPseudo.faa --clusterout_id --clusterout_sort --uc PseudoPrueba.uc
```
los cuales describen estas acciones
```
vsearch           | Llamar el programa para ejecutarlo
--cluster_fast    | Usa el archivo 'fromscriptall.genes.faa', donde estan las proteinas de cada organismo concatenadas en formato fasta, para finalmente clusterizar las proteinas por orden de longitud de las secuencias.
--id              | Aqui se puede especificar cual es la identidad minima por la cual se van a agrupar las proteinas para generar los clusters.
--centroids       | Especifica las secuencias centrales por las cuales se ocuparon para agrupar las demas.
--clusterout_id   | En el archivo de salida indicado por '--consout' agrega un id de agrupacion y a los archivos de perfil
--clusterout_sort | Ordena el perfil por abundancia de 'decr' en los archivos de salida indicados por los comnados '--msaout' y '--consout'
--uc              | Especifica el nombre del archivo de salida como lo haria el programa de tipo UCLUST (por similitud de las secuencias)
```
De lo anterior:
```
Como extra
--consout         | Exporta un archivo con las secuencias consenso para la agrupacion, en un archivo FASTA
--msout           | Exporta alineamientos multiples en un archivo FASTA
```
