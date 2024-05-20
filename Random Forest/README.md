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
