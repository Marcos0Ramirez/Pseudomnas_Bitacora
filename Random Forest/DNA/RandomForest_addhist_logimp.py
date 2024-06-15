#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos las librerias necesarias
import time
import pandas as pd
import numpy as np
import os
import csv
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score # ConfusionMatrixDisplay,
import matplotlib
matplotlib.use('Agg')  # Usar backend 'Agg' para entornos sin pantalla
import matplotlib.pyplot as plt
import sys
import io
import codecs

reload(sys)
sys.setdefaultencoding('utf-8')

def safe_precision_score(y_true, y_pred):
    try:
        return precision_score(y_true, y_pred, average='weighted')
    except ZeroDivisionError:
        return 0.0

def confusion_graph():
    start_time = time.time()
    ###################### -- DIRECCIONES, ARCHIVOS Y PARAMETROS -- ######################
    rutabase= "Pseudomonas/WORK/ANALYSIS_CDHIT/MATRIXCDHIT/" # Ruta base
    filemtz = "fast_matrizcdhit_pymatrizcdhit.csv" #Nombre del archivo con la matriz
    fileclass = "nichospseudo3894.txt" # Nombre de la tabla de clasificacion
    n_estima = 50
    porcen_comprobacion = 0.20
    estado_aleatorio1 = 99
    estado_aleatorio2 = 7
    
    rutamtz = os.path.join(rutabase, filemtz)
    rutaclass = os.path.join(rutabase, fileclass)
    
    imgrutabase = "/Pseudomonas/WORK/ANALYSIS_CDHIT/MATRIXCDHIT/IMAGENES/"
    imgic = "importancia_caracteristicas.png"
    imgic2 = "importancia_caracteristicas_log.png" #------------------------- // NUEVO \\ --------------------------#
    mtzconfusion = "confusion_matrix.csv"
    histo="histograma_tlabels.png" #------------------------- // NUEVO \\ --------------------------#
    histom="histograma_mlabels.png" #------------------------- // NUEVO \\ --------------------------#
    
    rutaimportacara = os.path.join(imgrutabase, imgic)
    rutaimportacara2 = os.path.join(imgrutabase, imgic2) #------------------------- // NUEVO \\ --------------------------#
    rutaconfusion = os.path.join(imgrutabase, mtzconfusion)
    histlabelspng = os.path.join(imgrutabase, histo) #------------------------- // NUEVO \\ --------------------------#
    histmlabelspng = os.path.join(imgrutabase, histom) #------------------------- // NUEVO \\ --------------------------#

    
    ###################### -- EXTRACCION DE LOS DATOS -- ######################
    # Extraemos la data
    # Matriz de frecuencias genomas-clusters
    chunks = []
    chunk_size = 100000  # Número de filas por chunk
    row_count = 0
    print("abriendo el archivo")
    sys.stdout.flush()
    
    with codecs.open(rutamtz, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        print("empezamos con los chunks")
        sys.stdout.flush()
        chunk = []
        for row in csvreader:
            chunk.append(row)
            row_count += 1
            if row_count % chunk_size == 0:
                df_chunk = pd.DataFrame(chunk, columns=header)
                chunks.append(df_chunk)
                chunk = []
        print("tomamos los chunks")
        sys.stdout.flush()
        if chunk:
            df_chunk = pd.DataFrame(chunk, columns=header)
            chunks.append(df_chunk)
    print("listo para concatenar todo")
    sys.stdout.flush()
    df = pd.concat(chunks, ignore_index=True)
    
    columns_to_drop = [col for col in df.columns if col == '' or col is None]
    df.drop(columns=columns_to_drop, inplace=True)
    
    print("Ahora si las dimensiones de la matriz dataframe")
    sys.stdout.flush()
    print(df.shape)
    
    # Tabla de clasificacion por nichos
    with codecs.open(rutaclass, 'r', encoding='utf-8') as csvclass:
            csvclase = csv.reader(csvclass, delimiter="\t")
            data = list(csvclase)
    
    encabezado = data[0]
    rows = data[1:]
    df_clase = pd.DataFrame(rows, columns=encabezado)
    
    mtz_class_caracteres = pd.merge(df.sort_values(by='Genomas'), df_clase.sort_values(by='Genomas'), on='Genomas')
    mtz_class_caracteres.set_index('Genomas', inplace=True) #------------------------- // NUEVO \\ --------------------------#
    mtz_class_caracteres = mtz_class_caracteres[mtz_class_caracteres['Nicho'] != 'vacio']
    mtz_idgen_nicho = pd.DataFrame(pd.Series(mtz_class_caracteres['Nicho'])) #------------------------- // NUEVO \\ --------------------------#
    print(mtz_class_caracteres.shape)
    sys.stdout.flush()
    print(mtz_class_caracteres.head())
    sys.stdout.flush()
    
    ###################### -- PREPARACION DE LOS DATOS -- ######################
    mtz_class_caracteres = pd.concat([mtz_class_caracteres.drop(columns=['Genomas'])], axis=1) 
    
    print("los nichos los hacemos array")
    sys.stdout.flush()
    labels = np.array(mtz_class_caracteres["Nicho"])
    la_enc = LabelEncoder()
    encoded_labels = la_enc.fit_transform(labels)

    etiquetas = labels.reshape(1, -1) #------------------------- // NUEVO \\ --------------------------#
    codified =  encoded_labels.reshape(1, -1) #------------------------- // NUEVO \\ --------------------------#

    class_etiquetas = np.concatenate((etiquetas, codified)).T #------------------------- // NUEVO \\ --------------------------#
    print(class_etiquetas) #------------------------- // NUEVO \\ --------------------------#
    sys.stdout.flush() #------------------------- // NUEVO \\ --------------------------#
    pd.DataFrame(class_etiquetas).drop_duplicates().to_csv("np_class_etiquetas.csv", index=False) #------------------------- // NUEVO \\ --------------------------#
    
    mtz_class_caracteres = mtz_class_caracteres.drop("Nicho", axis=1)
    mtz_class_caracteres_list = list(mtz_class_caracteres.columns)
    print("la matriz la hacemos arreglo")
    sys.stdout.flush()
    mtz_class_caracteres = np.array(mtz_class_caracteres)
    
    train_mtz_class_caracteres, test_mtz_class_caracteres, train_labels, test_labels = train_test_split(mtz_class_caracteres, 
                                                                                                        encoded_labels, 
                                                                                                        test_size=porcen_comprobacion,  #==================== // MODIFICADO \\ ====================#
                                                                                                        random_state=estado_aleatorio1) #==================== // MODIFICADO \\ ====================#
    
    print('Training Features Shape:', train_mtz_class_caracteres.shape)
    sys.stdout.flush()
    print('Training Labels Shape:', train_labels.shape)
    sys.stdout.flush()
    print('Testing Features Shape:', test_mtz_class_caracteres.shape)
    sys.stdout.flush()
    print('Testing Labels Shape:', test_labels.shape)
    sys.stdout.flush()
    
    ###################### -- ENTRENAMIENTO DEL MODELO -- ######################
    rf = RandomForestRegressor(n_estimators=n_estima, random_state=estado_aleatorio2) #==================== // MODIFICADO X2 \\ ====================#
    rf.fit(train_mtz_class_caracteres, train_labels)
    
    ###################### -- Caracteristicas que son importantes -- ######################
    importancias = rf.feature_importances_
    feature_importances = pd.DataFrame(importancias, index=mtz_class_caracteres_list, columns=['Importancia'])
    feature_importances = feature_importances.sort_values(by='Importancia', ascending=False)
    
    print(feature_importances)
    sys.stdout.flush()
    primeros100 = feature_importances.iloc[:100]
    print(primeros100)
    sys.stdout.flush()
    
    ###################### -- Nichos por Clusters -- ######################
    #Tomamos los nombres de los clusters.
    cienclusters_importantes = " ".join(primeros100.index)  #------------------------- // NUEVO \\ --------------------------#
    # Como la matriz esta en un numpy array, ahora toca extraer por el numero de las columna. #------------------------- // NUEVO \\ --------------------------#
    cienclusters_importantes = cienclusters_importantes.replace("Cluster", "").split(" ") #------------------------- // NUEVO \\ --------------------------#
    # Nombramos las columnas que necesitamos #------------------------- // NUEVO \\ --------------------------#
    clustercien = [mtz_class_caracteres[:,int(npcol)] for npcol in cienclusters_importantes if not npcol is None] #------------------------- // NUEVO \\ --------------------------#
    mtz_clustercien = pd.DataFrame(np.array(clustercien).T, columns=cienclusters_importantes, index=mtz_idgen_nicho.index) #------------------------- // NUEVO \\ --------------------------#
    # añadimos los nichos #------------------------- // NUEVO \\ --------------------------#
    mtz_clustercien['Nicho'] = mtz_idgen_nicho['Nicho'] #------------------------- // NUEVO \\ --------------------------#

    
    ###################### -- Nichos por Clusters: Hacemos el conteo -- ######################
    u = mtz_idgen_nicho["Nicho"].unique() #------------------------- // NUEVO \\ --------------------------#
    c =list(mtz_clustercien.columns) #------------------------- // NUEVO \\ --------------------------#
    del c[c.index('Nicho')] #------------------------- // NUEVO \\ --------------------------#
    #Creamos una matriz #------------------------- // NUEVO \\ --------------------------#
    zeroconteonichos = pd.DataFrame(0, index=u, columns=c) #------------------------- // NUEVO \\ --------------------------#
    for i in u: #------------------------- // NUEVO \\ --------------------------#
        for j in c: #------------------------- // NUEVO \\ --------------------------#
            ev = list(mtz_clustercien.index[mtz_clustercien['Nicho'] == i]) #------------------------- // NUEVO \\ --------------------------#
            zeroconteonichos.loc[i,j] = int(sum(list(mtz_clustercien.loc[ev,j]))) #------------------------- // NUEVO \\ --------------------------#

    ###################### -- GRAFICOS -- ######################
    # Grafico de barras, de escala normal
    plt.figure(figsize=(20, 12))
    primeros20.plot(kind='bar')
    plt.title('Importancia de las características')
    plt.xlabel('Características')
    plt.ylabel('Importancia')
    plt.xticks(rotation=90, fontsize=3, fontweight='bold') #==================== // MODIFICADO \\ ====================#
    plt.tight_layout()
    
    try:
        plt.savefig(rutaimportacara, format='png', dpi=300, bbox_inches='tight')
        print("Imagen guardada exitosamente")
    except Exception as e:
        sys.stderr.write("Error al guardar la imagen: {}\n".format(e))
        sys.stderr.flush()

    # Grafico de barras, de escala logaritmica
    plt.figure(figsize=(20, 12))  #------------------------- // NUEVO \\ --------------------------#
    primeros20.plot(kind='bar', logy=True)  #------------------------- // NUEVO \\ --------------------------#
    plt.title('Importancia de las características')  #------------------------- // NUEVO \\ --------------------------#
    plt.xlabel('Características')  #------------------------- // NUEVO \\ --------------------------#
    plt.ylabel('Importancia')  #------------------------- // NUEVO \\ --------------------------#
    plt.xticks(rotation=90, fontsize=3, fontweight='bold')   #------------------------- // NUEVO \\ --------------------------#
    plt.tight_layout()  #------------------------- // NUEVO \\ --------------------------#
    
    try:  #------------------------- // NUEVO \\ --------------------------#
        plt.savefig(rutaimportacara2, format='png', dpi=300, bbox_inches='tight')   #------------------------- // NUEVO \\ --------------------------#
        print("Imagen guardada exitosamente")  #------------------------- // NUEVO \\ --------------------------#
    except Exception as e:  #------------------------- // NUEVO \\ --------------------------#
        sys.stderr.write("Error al guardar la imagen: {}\n".format(e))  #------------------------- // NUEVO \\ --------------------------#
        sys.stderr.flush()  #------------------------- // NUEVO \\ --------------------------#

    # Histograma, mayor a 2 nichos
    if len(zeroconteonichos.index) > 2:
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
            
            # Guardar la gráfica como un archivo PNG
            try:  #------------------------- // NUEVO \\ --------------------------#
                histlabelspng
                plt.savefig(histmlabelspng,, format='png', dpi=300, bbox_inches='tight')   #------------------------- // NUEVO \\ --------------------------#
                plt.close(fig)
                print("Imagen guardada exitosamente")  #------------------------- // NUEVO \\ --------------------------#
            except Exception as e:  #------------------------- // NUEVO \\ --------------------------#
                sys.stderr.write("Error al guardar la imagen: {}\n".format(e))  #------------------------- // NUEVO \\ --------------------------#
                sys.stderr.flush()  #------------------------- // NUEVO \\ --------------------------#
    else:
        # UN HISTOGRAMA (dos filas)
        # Apilar los datos para combinarlos en una sola serie
        h3 = zeroconteonichos.stack().reset_index()
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
        try:  #------------------------- // NUEVO \\ --------------------------#
            histlabelspng
            plt.savefig(histlabelspng,, format='png', dpi=300, bbox_inches='tight')   #------------------------- // NUEVO \\ --------------------------#
            print("Imagen guardada exitosamente")  #------------------------- // NUEVO \\ --------------------------#
        except Exception as e:  #------------------------- // NUEVO \\ --------------------------#
            sys.stderr.write("Error al guardar la imagen: {}\n".format(e))  #------------------------- // NUEVO \\ --------------------------#
            sys.stderr.flush()  #------------------------- // NUEVO \\ --------------------------#



    ###################### -- Hacemos predicciones con el conjunto de prueba -- ######################
    predictions = rf.predict(test_mtz_class_caracteres)

    ##################### -- Matriz de Confusion -- ######################
    prediction_discrete = np.round(predictions).astype(int)
    mc = confusion_matrix(test_labels, prediction_discrete)
    
    mc_df = pd.DataFrame(mc)
    
    try:
        mc_df.to_csv(rutaconfusion)
        print("Matriz de confusión guardada exitosamente")
    except Exception as e:
        sys.stderr.write("Error al guardar la matriz de confusión: {}\n".format(e))
        sys.stderr.flush()
    
    try:
        accuracy = accuracy_score(test_labels, prediction_discrete)
        precision = safe_precision_score(test_labels, prediction_discrete)
        recall = recall_score(test_labels, prediction_discrete, average='weighted')
        f1 = f1_score(test_labels, prediction_discrete, average='weighted')

        print("Accuracy:", accuracy)
        sys.stdout.flush()
        print("Precision:", precision)
        sys.stdout.flush()
        print("Recall:", recall)
        sys.stdout.flush()
        print("F1 Score:", f1)
        sys.stdout.flush()
    except Exception as e:
        sys.stderr.write("Error al calcular las métricas: {}\n".format(e))
        sys.stderr.flush()
    
    elapsed_time = time.time() - start_time
    print("Elapsed time to compute the importances: {:.3f} seconds".format(elapsed_time))
    sys.stdout.flush()

if __name__ == "__main__":
    try:
        confusion_graph()
    except Exception as e:
        sys.stderr.write("Ha ocurrido un error: {}\n".format(e))
        sys.stderr.flush()

