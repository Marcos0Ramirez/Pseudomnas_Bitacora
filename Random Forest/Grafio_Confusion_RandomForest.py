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

rutabase= "/RandomForest/RandomForest_py/" # Ruta base
filemtz = "reduced_testpysh_pymatrizcdhit.csv" #Nombre del archivo con la matriz
fileclass = "reduced_classificacion_genomas.txt" # Nombre de la tabla de clasificacion

rutamtz = os.path.join(rutabase, filemtz)
rutaclass = os.path.join(rutabase, fileclass)

imgrutabase = "/RandomForest/RandomForest_py/Imagenes_results_local_data/Prueba1_donichos/"
imgic = "importancia_caracteristicas.png"
imgic2 = "importancia_caracteristicas_log.png"
mtzconfusion = "confusion_matrix.csv"
mtzconfusion2 = "confusion_matrix.png"
histo="histograma_tlabels.png"
histot_50="histograma_t50labels_{}.png"
histom="histograma_mlabels.png"
histompy2="histograma_mlabels_encoded.png"
histom_input = "histograma_mlabels_encoded_{}.png" #Mantener el {0} para las multiples imagenes si son mas de dos nichos
conteonichos = "zeroconteonichos.csv"
conteonichos_encoded = "zeroconteonichos_encoded.csv"
etiquetas_codificadas = "np_class_etiquetas.csv"

rutaimportacara = os.path.join(imgrutabase, imgic)
rutaimportacara2 = os.path.join(imgrutabase, imgic2)
rutaconfusion = os.path.join(imgrutabase, mtzconfusion)
rutaconfusionpng = os.path.join(imgrutabase, mtzconfusion2)
histlabelspng = os.path.join(imgrutabase, histo)
histt50labelspang = os.path.join(imgrutabase, histot_50)
histmlabelspng = os.path.join(imgrutabase, histom)
histmlabelspng_encoded = os.path.join(imgrutabase, histompy2)
cluster100matriz = os.path.join(imgrutabase, conteonichos)
cluster100matriz_encoded = os.path.join(imgrutabase, conteonichos_encoded)
rutaetiquetas_codificadas = os.path.join(imgrutabase, etiquetas_codificadas)

# Extraemos la data
matriz = pd.read_csv(rutamtz)
print(matriz)
matriz = matriz.rename_axis("HOLA")
# Extremos la tabla de clasificacion

classificacion = pd.read_csv(rutaclass, sep='\t')

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
#mtz_class_caracteres = pd.concat([mtz_class_caracteres.drop(columns=['Specie'])], axis=1) 

### -- Caracteristicas y Objetivos, y Convertir Datos en Arreglos -- ###
labels = np.array(mtz_class_caracteres["Nicho"])
la_enc = LabelEncoder()
encoded_labels = la_enc.fit_transform(labels)

etiquetas = labels.reshape(1, -1)
codified =  encoded_labels.reshape(1, -1)

class_etiquetas = np.concatenate((etiquetas, codified)).T
print(class_etiquetas)
pd.DataFrame(class_etiquetas).drop_duplicates().to_csv(rutaetiquetas_codificadas, index=False)
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
        
zeroconteonichos.to_csv(cluster100matriz)
      
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
zeroconteonichos_encoded.to_csv(cluster100matriz_encoded)

##### Continuamos con el histograma. ######


# =============================================================================
# =============================================================================
# # OPCION 9
# # MUCHOS HISTOGRAMAS
# 
# # Número total de clústeres
# num_clusters = zeroconteonichos.shape[1]
# 
# # Dividir en grupos de 25 clústeres
# clusters_per_image = 25
# num_images = num_clusters // clusters_per_image
# 
# # Lista de colores para los histogramas
# colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightpink']
# 
# for img in range(num_images):
#     histom=histom_input.format(img + 1)
#     histmlabelspng = os.path.join(imgrutabase, histom)
#     start_idx = img * clusters_per_image
#     end_idx = start_idx + clusters_per_image
#     clusters_subset = zeroconteonichos.columns[start_idx:end_idx]
#     
#     # Crear subplots: número de filas y columnas
#     num_cols = 5  # Número de columnas deseadas en el grid
#     num_rows = (clusters_per_image + num_cols - 1) // num_cols  # Calcular el número de filas
# 
#     fig, axes = plt.subplots(num_rows, num_cols, figsize=(25, num_rows * 5), sharex=True, sharey=True)
#     axes = axes.flatten()
# 
#     for i, cluster in enumerate(clusters_subset):
#         print(i, cluster)
#         axes[i].bar(zeroconteonichos.index, zeroconteonichos[cluster], color=colors[i % len(colors)])
#         axes[i].set_title(cluster, fontsize=20)
#         axes[i].tick_params(axis='x', rotation=90, labelsize=20)  # Aumentar tamaño de fuente de los números del eje x
#         axes[i].tick_params(axis='y', labelsize=25)  # Aumentar tamaño de fuente de los números del eje y
# 
#     # Remover ejes adicionales en caso de que existan
#     for i in range(len(clusters_subset), len(axes)):
#         fig.delaxes(axes[i])
# 
#     # Solo una etiqueta de eje y
#     fig.text(0.01, 0.5, 'Frecuencia', va='center', ha='center', rotation='vertical', fontsize=26)
# 
#     # Solo una etiqueta de eje x
#     fig.text(0.5, 0.001, 'Característica', va='center', ha='center', fontsize=26)
#     
#     # Ajustar las etiquetas de las características
#     plt.setp(axes, xticks=range(len(zeroconteonichos.index)), xticklabels=zeroconteonichos.index)
# 
#     # Añadir un título general
#     fig.suptitle(f'Histograma {img + 1}', fontsize=30)
#     # Ajusta los márgenes de la figura
#     plt.subplots_adjust(left=0.05, right=0.9, top=0.95, bottom=0.1)
# 
#     #plt.show()
#     # Ajustar el diseño para que no se recorten los elementos
#     #plt.tight_layout()
#     # Guardar la gráfica como un archivo PNG
#     plt.savefig(histmlabelspng, format='png', dpi=300, bbox_inches='tight')
#     plt.close(fig) 
# =============================================================================

# =============================================================================
if len(zeroconteonichos.index) > 2:
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
        histompy2=histom_input.format(img + 1)
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
else:
    # OPCION 11
    # UN HISTOGRAMA (dos filas)
    # Apilar los datos para combinarlos en una sola serie

    h3_o = pd.DataFrame(np.array([[i, j, int(zeroconteonichos.loc[i,j])] for j in zeroconteonichos.columns if j for i in zeroconteonichos.index if i]))
    h3_o.columns = ['Caracteristica', 'Cluster', 'Frecuencia']

    for i in [0, 50, 100, 150]:
        h3 = h3_o[i:i+50]
        h3 = h3.reset_index(drop=True)
        y_min, y_max = 0, int(max(h3['Frecuencia'])) + 1
        print(h3)
        
        histot_50="histograma_t50labels_{}.png".format(i)
        histt50labelspang = os.path.join(imgrutabase, histot_50)
        
        # Crear el histograma
        plt.figure(figsize=(12, 4))
        clusters = h3['Cluster'].unique()
        caracteristicas = h3['Caracteristica'].unique()
        bar_width = 0.1  # Ajusta el ancho de las barras
        
        # Asignar colores
        colors = ['blue', 'orange']  # Dos colores para las barras
            
        # Calcular las posiciones
        positions = []
        par=[]
        impar=[]
        for i in range(0,len(h3)):
            if i % 2 == 0:
                #print('par', i)
                par.append(i*bar_width)
            else:
                #print('impar', i)
                impar.append(i*bar_width)
        positions.append(par)
        positions.append(impar)
        
        
        # Dibujar las barras
        for i, cluster in enumerate(clusters):
            cluster_data = h3[h3['Cluster'] == cluster]
            pos = [positions[j][i] for j in range(len(caracteristicas))]
            plt.bar(pos, pd.Series(int(i) for i in cluster_data['Frecuencia'] if i), width=bar_width, color=[colors[0],colors[1]])
    
        # Ajustar las posiciones del eje x y las etiquetas
        #flattened_positions = [p for sublist in positions2 for p in sublist]
        flattened_positions = [p for sublist in positions for p in sublist]
        x_labels = ['{}\nCluster {}'.format(caracteristicas[i], clusters[j]) for i in range(len(caracteristicas)) for j in range(len(clusters))]
        plt.xticks(flattened_positions, x_labels, rotation=90, fontsize=6, fontweight='bold')
        
        # Ajustar el eje y manualmente para asegurar consistencia
        plt.ylim(y_min, y_max)
        plt.yticks(np.arange(y_min, y_max, 1)) 
        
        # Añadir etiquetas y leyenda con colores personalizados
        legend_patches = [
            plt.Rectangle((0, 0), 1, 1, fc='blue', alpha=0.7),
            plt.Rectangle((0, 0), 1, 1, fc='orange', alpha=0.7)
        ]
        plt.legend(legend_patches, caracteristicas)
        
        # Añadir etiquetas y leyenda
        plt.xlabel('Característica y Clúster')
        plt.ylabel('Frecuencia')
        plt.title('Frecuencias por Característica y Clúster ({})'.format(" y ".join(caracteristicas)))
        #plt.show()
        # Ajustar el diseño para que no se recorten los elementos
        plt.tight_layout()
        # Guardar la gráfica como un archivo PNG
        plt.savefig(histt50labelspang, format='png', dpi=300, bbox_inches='tight')
        plt.close()

# =============================================================================
# =============================================================================

# Crear la figura y el objeto Axes
fig, ax = plt.subplots(figsize=(12, 4))

# Crear el gráfico de barras en el objeto Axes
primeros100.plot(kind='bar', ax=ax)

# Título y etiquetas de los ejes
ax.set_title('Importancia de las características NORMAL, \ncomparativa ({})'.format(" ".join(caracteristicas)))
ax.set_xlabel('Random Forest: Características consideradas (clusters)')
ax.set_ylabel('Importancia de las caracteristicas (clusters), \nnormal')

# Ajustar la rotación de las etiquetas del eje x
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, fontsize=6, fontweight='bold')

# Ajustar el diseño para que no se recorten los elementos
plt.tight_layout()

# Guardar la gráfica como un archivo PNG
plt.savefig(rutaimportacara, format='png', dpi=300, bbox_inches='tight')

# Mostrar la gráfica
plt.show()

# =============================================================================
# Configurar el tamaño de la figura (ancho, alto) en pulgadas (GRAFICO LOGARITMICA)
# Crear la figura con el tamaño especificado
fig, ax = plt.subplots(figsize=(12, 4))

# Crear la gráfica de barras con el eje y en escala logarítmica
primeros100.plot(kind='bar', logy=True, ax=ax)  # Aquí se especifica que el eje y será logarítmico

# Título y etiquetas de los ejes
ax.set_title('Importancia de las características LOGARITMICA, \ncomparativa ({})'.format(" ".join(caracteristicas)))
ax.set_xlabel('Random Forest: Características consideradas (clusters)')
ax.set_ylabel('Importancia de las caracteristicas (clusters), \nlogaritmica')

# Ajustar la rotación de las etiquetas del eje x
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, fontsize=6, fontweight='bold')

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
