# Aqui se anotan los errores vistos en la salida
Al abrir el archivo de entrada para la matriz `fast_matrizcdhit_inputmatrizcdhit.mtcdhit`, aparecen unos datos sin cluster concatenado

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/a7dd0bb1-4a72-42c1-b92b-6216d00667d1)

Y por otra parte, tenemos que al contar en el archivo `fast_matrizcdhit_genomasproteinas.idgidp`

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/7b0a4fe7-a384-4dff-930d-7fe97faaa12b)

son `22332436 fast_matrizcdhit_genomasproteinas.idgidp`

y del archivo madre incial, pero modificado con `Cluster [0-9]+` a  `Cluster[0-9]+` para este programa `fast_matrizcdhit_filtclstr.cdhitpy` son `grep -v -c "Cluster" fast_matrizcdhit_filtclstr.cdhitpy`: `22332430`

lo que son 6 accesiones menos usados, pero hace falta encontrar los que no fueron usados o encontrados o que incluso puede ser que no se haya hecho una buena busqueda al concatenar los genomas.

> Si bien encontramos que si se ordenaron correctamente las proteinas de manera correcta en el archivo `fast_matrizcdhit_concat.idgidpclustidp`

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/8db8fe94-715a-4214-b0ff-651cf57c2769)

con una cantidad de lineas `22332436`y que como podemos ver al hacer una busqueda

```
grep -E "^[0-9]+:[0-9]+\sClu" fast_matrizcdhit_concat.idgidpclustidp
```

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/89ce67d4-36d9-4870-a336-97b191b4a58c)

Si bien en el archvo concatendao, se encuentran los que quedaron solos, toca ver cuales de esos en los archivos originales aparecen en el formato `FASTA` o en el nombre de una proteina, para tener cuidado.
```
grep -E -v "^[0-9]+:[0-9]+\sClu" fast_matrizcdhit_concat.idgidpclustidp
```

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/0fa4ac81-c060-4dd2-9c82-7281cd2bc754)

Y como podemos ver de los que aparecen imparentados, si tienen pareja en CLuster, pero no estan ordenados, lo que quiere decir que hay datos que aparecen entre y hace que al final en el input de la matriz aparezcan los que no tienen pareja.

```
grep "8088481126" fast_matrizcdhit_concat.idgidpclustidp
```

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/296de4aa-5218-470d-bd81-d96dc91fd8ac)

```
grep "8088481120" fast_matrizcdhit_concat.idgidpclustidp
```

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/3cf76cd3-d631-4c75-bb6f-da88b930b61f)

Asi que en lo siguiente, toca ver cuales son esas accesiones que aparecen extra.

# 15 de mayo del 2024
El dia de hoy se retoma el problema sobre los id extras que hacen que no aparezcan correctamente ajustados con sus parejas.
Al parecer lo visto con los comandos
```
grep "8088474632" fast_matrizcdhit_concat.idgidpclustidp | less
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/a68ede92-5b25-4290-91e6-253194645521)

Y tambien 
```
grep "8088468458" fast_matrizcdhit_concat.idgidpclustidp | less
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/4f6ac4dc-4406-4987-a76f-91d2e41e430d)

```
grep "8088461797" fast_matrizcdhit_concat.idgidpclustidp | less
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/c782fcb8-04c9-4e94-ab13-a02145b75d37)

```
grep ":8088461797" fast_matrizcdhit_concat.idgidpclustidp | less
```

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/167043d3-5e99-453f-95f4-685334646606)

Y al suceder con el otro genoma
```
grep "8088455273" fast_matrizcdhit_concat.idgidpclustidp | less
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/19c68539-7679-4f3b-9989-7ceeaaebb6ee)

```
grep "8087728815" fast_matrizcdhit_concat.idgidpclustidp | less
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/cf378729-399b-4f79-b9d5-6f24ff4f8e6c)

Asi hasta llegar a este genoma, ya no se encontro mas genomas que sucedieran y se encontraran en otro. Pero aun asi, no se encuentra ordenado. Por lo que falta aun ver en que parte es donde no comienza a haber una congruencia con el orden.

> Por lo que toca ver dentro de los genomas si hay dichos ids de proteinas dentro.

Sin embargo antes se revisara en la extraccion de los `idgenomas:idproteinas` para verificar cuantos son 

Al explorar dentro de `fast_matrizcdhit_genomasproteinas.idgidp` se encuentra este primer id

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/d2441596-2a5c-419d-b6d7-163cd71e7106)

Pero al buscar el genoma `637000218` dentro de la carpeta `PSEUDOMONAS_GENOMAS` si se encontro. Y al abrir la carpeta con todos los genomas y aplicando un sort, resulta
```
ls PSEUDOMONAS_GENOMAS/ | sort -n | less
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/5c785c20-b613-4af9-8d17-aeda03ae9239)

Para ver en que parte empieza el desfase, se descargo `fast_matrizcdhit_concat.idgidpclustidp` para verlo en un gestor de texto como `sublime`. Mejor utilizamos el lector de texto por defecto de windows.

Se empezo a ver el desfase de los ids a partir del genoma `2506783016` y justo aqui

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/6329a1a7-96c5-476a-91c0-5c9d7c4d41a4)

A partir del 
```
2506783016:2506882742   Cluster27115:2506882744
```
en adelante, ahora buscamos tanto en los genomas
```
grep "2506882742" 2506783016/*faa
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/4c8e4886-e2ea-4d68-8a2e-e8bc5b97fb1e)

El cual si se encuentra en dicho genoma
Por otra parte en la concatenacion de los datos, archivo `psedomonasIMGconcatenados.genes.faa` 
```
grep "2506882742" psedomonasIMGconcatenados.genes.faa
```

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/909fd983-a201-4c29-aec4-b2d3051d02b2)

Ahora por otra parte al ser usado por `CD-HIT` en los resultados
```
grep "2506882742" pseudocluster
grep "2506882742" pseudocluster.clstr
```
No muestra nadaa

Por lo que al parecer quiere decir que no lo uso para hacer el clustering y que por tanto puede indicar que es importante hacer un pqueño filtrado en los datos de concatenacion `idgenoma:idproteina cluster:idproteina` para que todo vaya acorde.
Si para comprobar, ni en `fast_matrizcdhit_filtclstr.cdhitpy` y `fast_matrizcdhit_filtchangeformat.clustidp` se encuentra el `idproteina:2506882742` y por tanto queda agregar al codigo un pequeño filtrado.

Debido a esta incongruencia podemos ver que en la matriz por no tener correctos los ids, todo aparece en 0´s.

Incluyendo ademas en el archivo de entrada para realizar la matriz, encontramos la primera anomalia `fast_matrizcdhit_inputmatrizcdhit.mtcdhit`

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/b5e1c8e0-7a0f-428f-b55a-0f9abf85b393)


El cual no tiene union de cluster y para ello hacemos una busqueda rapida para ver que show
```
grep -E "^:[0-9]+:" fast_matrizcdhit_inputmatrizcdhit.mtcdhit
```
Solo es el unico que aparecio

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/0f5a1005-f719-4b58-ad7e-62aa157db8ec)

Como aparecio 6 veces al parecer, en la primera buscqueda en los resultados de `CD-HIT` del archivo `` aparece esto

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/a18507aa-5380-408c-a619-5096185c9a64)

Y al buscar dentro si habia mas coincidencias, solo se encontro esa.

# 16 de mayo del 2024
Se finalizo el filtrado sobre el desfase de `idgenoma:idproteina` con `Cluster[0-9]+:idproteina` con el script de python en base a bash
```
#!/bin/bash


python2 - << END

import re

with open('Pseudomonas/WORK/ANALYSIS_CDHIT/MATRIXCDHIT/fast_matrizcdhit_genomasproteinas.idgidp') as file:
        idgidp = file.read()
with open(Pseudomonas/WORK/ANALYSIS_CDHIT/MATRIXCDHIT/fast_matrizcdhit_filtchangeformat.clustidp') as file2:
        clustidp = file2.read()

idpgenomas = re.findall(r"(?<=:)(\d+)", idgidp)
cdhitidp = re.findall(r"Cluster\d+:(\d+)\n", clustidp)

print(len(idpgenomas), len(cdhitidp))

n = 0
m = 0
while n < len(cdhitidp):
        if idpgenomas[m] != cdhitidp[n]:
                print(idpgenomas.pop(m))
                if idpgenomas[m] == cdhitidp[n]:
                        print(idpgenomas[m] , cdhitidp[n])
                        m+=1
                        n+=1
        else:
                m+=1
                n+=1
print(len(idpgenomas), len(cdhitidp))
END

```

Con salida
```
(22332436, 22332430)
2506882742
('2506882744', '2506882744')
2508795298
('2508795299', '2508795299')
2511300800
('2511300801', '2511300801')
2511855715
('2511855716', '2511855716')
2549660264
('2549660265', '2549660265')
2597933538
('2597933539', '2597933539')
(22332430, 22332430)
```

Y finalmente le dimos la optimizacion al codigo para que pudiese hacer las evaluaciones, con un tiempo estimado de 23 segundos
```
#!/bin/bash


python2 - << END

import re

with open('Pseudomonas/WORK/ANALYSIS_CDHIT/MATRIXCDHIT/fast_matrizcdhit_genomasproteinas.idgidp') as file:
        idgidp = file.read()
lista1 = idgidp.split("\n")
with open('Pseudomonas/WORK/ANALYSIS_CDHIT/MATRIXCDHIT/fast_matrizcdhit_filtchangeformat.clustidp') as file2:
        clustidp = file2.read()

idpgenomas = re.findall(r"(?<=:)(\d+)", idgidp)
cdhitidp = re.findall(r"Cluster\d+:(\d+)\n", clustidp)

print("Si no concuerdan el numero de id's de proteinas de los extraidos en genomas: ", len(idpgenomas), "y los usados por CD-HIT", len(cdhitidp))
print("entonces ... ")

n = 0
while n < len(cdhitidp):
        if idpgenomas[n] != cdhitidp[n]:
                print("eliminamos idgenoma:idproteina", lista1.pop(n), "de la proteina", idpgenomas.pop(n))
                print("comprobamos que los siguientes esten correctos", "idgidp: ", idpgenomas[n], "cluster:idp: ", cdhitidp[n])
        else:
                n+=1

print("Esperando que salga el mismo numero de id de proteinas tanto de los genomas: ", len(idpgenomas), "como de los usados por CD-HIT: ", len(cdhitidp))
END
```
# 16 de mayo del 2024
```
#!/bin/bash


python2 - << END

import re

with open('/mnt/atgc-d2/sur/shared_data/Pseudomonas/WORK/ANALYSIS_CDHIT/MATRIXCDHIT/fast_matrizcdhit_genomasproteinas.idgidp') as file:
        idgidp = file.read()
lista1 = idgidp.split("\n")
with open('/mnt/atgc-d2/sur/shared_data/Pseudomonas/WORK/ANALYSIS_CDHIT/MATRIXCDHIT/fast_matrizcdhit_filtchangeformat.clustidp') as file2:
        clustidp = file2.read()

idpgenomas = re.findall(r"(?<=:)(\d+)", idgidp)
cdhitidp = re.findall(r"Cluster\d+:(\d+)\n", clustidp)

genomas = re.findall(r"(\d+):", idgidp)
cluster = re.findall(r"Cluster\d+", clustidp)

#print(genomas)


print("Si no concuerdan el numero de id's de proteinas de los extraidos en genomas: ", len(idpgenomas), "y los usados por CD-HIT", len(cdhitidp))
print("entonces ... ")
clustergenoma=[]
n = 0
while n < len(cdhitidp):
        if idpgenomas[n] != cdhitidp[n]:
                print("eliminamos idgenoma:idproteina", lista1.pop(n), "de la proteina", idpgenomas.pop(n))
                genomas.pop(n)
                print("comprobamos que los siguientes esten correctos", "idgidp: ", idpgenomas[n], "cluster:idp: ", cdhitidp[n])
        else:
                clustergenoma.append(str(cluster[n]) + ':' + str(genomas[n]))
                n+=1
#print(clustergenoma)
print("Esperando que salga el mismo numero de id de proteinas tanto de los genomas: ", len(idpgenomas), "como de los usados por CD-HIT: ", len(cdhitidp))
END
```


```
#!/bin/bash

# Antes creamos unas variables para introducirlas a codigo en PYTHON
# extraemos todos los Cluster[0-9]+
cols=$(grep "Cluster" Pseudomonas/WORK/ANALYSIS_CDHIT/MATRIXCDHIT/fast_matrizcdhit_filtclstr.cdhitpy)
echo $cols > "WORK/ANALYSIS_CDHIT/MATRIXCDHIT/tempclust.cluster"

# Extraemos todos los genomas que fueron usados.
filas=$(ls Pseudomonas/PSEUDOMONAS_GENOMAS/ | tr '\n' ' ')
echo -e "$filas" > "Pseudomonas/WORK/ANALYSIS_CDHIT/MATRIXCDHIT/tempgenomas.genomes"

python2 - << END

import re
import os
import pandas as pd
import sys

with open('Pseudomonas/WORK/ANALYSIS_CDHIT/MATRIXCDHIT/tempclust.cluster') as cl:
        cols = cl.read()
        cols = cols.split(' ')
#print(cols)

with open('Pseudomonas/WORK/ANALYSIS_CDHIT/MATRIXCDHIT/tempgenomas.genomes') as g:
        fl = g.read()
        fl = fl.split(' ')

#print(fl)

zerocdhit = pd.DataFrame(0, index=fl, columns=cols)
zerocdhit = zerocdhit.rename_axis("Genomas")

print(zerocdhit)

#from collections import Counter
with open('Pseudomonas/WORK/ANALYSIS_CDHIT/MATRIXCDHIT/fast_matrizcdhit_genomasproteinas.idgidp') as file:
        idgidp = file.read()
lista1 = idgidp.split("\n")
with open('WORK/ANALYSIS_CDHIT/MATRIXCDHIT/fast_matrizcdhit_filtchangeformat.clustidp') as file2:
        clustidp = file2.read()

idpgenomas = re.findall(r"(?<=:)(\d+)", idgidp)
cdhitidp = re.findall(r"Cluster\d+:(\d+)\n", clustidp)

genomas = re.findall(r"(\d+):", idgidp)
cluster = re.findall(r"Cluster\d+", clustidp)

#Creacion de la matriz

print("Si no concuerdan el numero de id's de proteinas de los extraidos en genomas: ", len(idpgenomas), "y los usados por CD-HIT", len(cdhitidp))
print("entonces ... ")
clustergenoma=[]
frecuencia={}
n = 0
while n < len(cdhitidp):
        if idpgenomas[n] != cdhitidp[n]:
                print("eliminamos idgenoma:idproteina", lista1.pop(n), "de la proteina", idpgenomas.pop(n))
                genomas.pop(n)
                print("comprobamos que los siguientes esten correctos", "idgidp: ", idpgenomas[n], "cluster:idp: ", cdhitidp[n])
        else:
                clustergenoma.append(str(cluster[n]) + ':' + str(genomas[n]))
                if clustergenoma[n] in frecuencia:
                        frecuencia[clustergenoma[n]] += 1
                else:
                        frecuencia[clustergenoma[n]] = 1
                coordenadas=clustergenoma[n].split(":")
                zerocdhit.at[ coordenadas[1], coordenadas[0] ] = frecuencia[clustergenoma[n]]
                n+=1

print("Esperando que salga el mismo numero de id de proteinas tanto de los genomas: ", len(idpgenomas), "como de los usados por CD-HIT: ", len(cdhitidp))
zerocdhit.to_csv("Pseudomonas/WORK/ANALYSIS_CDHIT/MATRIXCDHIT/tempfinalmtriz.mtz")

END
```




