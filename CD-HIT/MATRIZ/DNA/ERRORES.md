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








