# Aqui alojamos la informacion de comandos para ejecutar y usar en el cluster

Este es el script que se uso para concatenar las proteinas, anteriormente usado para correr CD-HIT
```
#!/bin/bash

PWD="/direccion/donde/esta/directorio/trabajo/Pseudomonas"

mostrarnomcarpeta=$(ls $PWD/PSEUDOMONAS_GENOMAS)

for i in $mostrarnomcarpeta; do cat $PWD/PSEUDOMONAS_GENOMAS/$i/$i.genes.faa >> $PWD/ANALYSIS_CDHIT/psedomonasIMGconcatenados.genes.faa; done

```
Se aplico el script siguiente para VSEARCH
```
#!/bin/bash

module load vsearch/2.27.0

PWDUNO="/direccion/donde/esta/directorio/trabajo/Pseudomonas/WORK/VSEARCH"
PWDDOS="/direccion/donde/esta/directorio/trabajo/Pseudomonas/WORK/VSEARCH/RESULTADOS/UNO"

nohup vsearch --cluster_fast $PWDUNO/ANALYSIS_CDHIT/psedomonasIMGconcatenados.genes.faa --id 0.6 --centroids $PWDDOS/pseudovsearch.centroids --clusterout_id --clusterout_sort --consout $PWDDOS/pseudovsearch.consout --msaout $PWDDOS/pseudovsearch.msout --uc $PWDDOS/pseudovsearch.uc &

module unload vsearch/2.27.0
```


Ahora que se usaron las proteinas con el archivo `.FAA`, no funciono y por tanto no concluyo bien el analisis
```
$ more nohup.out
vsearch v2.27.0_linux_x86_64, 62.7GB RAM, 16 cores
https://github.com/torognes/vsearch

Reading file /direccion/de/las/proteinas/concatenadas/ANALYSIS_CDHIT/psedomonasIMGconcatenados.genes.faa 100%
WARNING: 2521892444 invalid characters stripped from FASTA file: E(411793089) F(257792632) I(332125643) J(8) L(848263083) P(350392659) Q(321247361) X(277962) Z(7)
REMINDER: vsearch does not support amino acid sequences
4606402151 nt in 22032286 seqs, min 32, max 9769, avg 209
minseqlength 32: 300150 sequences discarded.
Masking 100%
Sorting by length 100%
Counting k-mers 100%
Clustering
```
Al parecer sigue clusterizando y por tanto, lo dejaremos ver que es lo que da de salida con las proteinas
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Ahora se modifico para concatenar las proteinas por DNA y que por tanto, nos da de salida el archivo con las secuencias de las proteinas en DNA
### Esto se hizo por el motivo de que al parecer VSEARCH, trabaja con secuencias de DNA/RNA, algo que es extraño porque al hacerlo en local en LENOVO, trabajo bien sin una salida como la anterior

Codigo para concatenar secuncias de ADN
```
#!/bin/bash

PWD="/mnt/atgc-d2/sur/shared_data/Pseudomonas"

mostrarnomcarpeta=$(ls $PWD/PSEUDOMONAS_GENOMAS)

for i in $mostrarnomcarpeta; do cat $PWD/PSEUDOMONAS_GENOMAS/$i/$i.genes.fna >> $PWD/WORK/VSEARCH/psedomonasIMGconcatenados.genes.fna; done
```

Ahora que se ejecuta el comando 
```
#!/bin/bash

module load vsearch/2.27.0

PWDUNO="/direccion/donde/esta/directorio/trabajo/Pseudomonas/WORK/VSEARCH"
PWDDOS="/direccion/donde/esta/directorio/trabajo/Pseudomonas/WORK/VSEARCH/RESULTADOS/DOS"

nohup vsearch --cluster_fast $PWDUNO/psedomonasIMGconcatenados.genes.fna --id 0.6 --centroids $PWDDOS/pseudovsearch.centroids --clusterout_id --clusterout_sort --consout $PWDDOS/pseudovsearch.consout --msaout $PWDDOS/pseudovsearch.msout --uc $PWDDOS/pseudovsearch.uc >> ../vsearchnohup.out &

module unload vsearch/2.27.0
```
Con una salida del archivo `vsearchnohup.out`
```
vsearch v2.27.0_linux_x86_64, 62.7GB RAM, 16 cores
https://github.com/torognes/vsearch

Reading file /direccion/de/las/proteinas/concatenadas/Pseudomonas/WORK/VSEARCH/psedomonasIMGconcatenados.genes.fna 100%
21578563956 nt in 22881644 seqs, min 33, max 43590, avg 943
minseqlength 32: 53 sequences discarded.
Masking 100%
Sorting by length 100%
Counting k-mers
```
