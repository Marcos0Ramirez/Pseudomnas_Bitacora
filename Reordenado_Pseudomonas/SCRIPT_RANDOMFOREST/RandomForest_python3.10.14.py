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
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, ConfusionMatrixDisplay
import matplotlib
matplotlib.use('Agg')  # Usar backend 'Agg' para entornos sin pantalla
import matplotlib.pyplot as plt
import sys
import traceback
import io
import codecs
from matplotlib.ticker import MaxNLocator









# direccion donde se encuentra el script
actual_script = os.path.abspath(__file__)
# Ahora extraemos la ruta del directorio
actual_directorio = os.path.dirname(actual_script)
# Nos cambiamos de ruta
os.chdir(actual_directorio)
print("Ya trabajando en directorio actual: ", os.getcwd())








def safe_precision_score(y_true, y_pred):
    try:
        return precision_score(y_true, y_pred, average='weighted')
    except ZeroDivisionError:
        return 0.0
    
    
    
    
    
    
    
    

if __name__ == "__main__":
    try:
        start_time = time.time()
        ###################### -- DIRECCIONES, ARCHIVOS Y PARAMETROS -- ######################
        siglas_exp =       "AP"
        test_or_original = "test"
        version =          "v1" 
        ################ -- INPUT -- ################
        rutabase=      "./INPUT/" # Ruta base
        filemtz =     f"cluster_pseudomonas_{test_or_original}.csv" #Nombre del archivo con la matriz
        fileclass =   f"{siglas_exp}_nicho_pseudomonas_{test_or_original}.txt" # Nombre de la tabla de clasificacion
        empty_nicho = 'Vacio'
        n_estima = 50
        porcen_comprobacion = 0.50
        estado_aleatorio1 = 99
        estado_aleatorio2 = 7
        
        rutamtz = os.path.join(rutabase, filemtz)
        rutaclass = os.path.join(rutabase, fileclass)
    
        ################ -- OUTPUT -- ################ 
        imgrutabase =   "OUTPUT"
        directo =      f"./{imgrutabase}_{siglas_exp}_{version}".upper()
        if not os.path.exists(directo):
            os.makedirs(directo)

        imgic =                 f"{version}_{siglas_exp}_{test_or_original}_clusters_importancia.png"
        imgic2 =                f"{version}_{siglas_exp}_{test_or_original}_clusters_importancia_log.png" 
        mtzconfusion =          f"{version}_{siglas_exp}_{test_or_original}_confmatrix.csv"
        mtzconfusion2 =         f"{version}_{siglas_exp}_{test_or_original}_confmatrix.png" # Nombre del histograma si solo son dos nichos que se estan comparando 
        conteonichos =          f"{version}_{siglas_exp}_{test_or_original}_contnichos.csv"
        conteonichos_encoded =  f"{version}_{siglas_exp}_{test_or_original}_contnichos_codificado.csv"
        etiquetas_codificadas = f"{version}_{siglas_exp}_{test_or_original}_nicho_etiquetas.csv"
        pr =                    f"{version}_{siglas_exp}_{test_or_original}_predprueba.csv"
        histot_50=              f"{version}_{siglas_exp}_{test_or_original}_histograma50labels_parte"
        histom_input =          "_{0}.png" #Mantener el {0} para las multiples imagenes si son mas de dos nichos
        
        
        rutaimportacara = os.path.join(directo, imgic)
        rutaimportacara2 = os.path.join(directo, imgic2) 
        rutaconfusion = os.path.join(directo, mtzconfusion)
        rutaconfusionpng = os.path.join(directo, mtzconfusion2)
        cluster100matriz = os.path.join(directo, conteonichos)
        cluster100matriz_encoded = os.path.join(directo, conteonichos_encoded)
        rutaetiquetas_codificadas = os.path.join(directo, etiquetas_codificadas)
        pred_g = os.path.join(directo, pr)
    
        
    
    
    
    
    
    
    
    
    
    
    
    
        ###################### -- EXTRACCION DE LOS DATOS -- ######################
        print("##### ABRIENDO TABLA DE CLASIFICACIONES #####", flush=True)
        # Tabla de clasificacion por nichos
        with codecs.open(rutaclass, 'r', encoding='utf-8') as csvclass:
                csvclase = csv.reader(csvclass, delimiter="\t")
                data = list(csvclase)
        encabezado = data[0]
        rows = data[1:]
        df_clase = pd.DataFrame(rows, columns=encabezado)
        print(df_clase, flush=True)
        
        
        
        
        
        print("##### EXTRAYENDO LOS GENOMAS #####", flush=True)
        # Extraemos la data
        # Matriz de frecuencias genomas-clusters
        chunks = []
        chunk_size = 100000  # Número de filas por chunk
        row_count = 0
        print("abriendo el archivo", flush=True)
        with codecs.open(rutamtz, 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            header = next(csvreader)
            print("empezamos con los chunks", flush=True)
            chunk = []
            for row in csvreader:
                chunk.append(row)
                row_count += 1
                if row_count % chunk_size == 0:
                    df_chunk = pd.DataFrame(chunk, columns=header)
                    chunks.append(df_chunk)
                    chunk = []
            print("tomamos los chunks", flush=True)
            if chunk:
                df_chunk = pd.DataFrame(chunk, columns=header)
                chunks.append(df_chunk)
        print("listo para concatenar todo", flush=True)
        df = pd.concat(chunks, ignore_index=True)
        print(df, flush=True)
        # Verificar la presencia de la columna 'Genomas' antes de eliminar columnas
        print("Columnas de df antes de eliminar:", df.columns, flush=True)
        if 'Genomas' not in df.columns:
            print("Error: 'Genomas' no se encuentra en df antes de eliminar columnas", flush=True)
        columns_to_drop = [col for col in df.columns if col == '' or col is None]
        print(columns_to_drop, flush=True)
        if len(columns_to_drop) > 0:
        	df.drop(columns=columns_to_drop, inplace=True)
        print(df, flush=True)
        # Verificar la presencia de la columna 'Genomas' después de eliminar columnas
        print("Columnas de df después de eliminar:", df.columns, flush=True)
        if 'Genomas' not in df.columns:
            print("Error: 'Genomas' no se encuentra en df después de eliminar columnas", flush=True)
        print("Ahora si las dimensiones de la matriz dataframe", flush=True)
        print(df.shape, flush=True)





        print("antes de concatenar las tablas", flush=True)
        mtz_class_caracteres = pd.merge(df.sort_values(by='Genomas'), df_clase.sort_values(by='Genomas'), on='Genomas')
        print(mtz_class_caracteres, flush=True)
        mtz_class_caracteres.set_index('Genomas', inplace=True, drop=False) 
        #mtz_class_caracteres.index.name = 'Genomas'
        
        print("Una vez que ya se hizo como indice la columna Genomas", flush=True)
        print(mtz_class_caracteres, flush=True)
        print(mtz_class_caracteres.index, flush=True)
        mtz_class_caracteres = mtz_class_caracteres[mtz_class_caracteres['Nicho'] != empty_nicho]
        mtz_idgen_nicho = pd.DataFrame(pd.Series(mtz_class_caracteres['Nicho'])) 
        print(mtz_class_caracteres.shape, flush=True)
        print(mtz_class_caracteres.head(), flush=True)
        
        
        
        
        
        
        
        
        
        
        
        
        ###################### -- PREPARACION DE LOS DATOS -- ######################
        print("##### PREPARAMOS LOS DATOS #####", flush=True)
        mtz_class_caracteres = pd.concat([mtz_class_caracteres.drop(columns=['Genomas'])], axis=1)
        print("los nichos los hacemos array", flush=True)
        labels = np.array(mtz_class_caracteres["Nicho"])
        la_enc = LabelEncoder()
        encoded_labels = la_enc.fit_transform(labels)
        etiquetas = labels.reshape(1, -1) 
        codified =  encoded_labels.reshape(1, -1) 
        class_etiquetas = np.concatenate((etiquetas, codified)).T 
        print(class_etiquetas, flush=True)
         
        np_clases_eitquetas=pd.DataFrame(class_etiquetas).drop_duplicates() 
        np_clases_eitquetas.to_csv(rutaetiquetas_codificadas, index=False)
        #print(mtz_class_caracteres)
        mtz_class_caracteres = mtz_class_caracteres.drop("Nicho", axis=1)
        #print(mtz_class_caracteres)
        mtz_class_caracteres_list = list(mtz_class_caracteres.columns)
        #print(mtz_class_caracteres_list)
        print("la matriz la hacemos arreglo", flush=True)
        mtz_class_caracteres = np.array(mtz_class_caracteres)
        train_mtz_class_caracteres, test_mtz_class_caracteres, train_labels, test_labels = train_test_split(mtz_class_caracteres, 
                                                                                                            encoded_labels, 
                                                                                                            test_size=porcen_comprobacion,  
                                                                                                            random_state=estado_aleatorio1) 
        
        print('Training Features Shape:', train_mtz_class_caracteres.shape, flush=True)
        print('Training Labels Shape:', train_labels.shape, flush=True)
        print('Testing Features Shape:', test_mtz_class_caracteres.shape, flush=True)
        print('Testing Labels Shape:', test_labels.shape, flush=True)
        
        
        
        
        
        
        
        
        
        
        
        ###################### -- ENTRENAMIENTO DEL MODELO -- ######################
        print("##### ENTRENANDO EL MODELO #####", flush=True)
        rf = RandomForestRegressor(n_estimators=n_estima, random_state=estado_aleatorio2) 
        rf.fit(train_mtz_class_caracteres, train_labels)
        
        ###################### -- Caracteristicas que son importantes -- ######################
        print("##### CLUSTERS DE IMPORTANCIA #####", flush=True)
        importancias = rf.feature_importances_
        feature_importances = pd.DataFrame(importancias, index=mtz_class_caracteres_list, columns=['Importancia'])
        feature_importances = feature_importances.sort_values(by='Importancia', ascending=False)
        
        print(feature_importances, flush=True)
        primeros100 = feature_importances.iloc[:100]
        print(primeros100, flush=True)
        
        
        
        
        
        
        
        
        ###################### -- Nichos por Clusters -- ######################
        print("##### PRIMEROS 100 CLUSTERS MAS IMPORTANTES #####", flush=True)
        #Tomamos los nombres de los clusters.
        cienclusters_importantes = " ".join(primeros100.index)  
        # Como la matriz esta en un numpy array, ahora toca extraer por el numero de las columna. 
        cienclusters_importantes = cienclusters_importantes.replace("Cluster", "").split(" ") 
        # Nombramos las columnas que necesitamos 
        clustercien = [mtz_class_caracteres[:,int(npcol)] for npcol in cienclusters_importantes if not npcol is None] 
        print("columnas 100; extraidas: ", clustercien, flush=True)
        #clustercien = [mtz_class_caracteres[npcol] for npcol in cienclusters_importantes if npcol in mtz_class_caracteres.columns]
        mtz_clustercien = pd.DataFrame(np.array(clustercien).T, columns=cienclusters_importantes, index=mtz_idgen_nicho.index) 
        # añadimos los nichos 
        mtz_clustercien['Nicho'] = mtz_idgen_nicho['Nicho'] 
        print(r"matriz mtz_clustercien creada\n", mtz_clustercien, flush=True)
        print(r"indices de mtz_clustercien \n", mtz_clustercien.index, flush=True)
        print(r"columnas de mtz_clustercien \n", mtz_clustercien.columns, flush=True)
        
        ###################### -- Nichos por Clusters: Hacemos el conteo -- ######################
        print("Continuamos hacia el conteo, juntando en indice y las 100 columnas", flush=True)
        u = mtz_idgen_nicho["Nicho"].unique() 
        c =list(mtz_clustercien.columns) 
        print("u", u, "c", c, flush=True)
        print("A eliminar la palabra Nicho de la lista c", flush=True)
        del c[c.index('Nicho')] 
        print(c, 'Nicho' in c, flush=True)
        #Creamos una matriz 
        print("matriz vacia, creandose", flush=True)
        zeroconteonichos = pd.DataFrame(0, index=u, columns=c) 
        print("matriz vacia, creada, continuamos con concatenar los 100 mejores cluster en la matriz vacia", flush=True)
        
        for i in u: 
            for j in c: 
                #print(i, j)
                ev = list(mtz_clustercien.index[mtz_clustercien['Nicho'] == i])
                #print(ev)
                # Asegúrate de que todos los elementos sean enteros
                values_to_sum = list(mtz_clustercien.loc[ev, j])
                #print("Valores a sumar (antes de convertir):", values_to_sum)
                values_to_sum = map(int, values_to_sum)
                #print("Valores a sumar (después de convertir):", values_to_sum)
                sumas = sum(values_to_sum)
                #print("sumas: ", sumas)
                zeroconteonichos.loc[i, j] = sumas
                #print("zeroconteonichos.loc[i,j]", zeroconteonichos.loc[i, j])
        print("##### GUARDANDING 100 MAS IMPORTANTES #####", flush=True)
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
    
        for i in u_encoded:
            for j in c:
                #print(i, j)
                #
                ev = list(mtz_clustercien_encod.index[mtz_clustercien_encod['Nicho'] == i])
                #print(ev)
                # Asegúrate de que todos los elementos sean enteros
                values_to_sum = list(mtz_clustercien_encod.loc[ev, j])
                #print("Valores a sumar (antes de convertir):", values_to_sum)
                values_to_sum = map(int, values_to_sum)
                #print("Valores a sumar (después de convertir):", values_to_sum)
                sumas = sum(values_to_sum)
                #print("sumas: ", sumas)
                zeroconteonichos_encoded.loc[i, j] = sumas
                #print("zeroconteonichos.loc[i,j]", zeroconteonichos.loc[i, j])
        print(zeroconteonichos_encoded.shape, flush=True)
        # print("##### GUARDANDING 100 MAS IMPORTANTES CODIFICADOS #####")
        # zeroconteonichos_encoded.to_csv(cluster100matriz_encoded)
        
        
        
        
        
        
        
                
        ###################### -- GRAFICOS -- ######################
        # =============================================================================
        
        # Histograma, mayor a 2 nichos
        if len(zeroconteonichos.index) > 2:
            # Codificacion en numeros, los indices
            # MUCHOS HISTOGRAMAS
            # Número total de clústeres
            print("HISTOGRAMA CON MUCHOS NICHOS", flush=True)
            num_clusters = zeroconteonichos_encoded.shape[1]
            # Dividir en grupos de 25 clústeres
            clusters_per_image = 25
            num_images = num_clusters // clusters_per_image
            # Lista de colores para los histogramas
            colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightpink']
            for img in range(num_images):
                histom = histom_input.format(img + 1)
                histmlabelspng = os.path.join(directo, histom)
                start_idx = img * clusters_per_image
                end_idx = start_idx + clusters_per_image
                clusters_subset = zeroconteonichos_encoded.columns[start_idx:end_idx]
                # Crear subplots: número de filas y columnas
                num_cols = 5  # Número de columnas deseadas en el grid
                num_rows = (clusters_per_image + num_cols - 1) // num_cols  # Calcular el número de filas
                fig, axes = plt.subplots(num_rows, num_cols, figsize=(25, num_rows * 5), sharex=True, sharey=True)
                axes = axes.flatten()
                print("Toca procesar las posiciones de las imagenes", flush=True)
                for i, cluster in enumerate(clusters_subset):
                    print(i, cluster, type(i), type(cluster), flush=True)
                    #cluster=int(cluster)
                    #print(i, cluster, type(i), type(cluster))
                    #print(zeroconteonichos.index, type(zeroconteonichos.index), zeroconteonichos[cluster], type(zeroconteonichos[cluster]))
                    print("Ordenando la lista: ", sorted(list(zeroconteonichos_encoded.index)), flush=True)
                    axes[i].bar(sorted(list(zeroconteonichos_encoded.index)), zeroconteonichos_encoded[cluster], color=colors[i % len(colors)])
                    axes[i].set_title(cluster, fontsize=20)
                    #plt.setp(axes[i].get_xticklabels(), rotation=90, fontsize=20)
                    axes[i].tick_params(axis='x', labelsize=20)  # Aumentar tamaño de fuente de los números del eje x rotation=90,
                    axes[i].tick_params(axis='y', labelsize=25)  # Aumentar tamaño de fuente de los números del eje y
        
                print("Vamos con los ejes", flush=True)
                # Remover ejes adicionales en caso de que existan
                for i in range(len(clusters_subset), len(axes)):
                    fig.delaxes(axes[i])
                # Solo una etiqueta de eje y
                fig.text(0.01, 0.5, 'Frecuencia', va='center', ha='center', rotation='vertical', fontsize=26)
                # Solo una etiqueta de eje x
                fig.text(0.5, 0.001, 'Característica', va='center', ha='center', fontsize=26)
                # Ajustar las etiquetas de las características
                print(range(len(zeroconteonichos_encoded.index)), flush=True)
                print(zeroconteonichos_encoded.index, flush=True)
                plt.setp(axes, xticks=range(len(zeroconteonichos_encoded.index)), xticklabels=zeroconteonichos_encoded.index)
                # Añadir un título general
                fig.suptitle('Histograma {0}'.format(img + 1), fontsize=30)
                # Ajusta los márgenes de la figura
                plt.subplots_adjust(left=0.05, right=0.9, top=0.95, bottom=0.1)
                # Guardar la gráfica como un archivo PNG
                try:  
                    plt.savefig(histmlabelspng, format='png', dpi=300, bbox_inches='tight')   
                    plt.close(fig)
                    print("Imagen guardada exitosamente", flush=True)  
                except Exception as e:  
                    sys.stderr.write("Error al guardar la imagen: {}\n".format(e))  
                    sys.stderr.flush()  
        else:
            # OPCION 11
            # UN HISTOGRAMA (dos filas)
            # Apilar los datos para combinarlos en una sola serie
            h3_o = pd.DataFrame(np.array([[i, j, int(zeroconteonichos.loc[i,j])] for j in zeroconteonichos.columns if j for i in zeroconteonichos.index if i]))
            h3_o.columns = ['Caracteristica', 'Cluster', 'Frecuencia']
            
            for i in [0, 50, 100, 150]:
                h3 = h3_o[i:i+50]
                h3 = h3.reset_index(drop=True)
                h3['Frecuencia'] = h3['Frecuencia'].astype(int)
                y_min, y_max = 0, int(max(h3['Frecuencia'])) + 2
                histot_50_2=f"_{i}.png"
                pegadin= histot_50 + histot_50_2
                print(pegadin, flush=True)
                histt50labelspang = os.path.join(directo, pegadin)
                print(histt50labelspang, flush=True)
                print(h3, flush=True)
                # Crear el histograma
                plt.figure(figsize=(10, 4))
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
                print(len(par), flush=True)
                print(len(impar), flush=True)
                
                # Dibujar las barras
                for i, cluster in enumerate(clusters):
                    print("###########################", flush=True)
                    cluster_data = h3[h3['Cluster'] == cluster]
                    
                    pos = [positions[j][i] for j in range(len(caracteristicas))]
                    freqs =[]
                    for i in list(cluster_data['Frecuencia']):
                        freqs.append(i)
                    #freqsantes = [int(i) for i in list(cluster_data['Frecuencia']) if i]
                    freqs = pd.Series(freqs)
                    print("Cluster data \n", cluster_data, flush=True)
                    print("Posiciones: ", pos, flush=True)
                    print("Frecuencias: ", list(cluster_data['Frecuencia']), flush=True)
                    print("Longitud de las frecuencias: ", len(freqs), flush=True)
                    if len(freqs) == len(pos):
                        plt.bar(pos, freqs, width=bar_width, color=[colors[0],colors[1]])
                    else:
                        print("Se diferencian por longitudes las frecuencias con longitud ", len(freqs), "y la longitud de las posisciones con longitud ", len(pos), flush=True)
                        exit()
                
                # Ajustar las posiciones del eje x y las etiquetas
                #flattened_positions = [p for sublist in positions2 for p in sublist]
                flattened_positions = [p for sublist in positions for p in sublist]
                x_labels = [f'{caracteristicas[i]}\nCluster {clusters[j]}' for i in range(len(caracteristicas)) for j in range(len(clusters))]
                plt.xticks(flattened_positions, x_labels, rotation=90, fontsize=5, fontweight='bold')
                # Ajustar el eje y manualmente para asegurar consistencia
                plt.ylim(y_min, y_max)
                #plt.yticks(np.arange(y_min, y_max, 300))
                plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True, prune='both'))
                # Añadir etiquetas y leyenda con colores personalizados
                legend_patches = [
                    plt.Rectangle((0, 0), 1, 1, fc='blue', alpha=0.7),
                    plt.Rectangle((0, 0), 1, 1, fc='orange', alpha=0.7)
                ]
                plt.legend(legend_patches, caracteristicas)
                # Añadir etiquetas y leyenda
                plt.xlabel('Característica y Clúster')
                plt.ylabel('Frecuencia')
                plt.title(f'Frecuencias por Característica y Clúster ({caracteristicas[0]} y {caracteristicas[1]})')
                #plt.show()
                # Ajustar el diseño para que no se recorten los elementos
                plt.tight_layout()
                # Guardar la gráfica como un archivo PNG
                plt.savefig(histt50labelspang, format='png', dpi=300, bbox_inches='tight')
                plt.close()
    
    
    
    
    
    
    
    
            # =============================================================================
            # Crear la figura y el objeto Axes
            fig, ax = plt.subplots(figsize=(12, 4))
            # Crear el gráfico de barras en el objeto Axes
            primeros100.plot(kind='bar', ax=ax)
            # Título y etiquetas de los ejes
            ax.set_title(f'Importancia de las características NORMAL, \ncomparativa ({" ".join(caracteristicas)})')
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
            ax.set_title(f'Importancia de las características LOGARITMICA, \ncomparativa ({" ".join(caracteristicas)})')
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
            predicciones_prueba = {"Originales": test_labels,
                                   "Predicciones": prediction_discrete}
            
            pred_guardado = pd.DataFrame(predicciones_prueba)
            pred_guardado.to_csv(pred_g)
            mc = confusion_matrix(test_labels, prediction_discrete)
            #tn, fp, fn, tp = confusion_matrix(test_labels, prediction_discrete).ravel()
            #print(tn, fp, fn, tp)
            cero=str("".join(np_clases_eitquetas.loc[np_clases_eitquetas[1] == 0][0].tolist()))
            uno=str("".join(np_clases_eitquetas.loc[np_clases_eitquetas[1] == 1][0].tolist()))
            mc_df = pd.DataFrame(mc)
            mc_df = mc_df.rename(columns={
                '0': f'{cero}',
                '1': f'{uno}'
            })
            mc_df.index = [f'{cero}', f'{uno}']
            mc_df.to_csv(rutaconfusion)
            conf_matrix = mc_df.values
            ##################### -- Visualizacion de la Matriz de Confusion -- ######################
            # Crear la visualización de la matriz de confusión
            disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=[f'{cero}', f'{uno}'])
            disp.plot()
            
            # Ajustar el diseño para que no se recorten los elementos
            plt.tight_layout()
    
            # Guardar la gráfica como un archivo PNG con el tamaño y resolución especificados
            plt.savefig(rutaconfusionpng, format='png', dpi=300, bbox_inches='tight')
    
            try:
                mc_df.to_csv(rutaconfusion)
                print("Matriz de confusión guardada exitosamente", flush=True)
            except Exception as e:
                sys.stderr.write(f"Error al guardar la matriz de confusión: {e}\n")
                sys.stderr.flush()
            
            try:
                accuracy = accuracy_score(test_labels, prediction_discrete)
                precision = safe_precision_score(test_labels, prediction_discrete)
                recall = recall_score(test_labels, prediction_discrete, average='weighted')
                f1 = f1_score(test_labels, prediction_discrete, average='weighted')
                print("Accuracy:", accuracy, flush=True)
                print("Precision:", precision, flush=True)
                print("Recall:", recall, flush=True)
                print("F1 Score:", f1, flush=True)
                
            except Exception as e:
                sys.stderr.write(f"Error al calcular las métricas: {e}\n")
                sys.stderr.flush()
            
            elapsed_time = time.time() - start_time
            print("Elapsed time to compute the importances: {:.3f} seconds".format(elapsed_time), flush=True)
        









    except Exception as e:
        # Obtener la información del traceback
        exc_type, exc_value, exc_traceback = sys.exc_info()
        # Imprimir el traceback completo
        print("Ha ocurrido un error al usar la función confusion_graph():", e, flush=True)
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        # Escribir solo el mensaje de error en stderr
        sys.stderr.write(f"Error: {e}\n")
        sys.stderr.flush()

# =============================================================================
# 
# from sklearn.metrics import precision_score, accuracy_score, recall_score, f1_score
# 
# # =============================================================================
# # # Valores verdaderos
# # y_true = [0, 1, 2, 0, 1, 2, 2, 1, 0, 0]
# # 
# # # Predicciones del modelo
# # y_pred = [0, 2, 1, 0, 0, 2, 2, 1, 0, 1]
# # =============================================================================
# # Valores verdaderos
# y_true = [1, 0, 1, 2, 0, 1, 2, 2, 0, 1]
# 
# # Predicciones del modelo
# y_pred = [1, 0, 1, 1, 0, 2, 2, 0, 0, 1]
# accuracy = accuracy_score(y_true, y_pred)
# print(f'accuracy {accuracy:.2f}')
# 
# recall = recall_score(y_true, y_pred, average='weighted')
# print(f'recall {recall:.2f}')
# 
# f1 = f1_score(y_true, y_pred, average='weighted')
# print(f'f1 {f1:.2f}')
# 
# # Calcular la precisión ponderada
# precision_weighted = precision_score(y_true, y_pred, average='weighted')
# print(f'Precision ponderada: {precision_weighted:.2f}')
# 
# =============================================================================


