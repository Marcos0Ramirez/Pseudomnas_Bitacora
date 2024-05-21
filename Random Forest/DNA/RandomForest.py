# Importamos las librerias necesarias
import time
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
start_time = time.time()
###################### -- EXTRACCION DE LOS DATOS -- ######################

rutabase= "C:/Users/52477/Desktop/Descargas_NCBI/CDHIT/MATRIXDATA" # Ruta base
filemtz = "testpysh_pymatrizcdhit.csv" #Nombre del archivo con la matriz
fileclass = "classificacion_genomas.txt" # Nombre de la tabla de clasificacion

rutamtz = os.path.join(rutabase, filemtz)
rutaclass = os.path.join(rutabase, fileclass)

imgrutabase = "C:/Users/52477/Desktop/Descargas_NCBI/CDHIT/MATRIXDATA/Imagenes/"
imgic = "importancia_caracteristicas.png"
imgcm = "confusion_matrix.png"

rutaimportacara = os.path.join(imgrutabase, imgic)
rutaconfusion = os.path.join(imgrutabase, imgcm)
# Extraemos la data
matriz = pd.read_csv(rutamtz)

# Extremos la tabla de clasificacion

classificacion = pd.read_csv(rutaclass)

# Juntamos ambos archivos 
mtz_class_caracteres = pd.merge(matriz, classificacion, on='Genomas')
mtz_class_caracteres = mtz_class_caracteres[mtz_class_caracteres['Nicho'] != 'Unclassified']

###################### -- PREPARACION DE LOS DATOS -- ######################
### -- One-Hot Encoding -- ###
mtz_class_caracteres = pd.concat([mtz_class_caracteres.drop(columns=['Genomas', 'Specie'])], axis=1) 

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
feature_names = [f"feature {i}" for i in range(mtz_class_caracteres.shape[1])]
rf = RandomForestRegressor(n_estimators=1000, random_state=7)
rf.fit(train_mtz_class_caracteres, train_labels)

###################### -- Caracteristicas que son importantes -- ######################
importancias = rf.feature_importances_
feature_importances = pd.DataFrame(importancias, index=mtz_class_caracteres_list, columns=['Importancia'])
feature_importances = feature_importances.sort_values(by='Importancia', ascending=False)

print(feature_importances)
primeros20 = feature_importances.iloc[:20]

# Configurar el tamaño de la figura (ancho, alto) en pulgadas
plt.figure(figsize=(20, 12))
primeros20.plot(kind='bar')
plt.title('Importancia de las características')
plt.xlabel('Importancia')
plt.ylabel('Características')
# Ajustar la rotación de las etiquetas del eje y
plt.yticks(rotation=0)
# Ajustar el diseño para que no se recorten los elementos
plt.tight_layout()
# Guardar la gráfica como un archivo PNG
plt.savefig(rutaimportacara, format='png', dpi=300, bbox_inches='tight')
###################### -- Hacemos predicciones con el conjunto de prueba -- ######################
predictions = rf.predict(test_mtz_class_caracteres)

##################### -- Matriz de Confusion -- ######################
prediction_discrete = np.round(predictions).astype(int)
mc = confusion_matrix(test_labels, prediction_discrete)

##################### -- Visualizacion de la Matriz de Confusion -- ######################
vis = ConfusionMatrixDisplay(mc)
# Crear la visualización de la matriz de confusión
vis.plot()
# Ajustar el diseño para que no se recorten los elementos
plt.tight_layout()
# Guardar la gráfica como un archivo PNG con el tamaño y resolución especificados
plt.savefig(rutaconfusion, format='png', dpi=300, bbox_inches='tight')
##################### -- Exactitud Matriz de Confusion -- ######################
accuracy = accuracy_score(test_labels, prediction_discrete)
precision = precision_score(test_labels, prediction_discrete, average='weighted', zero_division=0)
recall = recall_score(test_labels, prediction_discrete, average='weighted', zero_division=0)
f1 = f1_score(test_labels, prediction_discrete, average='weighted', zero_division=0)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
elapsed_time = time.time() - start_time
print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")
