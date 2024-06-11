# 19 de mayo del 2024
El dia de hoy, se establecio la funcion de la matriz de confusion y asi una forma de saber cuales cluster son importantes para haer las predicciones en python

```

# Importamos las librerias necesarias
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

###################### -- EXTRACCION DE LOS DATOS -- ######################
# Extraemos la data
rutamtz = r"Descargas_NCBI\CDHIT\MATRIXDATA\testpysh_pymatrizcdhit.csv"
matriz = pd.read_csv(rutamtz)

# Extremos la tabla de clasificacion
rutaclass = r"Descargas_NCBI\CDHIT\MATRIXDATA\classificacion_genomas.txt"
classificacion = pd.read_csv(rutaclass)

# Juntamos ambos archivos 
mtz_class_caracteres = pd.merge(matriz, classificacion, on='Genomas')
mtz_class_caracteres = mtz_class_caracteres[mtz_class_caracteres['Nicho'] != 'Unclassified']

###################### -- PREPARACION DE LOS DATOS -- ######################
### -- One-Hot Encoding -- ###
#dummies_specie = pd.get_dummies(mtz_class_caracteres["Specie"]) , dummies_specie
dummies_Genomas = pd.get_dummies(mtz_class_caracteres["Genomas"])
mtz_class_caracteres = pd.concat([mtz_class_caracteres.drop(columns=['Genomas', 'Specie']), dummies_Genomas], axis=1)

### -- Caracteristicas y Objetivos, y Convertir Datos en Arreglos -- ###
labels = np.array(mtz_class_caracteres["Nicho"])
la_enc = LabelEncoder()
encoded_labels = la_enc.fit_transform(labels)

mtz_class_caracteres = mtz_class_caracteres.drop("Nicho", axis=1)
mtz_class_caracteres_list = list(mtz_class_caracteres.columns)
mtz_class_caracteres = np.array(mtz_class_caracteres)

### -- Entrenamiento y comprobacion de conjuntos -- ###
train_mtz_class_caracteres, test_mtz_class_caracteres, train_labels, test_labels = train_test_split(mtz_class_caracteres, 
                                                                                                     encoded_labels, 
                                                                                                     test_size=0.20, 
                                                                                                     random_state=99)

print('Training Features Shape:', train_mtz_class_caracteres.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_mtz_class_caracteres.shape)
print('Testing Labels Shape:', test_labels.shape)

###################### -- ENTRENAMIENTO DEL MODELO -- ######################
rf = RandomForestRegressor(n_estimators=1000, random_state=7)
rf.fit(train_mtz_class_caracteres, train_labels)

###################### -- Caracteristicas que son importantes -- ######################
importancias = rf.feature_importances_
feature_importances = pd.DataFrame(importancias, index=mtz_class_caracteres_list, columns=['Importancia'])
feature_importances = feature_importances.sort_values(by='Importancia', ascending=False)

print(feature_importances)
primeros20 = feature_importances.iloc[:20]
## >>>>> Queda pendiente pero puede ser util <<<<< ##
#first_zero_label = feature_importances[feature_importances['Importancia'] == 0].index[0]
#rango_zero = feature_importances.index.get_loc(first_zero_label)
#max_index = len(feature_importances) - 1
#end_index = min(rango_zero + 10, max_index)
#subrango_feature_importances = feature_importances.iloc[:end_index + 1]
# Graficar el DataFrame con barras horizontales
#ax = subrango_feature_importances.plot(kind='bar')
#plt.title('Importancia de las características')
#plt.xlabel('Importancia')
#plt.ylabel('Características')
# Ajustar la rotación de las etiquetas del eje y
#plt.yticks(rotation=0)
# Mostrar la gráfica
#plt.show()
## >>>>> Queda pendiente pero puede ser util <<<<< ##
# -------------------------------------------------------------- #
primeros20.plot(kind='bar')
plt.title('Importancia de las características')
plt.xlabel('Importancia')
plt.ylabel('Características')
# Ajustar la rotación de las etiquetas del eje y
plt.yticks(rotation=0)
# Mostrar la gráfica
plt.show()
###################### -- Hacemos predicciones con el conjunto de prueba -- ######################
predictions = rf.predict(test_mtz_class_caracteres)

##################### -- Matriz de Confusion -- ######################
prediction_discrete = np.round(predictions).astype(int)
mc = confusion_matrix(test_labels, prediction_discrete)

##################### -- Visualizacion de la Matriz de Confusion -- ######################
vis = ConfusionMatrixDisplay(mc)
vis.plot()

##################### -- Exactitud Matriz de Confusion -- ######################
accuracy = accuracy_score(test_labels, prediction_discrete)
precision = precision_score(test_labels, prediction_discrete, average='weighted', zero_division=0)
recall = recall_score(test_labels, prediction_discrete, average='weighted', zero_division=0)
f1 = f1_score(test_labels, prediction_discrete, average='weighted', zero_division=0)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

```

# 25 de mayo del 2024
Se termino el script final para correr en el cluster y analizar las 3,894 secuencias de IMG, el cual esta a disposicion aqui https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/tree/main/Random%20Forest/DNA 

Con el ejecutador del script `runpygraphconfusion.sh` y el script de Python que hace el analisis `RandomForest.py`

# 26 de mayo del 2024
Termino el script y con resultados exitosos del analisis, lo cuales podemos contar con el grafico de importancia

![importancia_caracteristicas](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/cdb8415b-f616-4ab0-add6-e65a17365d68)

Y con una salida csv debido a que en el cluster no se tiene el paquete para visualizar la matriz de confusion

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/7636354b-e6a3-4cb0-b515-1493d7684957)

Pero con el script `dataframeconfusionTOgraph.py` Se pudo obtener el grafico de confusion de manera local.

![Confusion_graph](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/cad56c29-ed1d-40e4-a8f5-52220c7ee104)

# 27 de mayo del 2024
Se observo que genomas se encuntran en le cluster mas importante `Cluster 50634`, los cuales los observados son proteinas reductasas.

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/b41ae281-fb55-4e20-bc77-07b0684d433c)

# 6 de junio del 2024
Trabajando con el analisis en local, se agrego al codigo que pueda guardar la codificaicon de los nichos en numeros.

```
labels = np.array(mtz_class_caracteres["Nicho"])
la_enc = LabelEncoder()
encoded_labels = la_enc.fit_transform(labels)
######## Nuevo de aqui pa bajo ########
etiquetas = labels.reshape(1, -1)
codified =  encoded_labels.reshape(1, -1)

class_etiquetas = np.concatenate((etiquetas, codified)).T
print(class_etiquetas)
pd.DataFrame(class_etiquetas).drop_duplicates().to_csv("np_class_etiquetas.csv", index=False)
```
Se añadio modificaciones para el grafico de importancia, pero ahora tambien se agrego el grafico en version logaritmica

### Los primeros 100
```
importancias = rf.feature_importances_
feature_importances = pd.DataFrame(importancias, index=mtz_class_caracteres_list, columns=['Importancia'])
feature_importances = feature_importances.sort_values(by='Importancia', ascending=False)

print(feature_importances)
primeros100 = feature_importances.iloc[:100]
```
### Normal
```
plt.figure(figsize=(20, 12))
primeros100.plot(kind='bar')
plt.title('Importancia de las características')
plt.xlabel('Características')
plt.ylabel('Importancia')
# Ajustar la rotación de las etiquetas del eje y
plt.xticks(rotation=90, fontsize=3, fontweight='bold') 
# Ajustar el diseño para que no se recorten los elementos
plt.tight_layout()
# Guardar la gráfica como un archivo PNG
plt.savefig(rutaimportacara, format='png', dpi=300, bbox_inches='tight')
```
### Logartimica
```
# Configurar el tamaño de la figura (ancho, alto) en pulgadas (GRAFICO LOGARITMICA)
# Crear la figura con el tamaño especificado
plt.figure(figsize=(20, 12))

# Crear la gráfica de barras con el eje y en escala logarítmica
primeros100.plot(kind='bar', logy=True)  # Aquí se especifica que el eje y será logarítmico

# Título y etiquetas de los ejes
plt.title('Importancia de las características')
plt.xlabel('Características')
plt.ylabel('Importancia')

# Ajustar el tamaño de las etiquetas del eje x
plt.xticks(rotation=90, fontsize=3, fontweight='bold')  # Ajusta el tamaño de la fuente según tus necesidades

# Ajustar el diseño para que no se recorten los elementos
plt.tight_layout()

# Guardar la gráfica como un archivo PNG
plt.savefig(rutaimportacara2, format='png', dpi=300, bbox_inches='tight')

```
Falta poner las diferencias entre cada cateogoria
Usar los 100 primeros cluster y de los genomas que pertenecen a cada cluster. Cuantos pertenecen a hospederos y cuantos a ambiente como este primer ejemplo.
Lo hacemos desde la matriz de cdhit, nombrando con la columnas columnas necesarias y tomando solo los datos que tengan etiquetas diferentes a vacio. Realizamos el conteo.

# 8 de junio del 2024
Se plantea añadir mas codigo para realizar ahora la matriz reducida con los 100 clusters mas importantes y con los genomas usados para hacer las predicciones.

Tener los genomas con indices son muy utiles dibido que al extraer los nichos, podemos obtener un nuevo dataframe con los genomas a usar para las predicciones.
```
# Juntamos ambos archivos 
mtz_class_caracteres = pd.merge(matriz.sort_values(by='Genomas'), classificacion.sort_values(by='Genomas'), on='Genomas')
mtz_class_caracteres.set_index('Genomas', inplace=True) ####### Nueva linea #######
mtz_class_caracteres = mtz_class_caracteres[mtz_class_caracteres['Nicho'] != 'Unclassified']

mtz_idgen_nicho = pd.DataFrame(pd.Series(mtz_class_caracteres['Nicho'])) ####### Nueva linea ####### Debido a que se quitaron los genomas que no se requieren

matriz.sort_values(by='Genomas')
classificacion.sort_values(by='Genomas')
###################### -- PREPARACION DE LOS DATOS -- ######################
### -- One-Hot Encoding -- ###
mtz_class_caracteres = pd.concat([mtz_class_caracteres.drop(columns=['Specie'])], axis=1) 
```
Ya con la informacion de los nichos y los genomas usados, ahora se puede saber cuales son los genomas que pertenecen a cada cluster
```
###################### -- Caracteristicas que son importantes -- ######################
importancias = rf.feature_importances_
feature_importances = pd.DataFrame(importancias, index=mtz_class_caracteres_list, columns=['Importancia'])
feature_importances = feature_importances.sort_values(by='Importancia', ascending=False)

print(feature_importances)
primeros100 = feature_importances.iloc[:100]
###################### -- Nichos por Clusters -- ###################### ####### Nueva linea #######
print(primeros100)
#Tomamos los nombres de los clusters. ####### Nueva linea #######
cienclusters_importantes = " ".join(primeros100.index) ####### Nueva linea #######
# Como la matriz esta en un numpy array, ahora toca extraer por el numero de las columna. ####### Nueva linea #######
cienclusters_importantes = cienclusters_importantes.replace("Cluster", "").split(" ") ####### Nueva linea #######
# Nombramos las columnas que necesitamos ####### Nueva linea #######

# Simplificamos el for anterior ####### Nueva linea #######
clustercien = [mtz_class_caracteres[:,int(npcol)] for npcol in cienclusters_importantes if not npcol is None] ####### Nueva linea #######
mtz_clustercien = pd.DataFrame(np.array(clustercien).T, columns=cienclusters_importantes, index=mtz_idgen_nicho.index) ####### Nueva linea #######
# añadimos los nichos    ####### Nueva linea #######
mtz_clustercien['Nichos'] = mtz_idgen_nicho['Nicho'] ####### Nueva linea #######
# Se virifico que al ordenar los datos, se colocan correctamente sin incosistencias ####### Nueva linea #######
```

# 10 de junio del 2024

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/2b3bd46e-6204-4520-84c5-a74dad1d043d)
