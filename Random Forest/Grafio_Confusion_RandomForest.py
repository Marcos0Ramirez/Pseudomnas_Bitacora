# -*- coding: utf-8 -*-
"""
Created on Sun May 19 16:28:43 2024

@author: 52477
"""

# Importamos las librerias necesarias
import time
import pandas as pd
import numpy as np
import os
import re
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
start_time = time.time()
###################### -- EXTRACCION DE LOS DATOS -- ######################

rutabase= "Descargas_NCBI/CDHIT/MATRIXDATA" # Ruta base
filemtz = "testpysh_pymatrizcdhit.csv" #Nombre del archivo con la matriz
fileclass = "classificacion_genomas.txt" # Nombre de la tabla de clasificacion

rutamtz = os.path.join(rutabase, filemtz)
rutaclass = os.path.join(rutabase, fileclass)

imgrutabase = "Descargas_NCBI/CDHIT/MATRIXDATA/Imagenes/"
imgic = "importancia_caracteristicas.png"
imgic2 = "importancia_caracteristicas_log.png"
mtzconfusion = "confusion_matrix.csv"
mtzconfusion2 = "confusion_matrix.png"
histo="histograma_tlabels.png"
histom="histograma_mlabels.png"
histompy2="histograma_mlabels_encoded.png"

rutaimportacara = os.path.join(imgrutabase, imgic)
rutaimportacara2 = os.path.join(imgrutabase, imgic2)
rutaconfusion = os.path.join(imgrutabase, mtzconfusion)
rutaconfusionpng = os.path.join(imgrutabase, mtzconfusion2)
histlabelspng = os.path.join(imgrutabase, histo)
histmlabelspng = os.path.join(imgrutabase, histom)
histmlabelspng_encoded = os.path.join(imgrutabase, histompy2)
# Extraemos la data
matriz = pd.read_csv(rutamtz)
print(matriz)
matriz = matriz.rename_axis("HOLA")
# Extremos la tabla de clasificacion

classificacion = pd.read_csv(rutaclass)

#matriz.drop([1,2,6,7]).to_csv("reduced_testpysh_pymatrizcdhit.csv", index=False)
#classificacion.drop([1,2,6,7]).drop('Specie', axis=1).to_csv("reduced_classificacion_genomas.txt", index=False, sep="\t")


# Juntamos ambos archivos 
mtz_class_caracteres = pd.merge(matriz.sort_values(by='Genomas'), classificacion.sort_values(by='Genomas'), on='Genomas')
mtz_class_caracteres.set_index('Genomas', inplace=True)
mtz_class_caracteres = mtz_class_caracteres[mtz_class_caracteres['Nicho'] != 'Unclassified']

#############################################################################################
mtz_idgen_nicho = pd.DataFrame(pd.Series(mtz_class_caracteres['Nicho']))
#############################################################################################

#matriz.sort_values(by='Genomas')
#classificacion.sort_values(by='Genomas')
###################### -- PREPARACION DE LOS DATOS -- ######################
### -- One-Hot Encoding -- ###
mtz_class_caracteres = pd.concat([mtz_class_caracteres.drop(columns=['Specie'])], axis=1) 

### -- Caracteristicas y Objetivos, y Convertir Datos en Arreglos -- ###
labels = np.array(mtz_class_caracteres["Nicho"])
la_enc = LabelEncoder()
encoded_labels = la_enc.fit_transform(labels)

etiquetas = labels.reshape(1, -1)
codified =  encoded_labels.reshape(1, -1)

class_etiquetas = np.concatenate((etiquetas, codified)).T
print(class_etiquetas)
pd.DataFrame(class_etiquetas).drop_duplicates().to_csv("np_class_etiquetas.csv", index=False)
list(pd.DataFrame(class_etiquetas).drop_duplicates()[1])
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
primeros100 = feature_importances.iloc[:100]
###################### -- Nichos por Clusters -- ######################
print(primeros100)
#Tomamos los nombres de los clusters.
cienclusters_importantes = " ".join(primeros100.index)
# Como la matriz esta en un numpy array, ahora toca extraer por el numero de las columna.
cienclusters_importantes = cienclusters_importantes.replace("Cluster", "").split(" ")
# Nombramos las columnas que necesitamos
    # Con una tupla los concatenamos
# =============================================================================
# clustercien = []
# for npcol in cienclusters_importantes:
#     clustercien.append(mtz_class_caracteres[:,int(npcol)])
# =============================================================================

# Simplificamos el for anterior
clustercien = [mtz_class_caracteres[:,int(npcol)] for npcol in cienclusters_importantes if not npcol is None]
mtz_clustercien = pd.DataFrame(np.array(clustercien).T, columns=cienclusters_importantes, index=mtz_idgen_nicho.index)
# añadimos los nichos   
mtz_clustercien['Nicho'] = mtz_idgen_nicho['Nicho']
# Se virifico que al ordenar los datos, se colocan correctamente sin incosistencias

###################### -- Hacemos el conteo -- ######################
# Tabla que tiene los datos mtz_idgen_nicho
#print(mtz_clustercien.at[2505313052, '1723'])
#list(mtz_clustercien.index[mtz_clustercien['Nicho'] == 'Patogeno'])
# u = mtz_idgen_nicho["Nicho"].unique()
# c =list(mtz_clustercien.columns)
# del c[c.index('Nicho')]


# #Creamos una matriz
# zeroconteonichos = pd.DataFrame(0, index=u, columns=c)
# # =============================================================================
# # for i in c:
# #     for j in u:
# #         ev = list(mtz_clustercien.index[mtz_clustercien['Nicho'] == j])
# #         print(mtz_clustercien.loc[ev,i])
# #         print(sum(list(mtz_clustercien.loc[ev,i])))
# # =============================================================================
# for i in u:
#     for j in c:
#         ev = list(mtz_clustercien.index[mtz_clustercien['Nicho'] == i])
#         #print(mtz_clustercien.loc[ev,j])
#         #print(sum(list(mtz_clustercien.loc[ev,j])))
#         zeroconteonichos.loc[i,j] = int(sum(list(mtz_clustercien.loc[ev,j])))
        #zeroconteonichos.loc['Patogeno','1723']
        
#        sum(list(mtz_clustercien.loc[list(mtz_clustercien.index[mtz_clustercien['Nicho'] == i]),j]))
#int(sum(list(mtz_clustercien.loc[list(mtz_clustercien.index[mtz_clustercien['Nicho'] == i]),j])) for i in u if not i is None for j in c if not j is None)
#zeroconteonichos.loc[i,j] = "".join([int(sum(list(mtz_clustercien.loc[list(mtz_clustercien.index[mtz_clustercien['Nicho'] == i]),j]))) for i in u if not i is None for j in c if not j is None])


# --------- Trabajo en limpio de la matriz ------------#
u = mtz_idgen_nicho["Nicho"].unique()
c =list(mtz_clustercien.columns)
del c[c.index('Nicho')]
#Creamos una matriz
zeroconteonichos = pd.DataFrame(0, index=u, columns=c)
for i in u:
    for j in c:
        ev = list(mtz_clustercien.index[mtz_clustercien['Nicho'] == i])
        zeroconteonichos.loc[i,j] = int(sum(list(mtz_clustercien.loc[ev,j])))
      
#############################################################################################
mtz_idgen_nicho_encoded = pd.DataFrame(pd.Series(mtz_idgen_nicho['Nicho']))
mtz_idgen_nicho_encoded["Nicho"] = encoded_labels
#############################################################################################
mtz_clustercien_encod = pd.DataFrame(np.array(clustercien).T, columns=cienclusters_importantes, index=mtz_idgen_nicho_encoded.index)
# añadimos los nichos   
mtz_clustercien_encod['Nicho'] = mtz_idgen_nicho_encoded['Nicho']

u_encoded = mtz_idgen_nicho_encoded["Nicho"].unique()
c =list(mtz_clustercien_encod.columns)
del c[c.index('Nicho')]
#Creamos una matriz
zeroconteonichos_encoded = pd.DataFrame(0, index=u_encoded, columns=c)
zeroconteonichos_encoded2 = pd.DataFrame(0, index=u_encoded, columns=c)

# =============================================================================
# for i in u_encoded:
#     for j in c:
#         ev = list(mtz_clustercien_encod.index[mtz_clustercien_encod['Nicho'] == i])
#         zeroconteonichos_encoded.loc[i,j] = int(sum(list(mtz_clustercien_encod.loc[ev,j])))
# =============================================================================

for i in u_encoded:
    for j in c:
        #print(i, j)
        #sys.stdout.flush()
        ev = list(mtz_clustercien_encod.index[mtz_clustercien_encod['Nicho'] == i])
        #print(ev)
        #sys.stdout.flush()
        # Asegúrate de que todos los elementos sean enteros
        values_to_sum = list(mtz_clustercien_encod.loc[ev, j])
        #print("Valores a sumar (antes de convertir):", values_to_sum)
        #sys.stdout.flush()
        values_to_sum = map(int, values_to_sum)
        #print("Valores a sumar (después de convertir):", values_to_sum)
        #sys.stdout.flush()
        sumas = sum(values_to_sum)
        #print("sumas: ", sumas)
        #sys.stdout.flush()
        zeroconteonichos_encoded.loc[i, j] = sumas
        #print("zeroconteonichos.loc[i,j]", zeroconteonichos.loc[i, j])
        #sys.stdout.flush()


##### Continuamos con el histograma. ######

# # =============================================================================
# =============================================================================
# OPCION 9
# MUCHOS HISTOGRAMAS

# Número total de clústeres
num_clusters = zeroconteonichos.shape[1]

# Dividir en grupos de 25 clústeres
clusters_per_image = 25
num_images = num_clusters // clusters_per_image

# Lista de colores para los histogramas
colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightpink']

for img in range(num_images):
    histom=f"histograma_mlabels_{img+1}.png"
    histmlabelspng = os.path.join(imgrutabase, histom)
    start_idx = img * clusters_per_image
    end_idx = start_idx + clusters_per_image
    clusters_subset = zeroconteonichos.columns[start_idx:end_idx]
    
    # Crear subplots: número de filas y columnas
    num_cols = 5  # Número de columnas deseadas en el grid
    num_rows = (clusters_per_image + num_cols - 1) // num_cols  # Calcular el número de filas

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(25, num_rows * 5), sharex=True, sharey=True)
    axes = axes.flatten()

    for i, cluster in enumerate(clusters_subset):
        print(i, cluster)
        axes[i].bar(zeroconteonichos.index, zeroconteonichos[cluster], color=colors[i % len(colors)])
        axes[i].set_title(cluster, fontsize=20)
        axes[i].tick_params(axis='x', rotation=90, labelsize=20)  # Aumentar tamaño de fuente de los números del eje x
        axes[i].tick_params(axis='y', labelsize=25)  # Aumentar tamaño de fuente de los números del eje y

    # Remover ejes adicionales en caso de que existan
    for i in range(len(clusters_subset), len(axes)):
        fig.delaxes(axes[i])

    # Solo una etiqueta de eje y
    fig.text(0.01, 0.5, 'Frecuencia', va='center', ha='center', rotation='vertical', fontsize=26)

    # Solo una etiqueta de eje x
    fig.text(0.5, 0.001, 'Característica', va='center', ha='center', fontsize=26)
    
    # Ajustar las etiquetas de las características
    plt.setp(axes, xticks=range(len(zeroconteonichos.index)), xticklabels=zeroconteonichos.index)

    # Añadir un título general
    fig.suptitle(f'Histograma {img + 1}', fontsize=30)
    # Ajusta los márgenes de la figura
    plt.subplots_adjust(left=0.05, right=0.9, top=0.95, bottom=0.1)

    #plt.show()
    # Ajustar el diseño para que no se recorten los elementos
    #plt.tight_layout()
    # Guardar la gráfica como un archivo PNG
    plt.savefig(histmlabelspng, format='png', dpi=300, bbox_inches='tight')
    plt.close(fig) 
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# OPCION 9  Para python 2
# MUCHOS HISTOGRAMAS

# Número total de clústeres
num_clusters = zeroconteonichos_encoded.shape[1]

# Dividir en grupos de 25 clústeres
clusters_per_image = 25
num_images = num_clusters // clusters_per_image

# Lista de colores para los histogramas
colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightpink']

for img in range(num_images):
    histompy2=f"histograma_mlabels_encoded2_{img+1}.png"
    histmlabelspng_encoded = os.path.join(imgrutabase, histompy2)
    start_idx = img * clusters_per_image
    end_idx = start_idx + clusters_per_image
    clusters_subset = zeroconteonichos_encoded.columns[start_idx:end_idx]
    
    # Crear subplots: número de filas y columnas
    num_cols = 5  # Número de columnas deseadas en el grid
    num_rows = (clusters_per_image + num_cols - 1) // num_cols  # Calcular el número de filas

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(25, num_rows * 5), sharex=True, sharey=True)
    axes = axes.flatten()
    
    for i, cluster in enumerate(clusters_subset):
        print(i, cluster)
        axes[i].bar(sorted(list(zeroconteonichos_encoded.index)), zeroconteonichos_encoded[cluster], color=colors[i % len(colors)])
        axes[i].set_title(cluster, fontsize=20)
        axes[i].tick_params(axis='x', rotation=90, labelsize=20)  # Aumentar tamaño de fuente de los números del eje x
        axes[i].tick_params(axis='y', labelsize=25)  # Aumentar tamaño de fuente de los números del eje y

    # Remover ejes adicionales en caso de que existan
    for i in range(len(clusters_subset), len(axes)):
        fig.delaxes(axes[i])

    # Solo una etiqueta de eje y
    fig.text(0.01, 0.5, 'Frecuencia', va='center', ha='center', rotation='vertical', fontsize=26)

    # Solo una etiqueta de eje x
    fig.text(0.5, 0.001, 'Característica', va='center', ha='center', fontsize=26)
    
    # Ajustar las etiquetas de las características
    plt.setp(axes, xticks=range(len(zeroconteonichos_encoded.index)), xticklabels=zeroconteonichos_encoded.index)

    # Añadir un título general
    fig.suptitle(f'Histograma_encoded {img + 1}', fontsize=30)
    # Ajusta los márgenes de la figura
    plt.subplots_adjust(left=0.05, right=0.9, top=0.95, bottom=0.1)

    #plt.show()
    # Ajustar el diseño para que no se recorten los elementos
    #plt.tight_layout()
    # Guardar la gráfica como un archivo PNG
    plt.savefig(histmlabelspng_encoded, format='png', dpi=300, bbox_inches='tight')
    plt.close(fig) 
# =============================================================================
# =============================================================================
# # OPCION 10
# # MUCHOS HISTOGRAMAS (dos filas)
# zeroconteonichos2 = pd.concat([zeroconteonichos.drop(['HostHuman', "HostFungi", "Hostalga", "Hostanimal"])], axis=0) 
# # Número total de clústeres
# num_clusters = zeroconteonichos2.shape[1]

# # Dividir en grupos de 25 clústeres
# clusters_per_image = 100
# num_images = num_clusters // clusters_per_image

# for img in range(num_images):
#     start_idx = img * clusters_per_image
#     end_idx = start_idx + clusters_per_image
#     clusters_subset = zeroconteonichos2.columns[start_idx:end_idx]
    
#     # Crear subplots: número de filas y columnas
#     num_cols = 10  # Número de columnas deseadas en el grid
#     num_rows = (clusters_per_image + num_cols - 1) // num_cols  # Calcular el número de filas

#     fig, axes = plt.subplots(num_rows, num_cols, figsize=(50, num_rows * 10), sharex=True, sharey=True)
#     axes = axes.flatten()

#     for i, cluster in enumerate(clusters_subset):
#         axes[i].bar(zeroconteonichos2.index, zeroconteonichos2[cluster], color='skyblue')
#         axes[i].set_title(cluster, fontsize=20)
#         axes[i].tick_params(axis='x', rotation=90, labelsize=16)  # Aumentar tamaño de fuente de los números del eje x
#         axes[i].tick_params(axis='y', labelsize=16)  # Aumentar tamaño de fuente de los números del eje y

#     # Remover ejes adicionales en caso de que existan
#     for i in range(len(clusters_subset), len(axes)):
#         fig.delaxes(axes[i])

#     # Solo una etiqueta de eje y
#     fig.text(0.04, 0.5, 'Frecuencia', va='center', ha='center', rotation='vertical', fontsize=18)

#     # Solo una etiqueta de eje x
#     fig.text(0.5, 0.04, 'Característica', va='center', ha='center', fontsize=18)
    
#     # Ajustar las etiquetas de las características
#     plt.setp(axes, xticks=range(len(zeroconteonichos2.index)), xticklabels=zeroconteonichos2.index)
    
#     plt.tight_layout(rect=[0.05, 0.05, 1, 0.95])
#     plt.show()
    
# =============================================================================
# =============================================================================
# OPCION 11
# UN HISTOGRAMA (dos filas)
len(zeroconteonichos.index)
# Apilar los datos para combinarlos en una sola serie
zeroconteonichos2 = pd.concat([zeroconteonichos.drop(['HostHuman', "HostFungi", "Hostalga", "Hostanimal"])], axis=0) 
h3 = zeroconteonichos2.stack().reset_index()
h3.columns = ['Caracteristica', 'Cluster', 'Frecuencia']

# Crear el histograma
plt.figure(figsize=(30, 8))
clusters = h3['Cluster'].unique()
caracteristicas = h3['Caracteristica'].unique()
bar_width = 0.4  # Ajusta el ancho de las barras

# Asignar colores
colors = ['blue', 'orange']  # Dos colores para las barras

# Calcular las posiciones
positions = []
for i, caracteristica in enumerate(caracteristicas):
    pos = [i * (bar_width * len(clusters) + 0.5) + j * bar_width for j in range(len(clusters))]
    positions.append(pos)

# Dibujar las barras
for i, cluster in enumerate(clusters):
    cluster_data = h3[h3['Cluster'] == cluster]
    pos = [positions[j][i] for j in range(len(caracteristicas))]
    plt.bar(pos, cluster_data['Frecuencia'], width=bar_width, color=colors[i % 2])

# Ajustar las posiciones del eje x y las etiquetas
flattened_positions = [p for sublist in positions for p in sublist]
x_labels = [f'{caracteristicas[i % len(caracteristicas)]}\nCluster {clusters[i // len(caracteristicas)]}' for i in range(len(flattened_positions))]
plt.xticks(flattened_positions, x_labels, rotation=90, fontsize=5, fontweight='bold')

# Añadir etiquetas y leyenda
plt.xlabel('Característica y Clúster')
plt.ylabel('Frecuencia')
plt.title('Frecuencias por Característica y Clúster')
#plt.show()
# Ajustar el diseño para que no se recorten los elementos
plt.tight_layout()
# Guardar la gráfica como un archivo PNG
plt.savefig(histlabelspng, format='png', dpi=300, bbox_inches='tight')
# =============================================================================
# =============================================================================

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
# =============================================================================
# Configurar el tamaño de la figura (ancho, alto) en pulgadas (GRAFICO DE BARRAS)
plt.figure(figsize=(20, 12))
primeros100.plot(kind='bar')
plt.title('Importancia de las características')
plt.xlabel('Características')
plt.ylabel('Importancia')
# Ajustar la rotación de las etiquetas del eje x
plt.xticks(rotation=90, fontsize=3, fontweight='bold') 
# Ajustar el diseño para que no se recorten los elementos
plt.tight_layout()
# Guardar la gráfica como un archivo PNG
plt.savefig(rutaimportacara, format='png', dpi=300, bbox_inches='tight')
# =============================================================================
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


###################### -- Hacemos predicciones con el conjunto de prueba -- ######################
predictions = rf.predict(test_mtz_class_caracteres)

##################### -- Matriz de Confusion -- ######################
prediction_discrete = np.round(predictions).astype(int)
mc = confusion_matrix(test_labels, prediction_discrete)

mc_df = pd.DataFrame(mc)
mc_df.to_csv(rutaconfusion)

##################### -- Visualizacion de la Matriz de Confusion -- ######################
vis = ConfusionMatrixDisplay(mc)
# Crear la visualización de la matriz de confusión
vis.plot()
# Ajustar el diseño para que no se recorten los elementos
plt.tight_layout()
# Guardar la gráfica como un archivo PNG con el tamaño y resolución especificados
plt.savefig(rutaconfusionpng, format='png', dpi=300, bbox_inches='tight')
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
