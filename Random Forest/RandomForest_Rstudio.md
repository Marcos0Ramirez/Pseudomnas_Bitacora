# Aqui anotamos en la bitacora como se puede aplicar Random Forest
## 5 de mayo del 2024
> Si para empezar, gracias a ChatGPT, podemos saber como son los comandos para aplicarlo a los datos, si bien tenemos la matriz falta terminar la tabla de clasficacion.

***Asi, para empezar consideramos el data set de 10 genomas con una clasificacion inventada o extraida de IMG database y aplicarla a lo que explico ChatGPT***

# Conversacion
---------------------------------------------------------------------------------------------------------------------------------------
### Yo
Si tengo una matriz de frecuencia en el numero de veces que aparece un genoma en cada cluster hecho en CD-HIT y la quiero usar para aplicar en random forest como lo aplicaria y para que serviria.
### ChatGPT
Para aplicar una matriz de frecuencia de genomas en un algoritmo de Random Forest, primero necesitarías tener tus datos preparados en un formato adecuado. Aquí hay un proceso general que podrías seguir:

Preparación de datos: Asegúrate de que tu matriz de frecuencia esté en un formato adecuado para el análisis. Cada fila de la matriz podría representar un genoma y cada columna podría representar un cluster. Los valores en la matriz serían las frecuencias de ocurrencia de cada genoma en cada cluster.
División de datos: Divide tus datos en un conjunto de entrenamiento y un conjunto de prueba. El conjunto de entrenamiento se utilizará para entrenar el modelo de Random Forest, mientras que el conjunto de prueba se utilizará para evaluar su rendimiento.
Entrenamiento del modelo de Random Forest: Utiliza la matriz de frecuencia como tus características (variables independientes) y etiquetas conocidas (si las tienes) como tus variables objetivo (variables dependientes) para entrenar el modelo de Random Forest.
Ajuste de hiperparámetros: Puedes ajustar los hiperparámetros del modelo de Random Forest para optimizar su rendimiento. Esto podría implicar ajustar el número de árboles en el bosque, la profundidad máxima de los árboles, etc.
Validación cruzada: Utiliza técnicas de validación cruzada para evaluar el rendimiento del modelo y asegurarte de que no esté sobreajustando los datos de entrenamiento.
Predicción en el conjunto de prueba: Una vez que hayas entrenado el modelo, utilízalo para hacer predicciones en el conjunto de prueba y evalúa su rendimiento utilizando métricas como precisión, recall, F1-score, etc.
Ahora, ¿para qué serviría usar un algoritmo de Random Forest con una matriz de frecuencia de genomas en clusters?

Clasificación de genomas: Podrías usar el modelo de Random Forest para clasificar genomas en diferentes clusters basados en su frecuencia de ocurrencia en esos clusters. Esto podría ayudar en la identificación de patrones o características distintivas de los genomas en diferentes grupos.
Predicción de pertenencia a clusters: Si tienes nuevas muestras de genomas y quieres predecir a qué cluster pertenecen, podrías usar el modelo entrenado para hacer esas predicciones. Esto podría ser útil en la clasificación de nuevos genomas en grupos predefinidos.
Análisis de similitud entre clusters: Al analizar la importancia de las características (genomas) en la predicción de los clusters, podrías obtener información sobre la similitud o diferencia entre los clusters en términos de composición genómica.
En resumen, aplicar un algoritmo de Random Forest a una matriz de frecuencia de genomas en clusters podría ayudarte a clasificar, predecir y analizar la composición genómica de diferentes grupos de manera eficaz.

### User
Como es el formato para introducir los datos en RandomForest en Rstudio?

2 / 2

### ChatGPT
En RStudio, puedes usar el paquete randomForest para entrenar un modelo de Random Forest. Para introducir los datos en el modelo, necesitarás tener tus datos preparados en un formato adecuado. Aquí hay un ejemplo de cómo podrías hacerlo:

Supongamos que tienes una matriz de frecuencia de genomas en clusters como esta:
```
# Ejemplo de matriz de frecuencia de genomas en clusters
          Cluster1 Cluster2 Cluster3
Genoma1        10        5        2
Genoma2         3        8        6
Genoma3         7        9        1
```
Para introducir estos datos en el modelo de Random Forest en RStudio, puedes seguir estos pasos:

Cargar los datos: Carga tus datos en RStudio desde un archivo CSV, Excel u otro formato que estés utilizando.
```
# Suponiendo que tus datos están en un archivo CSV llamado "datos.csv"
datos <- read.csv("datos.csv", header = TRUE)
```
Preparar los datos: Asegúrate de que tus datos estén en el formato adecuado para el análisis. En este caso, tu matriz de frecuencia de genomas en clusters ya está en el formato adecuado.
Entrenar el modelo de Random Forest:
```
library(randomForest)

# Suponiendo que la última columna de tus datos contiene la variable objetivo (si la tienes)
objetivo <- datos[, ncol(datos)]

# Las características son todas las columnas excepto la última
caracteristicas <- datos[, -ncol(datos)]

# Entrenar el modelo de Random Forest
modelo_rf <- randomForest(caracteristicas, objetivo)
```
Con estos pasos, has cargado tus datos, preparado tus características y etiquetas, y entrenado un modelo de Random Forest en RStudio.

Recuerda que este es solo un ejemplo básico. En un caso real, es posible que necesites realizar más pasos de preprocesamiento de datos, como manejar valores faltantes, escalar características, etc. Además, es importante ajustar los hiperparámetros del modelo de Random Forest para obtener los mejores resultados posibles.

### Yo
Ya entendi que significa esto, quiero agregarle un analisis de dos tablas, suponiendo que tengo la matriz como lo mencionaba antes y aparte una tabla en la que se clasifica cada genoma con que si es de un patogeno o de un organismo beneficioso o si vive en un hospedero o no.
### ChatGPT
Si deseas combinar la matriz de frecuencia de genomas en clusters con otra tabla que contiene información sobre la clasificación de cada genoma (por ejemplo, si es un patógeno, un organismo beneficioso, o si vive en un hospedero), puedes hacerlo mediante la unión de datos. Aquí te muestro cómo podrías hacerlo en RStudio:

Supongamos que tienes una matriz de frecuencia de genomas en clusters llamada `matriz_frecuencia` y una tabla adicional que contiene información de clasificación llamada `tabla_clasificacion`. Aquí está un ejemplo de cómo podrías combinarlos:
```
# Suponiendo que tienes una matriz de frecuencia de genomas en clusters
matriz_frecuencia <- read.csv("matriz_frecuencia.csv", header = TRUE)

# Suponiendo que tienes una tabla adicional con información de clasificación de genomas
tabla_clasificacion <- read.csv("tabla_clasificacion.csv", header = TRUE)

# Visualizar la matriz de frecuencia y la tabla de clasificación para entender su estructura
head(matriz_frecuencia)
head(tabla_clasificacion)

# Combinar la matriz de frecuencia con la tabla de clasificación basada en un identificador común (por ejemplo, el nombre del genoma)
datos_combinados <- merge(matriz_frecuencia, tabla_clasificacion, by = "Genoma")

# Verificar los datos combinados
head(datos_combinados)
```
En este código:

Primero, leemos las dos fuentes de datos (matriz_frecuencia.csv y tabla_clasificacion.csv) utilizando la función read.csv.
Luego, combinamos las dos fuentes de datos utilizando la función merge. Especificamos que queremos combinar las tablas basadas en el nombre del genoma, que suponemos es una columna común entre ambas.
Finalmente, verificamos los datos combinados para asegurarnos de que la combinación se haya realizado correctamente.
Después de combinar los datos, tendrás una tabla que contiene tanto la matriz de frecuencia de genomas en clusters como la información de clasificación para cada genoma. Luego puedes usar esta tabla combinada para entrenar tu modelo de Random Forest.


2 / 2

### User
Al usar esta funcion como podria quedar el formato?
datos_combinados <- merge(matriz_frecuencia, tabla_clasificacion, by = "Genoma")
### ChatGPT
Cuando utilizas la función merge() en R para combinar dos conjuntos de datos, el formato resultante de los datos combinados dependerá de cómo estén estructurados los conjuntos de datos originales y de la columna que utilices para fusionarlos.

En tu caso, supongamos que tienes una matriz de frecuencia de genomas en clusters como esta:
```
# Ejemplo de matriz de frecuencia de genomas en clusters
          Genoma Cluster1 Cluster2 Cluster3
1       Genoma1       10        5        2
2       Genoma2        3        8        6
3       Genoma3        7        9        1
```
Y supongamos que tienes una tabla adicional de clasificación de genomas como esta:
```
# Ejemplo de tabla de clasificación de genomas
          Genoma Clasificacion
1       Genoma1      Patógeno
2       Genoma2  Beneficioso
3       Genoma3     Hospedero
```
Cuando utilizas la función merge() de la siguiente manera:
```
datos_combinados <- merge(matriz_frecuencia, tabla_clasificacion, by = "Genoma")
```
El formato resultante de datos_combinados dependerá de si hay una o más columnas comunes entre las dos tablas que estás fusionando. En este caso, estamos fusionando las tablas por la columna "Genoma", que es común en ambas tablas.

El resultado de la fusión será una tabla que contiene todas las columnas de ambas tablas, con las filas combinadas basadas en los valores de la columna "Genoma". Algo así:
```
          Genoma Cluster1 Cluster2 Cluster3 Clasificacion
1       Genoma1       10        5        2      Patógeno
2       Genoma2        3        8        6  Beneficioso
3       Genoma3        7        9        1     Hospedero
```
En este ejemplo, la tabla datos_combinados tendrá las columnas de la matriz de frecuencia de genomas en clusters y la columna adicional de clasificación de genomas. Cada fila representará un genoma con su respectiva clasificación y frecuencia en cada cluster.

---------------------------------------------------------------------------------------------------------------------------------------
Pero el nivel de procesamiento en R, en mi computadora local es muy lento y por tanto se procedio a trabajar con python.
Continuando con lo demas, se hizo a mano la tabla de clasificacion.
```
Genomas,Nicho
2505313052,Patogeno
2517572175,HostHuman
2548876750,HostFungi
2554235471,Patogeno
2630968743,Ambiente
2713896862,Ambiente
2785510749,Hostalga
2923166773,Hostanimal
2972001829,Unclassified
8011072914,Unclassified
```
## 06 de abril del 2024
Y ahora vamos a hacer el codigo para correr randomforest, este script desarrollado con ChatGPT, se llama `RandomForest_pyscript.py`
```
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:21:40 2024

@author: 52477
"""

# Cargamos las librerias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Abrimos la matriz
rutamtz=r"C:\Users\52477\Desktop\Descargas_NCBI\CDHIT\MATRIXDATA\testpysh_pymatrizcdhit.csv"
matriz = pd.read_csv(rutamtz)

# Extremos la tabla de extraccion
rutaclass=r"C:\Users\52477\Desktop\Descargas_NCBI\CDHIT\MATRIXDATA\classificacion_genomas.txt"
classificacion = pd.read_csv(rutaclass)

# Juntamos ambos archivos 
mtz_class = pd.merge(matriz, classificacion, on='Genomas')
# Confirmamos que si se hayan juntado
mtz_class["Nicho"]

# Hablamos 
X = mtz_class.drop(['Genomas', 'Nicho'], axis=1)  # Elimina la columna de ID_genoma y la columna de clase
y = mtz_class['Nicho']  # La columna de clase es la etiqueta que queremos predecir


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Exactitud del modelo RandomForest:", accuracy)
```
Por aca se pone los resultados que aparecieron del codigo anterior
```

```

Se va a desarrollar tambien el script por medio de esta pagina https://towardsdatascience.com/random-forest-in-python-24d0893d51c0 

## 07 de mayo del 2024
Ahora que ya hemos aplicado estas partes del codigo, como resultado tenemos funcionando el comando para hacer la matriz
```
# Importamos las librerias necesarias
import pandas as pd

# Extraemos la data
rutamtz=r"Dir\Descargas_NCBI\CDHIT\MATRIXDATA\testpysh_pymatrizcdhit.csv"
matriz = pd.read_csv(rutamtz)

# Extremos la tabla de clasificacion
rutaclass=r"Dir\Descargas_NCBI\CDHIT\MATRIXDATA\classificacion_genomas.txt"
classificacion = pd.read_csv(rutaclass)

# Juntamos ambos archivos 
mtz_class = pd.merge(matriz, classificacion, on='Genomas')

# One-Hot Encoding
    # Aqui buscaremos una variable categorica, que pueda ayudar a hacer el One-Hot Encoding
mtz_class = pd.get_dummies(mtz_class)
```
Asi observadmos el resultado de las columnas nuevas
```
sub_mtz_class = mtz_class.iloc[:,19000:].head(5)
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/181dbbde-7a58-407d-bf51-4e365ae729df)

El codigo realizado hasta el dia de hoy, nombre del archivo `RandomForest_pagedevelop.py`
```
# Importamos las librerias necesarias
import pandas as pd
import numpy as np
###################### -- EXTRACCION DE LOS DATOS -- ######################
# Extraemos la data
rutamtz=r"Dir\Descargas_NCBI\CDHIT\MATRIXDATA\testpysh_pymatrizcdhit.csv"
matriz = pd.read_csv(rutamtz)

# Extremos la tabla de clasificacion
rutaclass=r"Dir\Descargas_NCBI\CDHIT\MATRIXDATA\classificacion_genomas.txt"
classificacion = pd.read_csv(rutaclass)

# Juntamos ambos archivos 
mtz_class = pd.merge(matriz, classificacion, on='Genomas')
sub1_mtz_class = mtz_class.iloc[:,19000:]





###################### -- PREPARACION DE LOS DATOS -- ######################
### -- One-Hot Encoding -- ###
    # Aqui buscaremos una variable categorica, que pueda ayudar a hacer el One-Hot Encoding
mtz_class = pd.get_dummies(mtz_class)
sub2_mtz_class = mtz_class.iloc[:,19000:]


### -- Caracteristicas y Objetivos, y Convertir Datos en Arreglos -- ###
# Pasamos a usar numpy
#### import numpy as np
# Cuales son las etiquetas que voy a predecir
labels = np.array(mtz_class.iloc[:,0:19001])
# Eliminamos la etiquetas de la matriz
# axis 1 se refiere a las columnas
mtz_class = mtz_class.drop(mtz_class.columns[1:19002], axis=1)
# Guardamos los cluster para su posterior uso
mtz_class_list = list(mtz_class.columns)
# Lo convertimos en arreglo de numpy
mtz_class = np.array(mtz_class)


### -- Entrenamiento y comprobacion de conjuntos -- ###
# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split
# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(mtz_class, labels, test_size = 0.25, random_state = 42)

print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)




###################### -- | -- ######################
```
## Extraccion de los datos.
1. matriz

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/d8e2cdca-5697-4674-ad97-6d292b82c47a)

---
2. Classificacion

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/6118cdfa-67cd-49e6-8aec-50b8bbc0f47b)

---
3. Unión

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/c2b44cc3-3b5e-454e-8432-2aacc62264a5)

---
a. Metadatos

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/61a7cbc6-7131-40ce-b624-c453ab3b4c40)

## PREPARACION DE LOS DATOS
### One-Hot Encoding

1. Reordenamiento

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/6104e20c-c085-46ee-a335-b5683acc1457)

---

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/755bd7ff-85bc-416b-9410-5d07f3368d45)

---
### Caracteristicas y Objetivos, y Convertir Datos en Arreglos

2. Etiquetas
labels = np.array(mtz_class.iloc[:,0:19001])

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/b659d1ba-cdda-4a38-8150-3070438ee818)

Con la correccion
labels = np.array(mtz_class.iloc[:,1:19002])

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/2378ab4a-a36b-4fff-beb9-0dd5d1797934)

---

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/f8dda5af-0f12-45c9-abc5-4c6ae1d24cf3)

Con la correccion

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/1302e27d-d4f0-408d-8805-756582a475bf)

---

3. Eliminacion

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/d3ec6b3f-9caa-424e-bee3-f2fef6f82fb0)

---

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/9483ec4d-460a-4296-b6ae-0a477c17b76e)

---

4. Lista

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/0c71fe29-c0af-421f-a6a0-404b5a588051)

---

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/770513b1-29cd-445c-ac55-e78c0718a40a)

---

5. Arreglo

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/9b45c14c-1c9b-402e-a813-0c941f403f21)

---

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/50871db0-46b8-479a-aed5-9770c0e21c5f)

---

### Entrenamiento y comprobacion de conjuntos



# 9 de mayo del 2024
Al parecer en la parte de errore, no funciona bien.
```
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 07:36:23 2024

@author: 52477
"""
# Importamos las librerias necesarias
import pandas as pd
import numpy as np
###################### -- EXTRACCION DE LOS DATOS -- ######################
# Extraemos la data
rutamtz=r"DirDescargas_NCBI\CDHIT\MATRIXDATA\testpysh_pymatrizcdhit.csv"
matriz = pd.read_csv(rutamtz)

# Extremos la tabla de clasificacion
rutaclass=r"Dir\Descargas_NCBI\CDHIT\MATRIXDATA\classificacion_genomas.txt"
classificacion = pd.read_csv(rutaclass)

# Juntamos ambos archivos 
mtz_class_caracteres = pd.merge(matriz, classificacion, on='Genomas')
sub1_mtz_class = mtz_class_caracteres.iloc[:,19000:]




###################### -- PREPARACION DE LOS DATOS -- ######################
### -- One-Hot Encoding -- ###
    # Aqui buscaremos una variable categorica, que pueda ayudar a hacer el One-Hot Encoding
dummies_specie = pd.get_dummies(mtz_class_caracteres["Specie"])
mtz_class_caracteres = pd.concat([mtz_class_caracteres.drop(columns=['Specie']), dummies_specie], axis=1)
sub2_mtz_class = mtz_class_caracteres.iloc[:,19000:]


### -- Caracteristicas y Objetivos, y Convertir Datos en Arreglos -- ###
# Pasamos a usar numpy
#### import numpy as np
# Cuales son las etiquetas que voy a predecir
labels = np.array(mtz_class_caracteres["Nicho"])
# Eliminamos la etiquetas de la matriz
# axis 1 se refiere a las columnas
mtz_class_caracteres = mtz_class_caracteres.drop("Nicho", axis=1)
sub3_mtz_class = mtz_class_caracteres.iloc[:,19000:]
# Guardamos los cluster para su posterior uso
mtz_class_caracteres_list = list(mtz_class_caracteres.columns)
# Lo convertimos en arreglo de numpy
mtz_class_caracteres = np.array(mtz_class_caracteres)


### -- Entrenamiento y comprobacion de conjuntos -- ###
# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split
# Split the data into training and testing sets
train_mtz_class_caracteres, test_mtz_class_caracteres, train_labels,  test_labels = train_test_split(mtz_class_caracteres, labels, test_size = 0.25, random_state = 42)

print('Training Features Shape:', train_mtz_class_caracteres.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_mtz_class_caracteres.shape)
print('Testing Labels Shape:', test_labels.shape)




###################### -- ESTABLECIMIENTO DE LINEA BASE -- ######################

# The baseline predictions are the historical averages
indices_caracteristicas = [mtz_class_caracteres_list.index(nombre) for nombre in mtz_class_caracteres_list[1:19002]]
baseline_preds = test_mtz_class_caracteres[:, indices_caracteristicas]
# Baseline errors, and display average baseline error
#baseline_errors = abs(baseline_preds - test_labels)
#print('Average baseline error: ', round(np.mean(baseline_errors), 2))






###################### -- | -- ######################
```


# 11 de mayo del 2024
Finalmente despues de probar y hacer modificaciones, la siguiente parte, se enfoco en solo ver que tanta precision partia al modificar diferentes variables.
```
import pandas as pd
import numpy as np
###################### -- EXTRACCION DE LOS DATOS -- ######################
# Extraemos la data
rutamtz=r"DirDescargas_NCBI\CDHIT\MATRIXDATA\testpysh_pymatrizcdhit.csv"
matriz = pd.read_csv(rutamtz)

# Extremos la tabla de clasificacion
rutaclass=r"Dir\Descargas_NCBI\CDHIT\MATRIXDATA\classificacion_genomas.txt"
classificacion = pd.read_csv(rutaclass)

# Juntamos ambos archivos 
mtz_class_caracteres = pd.merge(matriz, classificacion, on='Genomas')
sub1_mtz_class = mtz_class_caracteres.iloc[:,19000:]




###################### -- PREPARACION DE LOS DATOS -- ######################
### -- One-Hot Encoding -- ###
    # Aqui buscaremos una variable categorica, que pueda ayudar a hacer el One-Hot Encoding
dummies_specie = pd.get_dummies(mtz_class_caracteres["Specie"])
mtz_class_caracteres = pd.concat([mtz_class_caracteres.drop(columns=['Genomas', 'Specie']), dummies_specie], axis=1)
sub2_mtz_class = mtz_class_caracteres.iloc[:,19000:]


### -- Caracteristicas y Objetivos, y Convertir Datos en Arreglos -- ###
# Pasamos a usar numpy
#### import numpy as np


# Cuales son las etiquetas que voy a predecir
labels = np.array(mtz_class_caracteres["Nicho"])
# La columna Nicho, se traducira en numeros, para que el programa lo pueda leer.
encoded_labels, mapping_index = pd.factorize(labels)


# Eliminamos la etiquetas de la matriz
# axis 1 se refiere a las columnas
mtz_class_caracteres = mtz_class_caracteres.drop("Nicho", axis=1)
sub3_mtz_class = mtz_class_caracteres.iloc[:,19000:]
# Guardamos los cluster para su posterior uso
mtz_class_caracteres_list = list(mtz_class_caracteres.columns)
# Lo convertimos en arreglo de numpy
mtz_class_caracteres = np.array(mtz_class_caracteres)


### -- Entrenamiento y comprobacion de conjuntos -- ###
# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split
# Split the data into training and testing sets
train_mtz_class_caracteres, test_mtz_class_caracteres, train_labels,  test_labels = train_test_split(mtz_class_caracteres, encoded_labels, test_size = 0.50, random_state = 99)

print('Training Features Shape:', train_mtz_class_caracteres.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_mtz_class_caracteres.shape)
print('Testing Labels Shape:', test_labels.shape)




###################### -- ESTABLECIMIENTO DE LINEA BASE -- ######################

# The baseline predictions are the historical averages
indices_caracteristicas = [mtz_class_caracteres_list.index(nombre) for nombre in mtz_class_caracteres_list[1:19002]]
baseline_preds = test_mtz_class_caracteres[:, indices_caracteristicas]
# Baseline errors, and display average baseline error
#baseline_errors = abs(baseline_preds - test_labels)
#print('Average baseline error: ', round(np.mean(baseline_errors), 2))





###################### -- ENTRENAMIENTO DEL MODELO -- ######################

# Import the model we are using
from sklearn.ensemble import RandomForestRegressor
# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
# Train the model on training data
rf.fit(train_mtz_class_caracteres, train_labels);





###################### -- Hacemos predicciones con el conjunto de prueba -- ######################

# Use the forest's predict method on the test data
predictions = rf.predict(test_mtz_class_caracteres)
# Calculate the absolute errors
errors = abs(predictions - test_labels)
# Print out the mean absolute error (mae)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')




###################### -- Determinar métricas de rendimiento -- ######################
# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / test_labels)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')
```

En la cual al modficiar el `random_state` la precision de las predicciones puede aumentar mas o ser menos preciso.
Como podemos ver 
```
train_mtz_class_caracteres, test_mtz_class_caracteres, train_labels,  test_labels = train_test_split(mtz_class_caracteres, encoded_labels, test_size = 0.50, random_state = 99)
```
```
Training Features Shape: (5, 19009)
Training Labels Shape: (5,)
Testing Features Shape: (5, 19009)
Testing Labels Shape: (5,)
Mean Absolute Error: 1.8 degrees.
Accuracy: 50.55 %
```
errors
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/6c1f86e9-085a-43b3-bbd7-362c924d2920)

test_labels
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/3866c20f-f6a9-4676-a38c-e2f3bebe6207)

predictions
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/99f5d548-e74e-4f82-bcaa-b9208e53d936)

Y con otro valor de `random_state`
```
train_mtz_class_caracteres, test_mtz_class_caracteres, train_labels,  test_labels = train_test_split(mtz_class_caracteres, encoded_labels, test_size = 0.50, random_state = 81)
```
```
Training Features Shape: (5, 19009)
Training Labels Shape: (5,)
Testing Features Shape: (5, 19009)
Testing Labels Shape: (5,)
Mean Absolute Error: 2.01 degrees.
Accuracy: 49.34 %.
```
errors
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/448a8606-5905-47dc-a364-d9ea6bbe2bbd)

test_labels
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/03869224-6175-4331-9baf-c584331c1638)

predictions
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/17fc2d73-b7b0-4243-8740-88fe9bd008b1)


Y con otro valor de `random_state`
```
train_mtz_class_caracteres, test_mtz_class_caracteres, train_labels,  test_labels = train_test_split(mtz_class_caracteres, encoded_labels, test_size = 0.50, random_state = 42)
```
```
Training Features Shape: (5, 19009)
Training Labels Shape: (5,)
Testing Features Shape: (5, 19009)
Testing Labels Shape: (5,)
Mean Absolute Error: 1.88 degrees.
Accuracy: -inf %.
RuntimeWarning: divide by zero encountered in divide
  mape = 100 * (errors / test_labels)
```
errors
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/ac399686-fd05-46eb-bc0e-31be4b01e959)

test_labels
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/e1e9adc2-4c50-41ae-8331-1c43b7d196fa)

predictions
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/09b6a386-bd60-4e4a-b3fc-c5fa1bbf8c84)


Asi modificando partes del codigo, como por ejemplo tomar la configuracion mejor que se tuvo anteriormente y no eliminar la column de `Genomas`
```
dummies_Genomas = pd.get_dummies(mtz_class_caracteres["Genomas"])
mtz_class_caracteres = pd.concat([mtz_class_caracteres.drop(columns=['Genomas', 'Specie']), dummies_specie, dummies_Genomas], axis=1)

y

train_mtz_class_caracteres, test_mtz_class_caracteres, train_labels,  test_labels = train_test_split(mtz_class_caracteres, encoded_labels, test_size = 0.50, random_state = 99)

```
```
Training Features Shape: (5, 19019)
Training Labels Shape: (5,)
Testing Features Shape: (5, 19019)
Testing Labels Shape: (5,)
Mean Absolute Error: 1.83 degrees.
Accuracy: 50.09 %.
```


La siguiente pregunta, es como intrducir los datos de caracteres para que se puedan aplicar correctamente y tengan una mayor precision a la hora de hacer predicciones.

# 12 de abril del 2024
Por lo visto, del codigo anterior ya desarollado. Al modificar distintos parametros, encontramos una mejoria en la precision de las predicciones.

```
mtz_class_caracteres = pd.concat([mtz_class_caracteres.drop(columns=['Genomas', 'Specie']), dummies_specie, dummies_Genomas], axis=1)

train_mtz_class_caracteres, test_mtz_class_caracteres, train_labels,  test_labels = train_test_split(mtz_class_caracteres, encoded_labels, test_size = 0.30, random_state = 99999)

rf = RandomForestRegressor(n_estimators = 1000000, random_state = 1000000)
```
En `RandomForestRegressor` al ir aumentando el numero de estimaciones y de `random_state`. Se encontraban mayores porcentajes de precision, asi mismo al tomar mas cantidad de datos (`test_size` < 0.40) para hacer las precisiones, se obtenian resultados (Accuracy > 70%)

Si tan solo
```
train_test_split(test_size = 0.30, random_state = 99999)
RandomForestRegressor(n_estimators = 1x10^5, random_state = 1x10^5)
```
Resulto en 
```
Training Features Shape: (7, 19019)
Training Labels Shape: (7,)
Testing Features Shape: (3, 19019)
Testing Labels Shape: (3,)
Mean Absolute Error: 0.62 degrees.
Accuracy: 83.56 %.
```
Con un tiempo menor a 20 min
Y por otra parte
```
train_test_split(test_size = 0.30, random_state = 99999)
RandomForestRegressor(n_estimators = 1x10^6, random_state = 1x10^6)
```
Resulto en 
```
Training Features Shape: (7, 19019)
Training Labels Shape: (7,)
Testing Features Shape: (3, 19019)
Testing Labels Shape: (3,)
Mean Absolute Error: 0.62 degrees.
Accuracy: 83.59 %.
```
Con un tiempo de 2hrs aproximadas

# 19 de mayo del 2024
En el set de datos de prueba, se decidio probar con eliminar los dos genomas que no tenian clasificacion para ver como se comportaba y sorprendentemente, mejoro la prediccion. Modificacion...
```
# Juntamos ambos archivos 
mtz_class_caracteres = pd.merge(matriz, classificacion, on='Genomas')

mtz_class_caracteres = mtz_class_caracteres[mtz_class_caracteres['Nicho'] != 'Unclassified']
```
Codigo madre
```
import pandas as pd
import numpy as np
###################### -- EXTRACCION DE LOS DATOS -- ######################
# Extraemos la data
rutamtz=r"Descargas_NCBI\CDHIT\MATRIXDATA\testpysh_pymatrizcdhit.csv"
matriz = pd.read_csv(rutamtz)

# Extremos la tabla de clasificacion
rutaclass=r"Descargas_NCBI\CDHIT\MATRIXDATA\classificacion_genomas.txt"
classificacion = pd.read_csv(rutaclass)

# Juntamos ambos archivos 
mtz_class_caracteres = pd.merge(matriz, classificacion, on='Genomas')

mtz_class_caracteres = mtz_class_caracteres[mtz_class_caracteres['Nicho'] != 'Unclassified']

sub1_mtz_class = mtz_class_caracteres.iloc[:,19000:]




###################### -- PREPARACION DE LOS DATOS -- ######################
### -- One-Hot Encoding -- ###
    # Aqui buscaremos una variable categorica, que pueda ayudar a hacer el One-Hot Encoding
dummies_specie = pd.get_dummies(mtz_class_caracteres["Specie"])
dummies_Genomas = pd.get_dummies(mtz_class_caracteres["Genomas"])
mtz_class_caracteres = pd.concat([mtz_class_caracteres.drop(columns=['Genomas', 'Specie']), dummies_specie, dummies_Genomas], axis=1)
sub2_mtz_class = mtz_class_caracteres.iloc[:,19000:]


### -- Caracteristicas y Objetivos, y Convertir Datos en Arreglos -- ###
# Pasamos a usar numpy
#### import numpy as np


# Cuales son las etiquetas que voy a predecir
labels = np.array(mtz_class_caracteres["Nicho"])
# La columna Nicho, se traducira en numeros, para que el programa lo pueda leer.
# encoded_labels, mapping_index = pd.factorize(labels)
from sklearn.preprocessing import LabelEncoder
la_enc = LabelEncoder()
encoded_labels = la_enc.fit_transform(labels)


# Eliminamos la etiquetas de la matriz
# axis 1 se refiere a las columnas
mtz_class_caracteres = mtz_class_caracteres.drop("Nicho", axis=1)
sub3_mtz_class = mtz_class_caracteres.iloc[:,19000:]
# Guardamos los cluster para su posterior uso
mtz_class_caracteres_list = list(mtz_class_caracteres.columns)
# Lo convertimos en arreglo de numpy
mtz_class_caracteres = np.array(mtz_class_caracteres)


### -- Entrenamiento y comprobacion de conjuntos -- ###
# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split
# Split the data into training and testing sets
train_mtz_class_caracteres, test_mtz_class_caracteres, train_labels,  test_labels = train_test_split(mtz_class_caracteres, 
                                                                                                     encoded_labels, 
                                                                                                     test_size = 0.10, 
                                                                                                     random_state = 99)

print('Training Features Shape:', train_mtz_class_caracteres.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_mtz_class_caracteres.shape)
print('Testing Labels Shape:', test_labels.shape)




###################### -- ESTABLECIMIENTO DE LINEA BASE -- ######################

# The baseline predictions are the historical averages
indices_caracteristicas = [mtz_class_caracteres_list.index(nombre) for nombre in mtz_class_caracteres_list[1:19002]]
baseline_preds = test_mtz_class_caracteres[:, indices_caracteristicas]
# Baseline errors, and display average baseline error
#baseline_errors = abs(baseline_preds - test_labels)
#print('Average baseline error: ', round(np.mean(baseline_errors), 2))





###################### -- ENTRENAMIENTO DEL MODELO -- ######################

# Import the model we are using
from sklearn.ensemble import RandomForestRegressor
# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 1000, random_state = 99)
# Train the model on training data
rf.fit(train_mtz_class_caracteres, train_labels);





###################### -- Hacemos predicciones con el conjunto de prueba -- ######################

# Use the forest's predict method on the test data
predictions = rf.predict(test_mtz_class_caracteres)
# Calculate the absolute errors
#errors = abs(predictions - test_labels)
# Print out the mean absolute error (mae)
#print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')




###################### -- Determinar métricas de rendimiento -- ######################
# Calculate mean absolute percentage error (MAPE)
#mape = 100 * (errors / test_labels)
# Calculate and display accuracy
#accuracy = 100 - np.mean(mape)
#print('Accuracy:', round(accuracy, 2), '%.')


##################### -- Matriz de Confusion -- ######################
import sklearn.metrics
prediction_discrete = np.round(predictions).astype(int)
mc = sklearn.metrics.confusion_matrix(test_labels, prediction_discrete)

#print(type(test_labels))
#print(type(predictions))
#print(predictions.shape)

##################### -- Visualizacion de la Matriz de Confusion -- ######################


vis = sklearn.metrics.ConfusionMatrixDisplay(mc)
vis.plot()

##################### -- Exactitud Matriz de Confusion -- ######################
sklearn.metrics.accuracy_score(test_labels, prediction_discrete)

#sklearn.metrics.precision_score(test_labels, prediction_discrete)

#sklearn.metrics.recall_score(test_labels, prediction_discrete)

```

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/52b8f1b3-278d-4376-9509-bca1b24ec820)

Por otra parte al modiicar el codigo madre en esta parte
```
train_mtz_class_caracteres, test_mtz_class_caracteres, train_labels,  test_labels = train_test_split(mtz_class_caracteres, 
                                                                                                     encoded_labels, 
                                                                                                     test_size = 0.20, 
                                                                                                     random_state = 99)
```
