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
















