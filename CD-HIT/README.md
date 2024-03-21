## Comprobacion de comandos y creacion de script para analizar todos los genomas de *Pseudomonas*

Como mencionaba en el Word "Bitacora"
Se genero un archivo con las 10 secuencias de distintas *Pseudomonas*

```
cat 2505313052/2505313052.genes.faa >> ./TODOS/protcat.faa
cat 2554235471/2554235471.genes.faa >> ./TODOS/protcat.faa
cat 2517572175/2517572175.genes.faa >> ./TODOS/protcat.faa
cat 2548876750/2548876750.genes.faa >> ./TODOS/protcat.faa
cat 2630968743/2630968743.genes.faa >> ./TODOS/protcat.faa
cat 2713896862/2713896862.genes.faa >> ./TODOS/protcat.faa
cat 2785510749/2785510749.genes.faa >> ./TODOS/protcat.faa
cat 2923166773/2923166773.genes.faa >> ./TODOS/protcat.faa
cat 2972001829/2972001829.genes.faa >> ./TODOS/protcat.faa
cat 8011072914/8011072914.genes.faa >> ./TODOS/protcat.faa
```
Y para ver cual es la diferencia entre el poder de computo:
```
cd-hit -i protcat.faa -o clusterprotcatALL -c 0.60 -n 4 -M 800 -d 0 -T 1
```
el resultado del primer comando es
```
================================================================
Program: CD-HIT, V4.8.1 (+OpenMP), Mar 22 2020, 15:35:52
Command: cd-hit -i protcat.faa -o clusterprotcatALL -c 0.60 -n
         4 -M 800 -d 0 -T 1

Started: Thu Mar 21 09:08:15 2024
================================================================
                            Output
----------------------------------------------------------------
total seq: 56287
longest and shortest : 6388 and 11
Total letters: 18315252
Sequences have been sorted

Approximated minimal memory consumption:
Sequence        : 25M
Buffer          : 1 X 12M = 12M
Table           : 1 X 4M = 4M
Miscellaneous   : 0M
Total           : 42M

Table limit with the given memory limit:
Max number of representatives: 1495683
Max number of word counting entries: 94674537

comparing sequences from          0  to      56287
..........    10000  finished       3146  clusters
..........    20000  finished       6175  clusters
..........    30000  finished       9289  clusters
..........    40000  finished      12489  clusters
..........    50000  finished      16167  clusters
......
    56287  finished      19001  clusters

Approximated maximum memory consumption: 89M
writing new database
writing clustering information
program completed !

Total CPU time 63.19
```
Y en tanto, cambiando la memoria y los nucleos, sale esto
```
cd-hit -i protcat.faa -o clusterprotcatALL2000 -c 0.60 -n 4 -M 2000 -d 0 -T 2
```

```
================================================================
Program: CD-HIT, V4.8.1 (+OpenMP), Mar 22 2020, 15:35:52
Command: cd-hit -i protcat.faa -o clusterprotcatALL2000 -c
         0.60 -n 4 -M 2000 -d 0 -T 2

Started: Thu Mar 21 09:17:25 2024
================================================================
                            Output
----------------------------------------------------------------
total seq: 56287
longest and shortest : 6388 and 11
Total letters: 18315252
Sequences have been sorted

Approximated minimal memory consumption:
Sequence        : 25M
Buffer          : 2 X 12M = 25M
Table           : 2 X 4M = 8M
Miscellaneous   : 0M
Total           : 59M

Table limit with the given memory limit:
Max number of representatives: 3832749
Max number of word counting entries: 242607326

# comparing sequences from          0  to      14071
..........    10000  finished       3146  clusters
....---------- new table with     4321 representatives
# comparing sequences from      14071  to      24625
..........    20000  finished       6175  clusters
99.9%---------- new table with     3332 representatives
# comparing sequences from      24625  to      32540
..........    30000  finished       9289  clusters
99.9%---------- new table with     2383 representatives
# comparing sequences from      32540  to      38476
99.9%---------- new table with     1884 representatives
# comparing sequences from      38476  to      42928
100.0%---------- new table with     1620 representatives
# comparing sequences from      42928  to      46267
99.9%---------- new table with     1164 representatives
# comparing sequences from      46267  to      48772
100.0%---------- new table with      979 representatives
# comparing sequences from      48772  to      50650
..........    50000  finished      16167  clusters
99.9%---------- new table with      742 representatives
# comparing sequences from      50650  to      52059
99.9%---------- new table with      567 representatives
# comparing sequences from      52059  to      53116
100.0%---------- new table with      443 representatives
# comparing sequences from      53116  to      53908
99.9%---------- new table with      373 representatives
# comparing sequences from      53908  to      54502
99.9%---------- new table with      273 representatives
# comparing sequences from      54502  to      54948
99.9%---------- new table with      212 representatives
# comparing sequences from      54948  to      55282
99.8%---------- new table with      144 representatives
# comparing sequences from      55282  to      55533
99.9%---------- new table with      132 representatives
# comparing sequences from      55533  to      56287
...................---------- new table with      432 representatives

    56287  finished      19001  clusters

Approximated maximum memory consumption: 91M
writing new database
writing clustering information
program completed !

Total CPU time 105.70
```
y los resultas aparentemente son muy similares, por lo que faltara revizar si el numero de clusters cambia o si hay algunas agrupaciones que cambien. Para ello se dejan los siguientes archivos ...






