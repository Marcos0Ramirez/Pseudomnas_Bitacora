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









