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
import traceback
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
    rutabase= "/PSEUDOMONAS_SCRIPTS/MicroSetRANDOMFOREST/INPUT/" # Ruta base
    filemtz = "reduced_testpysh_pymatrizcdhit.csv" #Nombre del archivo con la matriz
    fileclass = "reduced_classificacion_genomas.txt" # Nombre de la tabla de clasificacion
    empty_nicho = 'Unclassified'
    n_estima = 50
    porcen_comprobacion = 0.20
    estado_aleatorio1 = 99
    estado_aleatorio2 = 7
    
    rutamtz = os.path.join(rutabase, filemtz)
    rutaclass = os.path.join(rutabase, fileclass)
    
    imgrutabase = "/PSEUDOMONAS_SCRIPTS/MicroSetRANDOMFOREST/OUTPUT/"
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
    print(df)

    # Verificar la presencia de la columna 'Genomas' antes de eliminar columnas
    print("Columnas de df antes de eliminar:", df.columns)
    if 'Genomas' not in df.columns:
        print("Error: 'Genomas' no se encuentra en df antes de eliminar columnas")

    columns_to_drop = [col for col in df.columns if col == '' or col is None]
    print(columns_to_drop)
    sys.stdout.flush()
    if len(columns_to_drop) > 0:
    	df.drop(columns=columns_to_drop, inplace=True)
    
    print(df)
    sys.stdout.flush()

    # Verificar la presencia de la columna 'Genomas' después de eliminar columnas
    print("Columnas de df después de eliminar:", df.columns)
    if 'Genomas' not in df.columns:
        print("Error: 'Genomas' no se encuentra en df después de eliminar columnas")

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
    print(df_clase)
    sys.stdout.flush()
    print("antes de concatenar las tablas")
    sys.stdout.flush()
    mtz_class_caracteres = pd.merge(df.sort_values(by='Genomas'), df_clase.sort_values(by='Genomas'), on='Genomas')
    print(mtz_class_caracteres)
    sys.stdout.flush()

    mtz_class_caracteres.set_index('Genomas', inplace=True, drop=False) #------------------------- // NUEVO \\ --------------------------#
    #mtz_class_caracteres.index.name = 'Genomas'
    print("Una vez que ya se hizo como indice la columna Genomas")
    sys.stdout.flush()
    print(mtz_class_caracteres)
    sys.stdout.flush()
    print(mtz_class_caracteres.index)
    sys.stdout.flush()
    

    mtz_class_caracteres = mtz_class_caracteres[mtz_class_caracteres['Nicho'] != empty_nicho]
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
    pd.DataFrame(class_etiquetas).drop_duplicates().to_csv("./OUTPUT/np_class_etiquetas.csv", index=False) #------------------------- // NUEVO \\ --------------------------#
    #print(mtz_class_caracteres)
    #sys.stdout.flush()
    mtz_class_caracteres = mtz_class_caracteres.drop("Nicho", axis=1)
    #print(mtz_class_caracteres)
    #sys.stdout.flush()
    mtz_class_caracteres_list = list(mtz_class_caracteres.columns)
    #print(mtz_class_caracteres_list)
    #sys.stdout.flush()
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
    print("columnas 100; extraidas: ", clustercien)
    sys.stdout.flush()
    #clustercien = [mtz_class_caracteres[npcol] for npcol in cienclusters_importantes if npcol in mtz_class_caracteres.columns]

    mtz_clustercien = pd.DataFrame(np.array(clustercien).T, columns=cienclusters_importantes, index=mtz_idgen_nicho.index) #------------------------- // NUEVO \\ --------------------------#
    # añadimos los nichos #------------------------- // NUEVO \\ --------------------------#
    mtz_clustercien['Nicho'] = mtz_idgen_nicho['Nicho'] #------------------------- // NUEVO \\ --------------------------#

    print(r"matriz mtz_clustercien creada\n", mtz_clustercien)
    sys.stdout.flush()
    print(r"indices de mtz_clustercien \n", mtz_clustercien.index)
    sys.stdout.flush()
    print(r"columnas de mtz_clustercien \n", mtz_clustercien.columns)
    sys.stdout.flush()
    
    ###################### -- Nichos por Clusters: Hacemos el conteo -- ######################
    print("Continuamos hacia el conteo, juntando en indice y las 100 columnas")
    sys.stdout.flush()
    u = mtz_idgen_nicho["Nicho"].unique() #------------------------- // NUEVO \\ --------------------------#
    c =list(mtz_clustercien.columns) #------------------------- // NUEVO \\ --------------------------#
    print("u", u, "c", c)
    sys.stdout.flush()
    print("A eliminar la palabra Nicho de la lista c")
    sys.stdout.flush()
    del c[c.index('Nicho')] #------------------------- // NUEVO \\ --------------------------#
    print(c, 'Nicho' in c)
    sys.stdout.flush()
    #Creamos una matriz #------------------------- // NUEVO \\ --------------------------#
    print("matriz vacia, creandose")
    sys.stdout.flush()

    zeroconteonichos = pd.DataFrame(0, index=u, columns=c) #------------------------- // NUEVO \\ --------------------------#
    print("matriz vacia, creada, continuamos con concatenar los 100 mejores cluster en la matriz vacia")
    sys.stdout.flush()
    for i in u: #------------------------- // NUEVO \\ --------------------------#
        for j in c: #------------------------- // NUEVO \\ --------------------------#
            #print(i, j)
            #sys.stdout.flush()
            ev = list(mtz_clustercien.index[mtz_clustercien['Nicho'] == i])
            #print(ev)
            #sys.stdout.flush()
            # Asegúrate de que todos los elementos sean enteros
            values_to_sum = list(mtz_clustercien.loc[ev, j])
            #print("Valores a sumar (antes de convertir):", values_to_sum)
            #sys.stdout.flush()
            values_to_sum = map(int, values_to_sum)
            #print("Valores a sumar (después de convertir):", values_to_sum)
            #sys.stdout.flush()
            sumas = sum(values_to_sum)
            #print("sumas: ", sumas)
            #sys.stdout.flush()
            zeroconteonichos.loc[i, j] = sumas
            #print("zeroconteonichos.loc[i,j]", zeroconteonichos.loc[i, j])
            #sys.stdout.flush()

    zeroconteonichos.to_csv("./OUTPUT/zeroconteonichos.csv")

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
    print(zeroconteonichos_encoded.shape)
    zeroconteonichos_encoded.to_csv("./OUTPUT/zeroconteonichos_encoded.csv")
            
    ###################### -- GRAFICOS -- ######################
    print("Hora de hacer los graficos \n El primero es de barras de escala normal")
    sys.stdout.flush()
    # Grafico de barras, de escala normal
    plt.figure(figsize=(20, 12))
    primeros100.plot(kind='bar')
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

    print("Hora de hacer los graficos \n El segundo es de barras de escala logaritmica")
    sys.stdout.flush()
    # Grafico de barras, de escala logaritmica
    plt.figure(figsize=(20, 12))  #------------------------- // NUEVO \\ --------------------------#
    primeros100.plot(kind='bar', logy=True)  #------------------------- // NUEVO \\ --------------------------#
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
        # Codificacion en numeros, los indices
        # MUCHOS HISTOGRAMAS
        # Número total de clústeres

        print("HISTOGRAMA CON MUCHOS NICHOS")
        sys.stdout.flush()

        num_clusters = zeroconteonichos_encoded.shape[1]
        # Dividir en grupos de 25 clústeres
        clusters_per_image = 25
        num_images = num_clusters // clusters_per_image
        # Lista de colores para los histogramas
        colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightpink']
        for img in range(num_images):
            histom = "histograma_mlabels_encoded_{0}.png".format(img + 1)
            histmlabelspng = os.path.join(imgrutabase, histom)
            start_idx = img * clusters_per_image
            end_idx = start_idx + clusters_per_image
            clusters_subset = zeroconteonichos_encoded.columns[start_idx:end_idx]
            
            # Crear subplots: número de filas y columnas
            num_cols = 5  # Número de columnas deseadas en el grid
            num_rows = (clusters_per_image + num_cols - 1) // num_cols  # Calcular el número de filas
        



            fig, axes = plt.subplots(num_rows, num_cols, figsize=(25, num_rows * 5), sharex=True, sharey=True)
            axes = axes.flatten()
            print("Toca procesar las posiciones de las imagenes")
            sys.stdout.flush()
            for i, cluster in enumerate(clusters_subset):
                print(i, cluster, type(i), type(cluster))
                sys.stdout.flush()
                #cluster=int(cluster)
                #print(i, cluster, type(i), type(cluster))
                #print(zeroconteonichos.index, type(zeroconteonichos.index), zeroconteonichos[cluster], type(zeroconteonichos[cluster]))
                # sys.stdout.flush()
                print("Ordenando la lista: ", sorted(list(zeroconteonichos_encoded.index)))
                axes[i].bar(sorted(list(zeroconteonichos_encoded.index)), zeroconteonichos_encoded[cluster], color=colors[i % len(colors)])
                axes[i].set_title(cluster, fontsize=20)
                #plt.setp(axes[i].get_xticklabels(), rotation=90, fontsize=20)
                axes[i].tick_params(axis='x', labelsize=20)  # Aumentar tamaño de fuente de los números del eje x rotation=90,
                axes[i].tick_params(axis='y', labelsize=25)  # Aumentar tamaño de fuente de los números del eje y



            
            print("Vamos con los ejes")
            sys.stdout.flush()
            # Remover ejes adicionales en caso de que existan
            for i in range(len(clusters_subset), len(axes)):
                fig.delaxes(axes[i])
        
            # Solo una etiqueta de eje y
            fig.text(0.01, 0.5, 'Frecuencia', va='center', ha='center', rotation='vertical', fontsize=26)
        
            # Solo una etiqueta de eje x
            fig.text(0.5, 0.001, 'Característica', va='center', ha='center', fontsize=26)
            
            # Ajustar las etiquetas de las características
            print(range(len(zeroconteonichos_encoded.index)))
            sys.stdout.flush()
            print(zeroconteonichos_encoded.index)
            sys.stdout.flush()
            plt.setp(axes, xticks=range(len(zeroconteonichos_encoded.index)), xticklabels=zeroconteonichos_encoded.index)
        
            # Añadir un título general
            fig.suptitle('Histograma {0}'.format(img + 1), fontsize=30)
            
            # Ajusta los márgenes de la figura
            plt.subplots_adjust(left=0.05, right=0.9, top=0.95, bottom=0.1)
            
            # Guardar la gráfica como un archivo PNG
            try:  #------------------------- // NUEVO \\ --------------------------#
                plt.savefig(histmlabelspng, format='png', dpi=300, bbox_inches='tight')   #------------------------- // NUEVO \\ --------------------------#
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
        x_labels = ['{0}\nCluster {1}'.format(caracteristicas[i % len(caracteristicas)], clusters[i // len(caracteristicas)]) for i in range(len(flattened_positions))]
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
            plt.savefig(histlabelspng, format='png', dpi=300, bbox_inches='tight')   #------------------------- // NUEVO \\ --------------------------#
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

# if __name__ == "__main__":
#     try:
#         confusion_graph()
#     except Exception as e:
#         sys.stderr.write("Ha ocurrido un error al usar la funcion confusion_graph(): {}\n".format(e))
#         sys.stderr.flush()


if __name__ == "__main__":
    try:
        confusion_graph()
    except Exception as e:
        # Obtener la información del traceback
        exc_type, exc_value, exc_traceback = sys.exc_info()
        
        # Imprimir el traceback completo
        print("Ha ocurrido un error al usar la función confusion_graph():")
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        
        # Escribir solo el mensaje de error en stderr
        sys.stderr.write("Error: {}\n".format(e))
        sys.stderr.flush()
