# Sera la bitacora de modificaciones de Random Forest.
_Finalmente se añadira a la carpeta final con todo y todo._

## FECHA 1 DE DICIEMBRE DEL 2024
Con el fin de optimizar el proceso de creacion del codigo, se adaptara buena parte del script a este.
Se instalo miniconda para la maquina virtual de Ubunut en Windows, de la siguiente liga: https://docs.anaconda.com/miniconda/install/

Por default se instalo python 3.12.7 y solo queda instalar los paquetes scikit-sklearn, numpy, pandas y matplotlib.pyplot
```
conda install -c conda-forge scikit-learn numpy pandas matplotlib seaborn
```

Si tienes mas versiones de python y no quieres alterarlas con instalar nuevos paquetes añade la version del python que quieres despues de los paquetes.
 
Ejemplo
```
conda install -c conda-forge scikit-learn numpy pandas matplotlib seaborn python=3.12.7
```
En el camino se hicieron estos reajustes, dentro del ambiente `base`, debido a que siempre habia una advertencia, sobre que no se reconocia un archivo de `numpy`, entonces se volvio a reinstalar los paquetes de `pandas` y `numpy`, para despues hacer una configuracion y actualizar los paquetes. Por otra parte aparecio que no se reconocia correctamente el paquete `pyexpat` y por tanto se volvio a forzar su instalacion y funciono.
```
conda remove pandas
conda remove numpy
conda install numpy pandas
conda config --set solver classic
conda update pandas numpy


conda install --force-reinstall expat
```

Estas fueron las modifiaciones:
Se copio y pego esto del codigo anterior, añadiendo el paquete `re`
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos las librerias necesarias
import time
import datetime
import pandas as pd
import numpy as np
import os
import csv
import sys
import traceback
import io
import re
import codecs
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# direccion donde se encuentra el script
actual_script = os.path.abspath(__file__)
# Ahora extraemos la ruta del directorio
actual_directorio = os.path.dirname(actual_script)
```
Se añadio la fecha y hora de ejecucion. Mismo otra ruta para guardar las importancias `csvimportancia`.
```
print("")
print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡")
# Nos cambiamos de ruta
os.chdir(actual_directorio)
print("Ya trabajando en directorio actual: ", os.getcwd())
hora_actual = datetime.datetime.now()
print("Fecha y hora de ejecución: ", hora_actual)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")

if __name__ == "__main__":
	try:
		start_time = time.time()
		###################### -- DIRECCIONES, ARCHIVOS Y PARAMETROS -- ######################
		siglas_exp =       "AP"
		test_or_original = "test"
		version =          "v1" 
		################ -- INPUT -- ################
		rutabase=      "./MicroSet/INPUT/" # Ruta base
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
		imgrutabase =   "./MicroSet/OUTPUT"
		directo =      f"./{imgrutabase}_{siglas_exp}_{version}".upper()
		if not os.path.exists(directo):
		    os.makedirs(directo)

		imgic =                 f"{version}_{siglas_exp}_{test_or_original}_clusters_importancia.png"
		imgic2 =                f"{version}_{siglas_exp}_{test_or_original}_clusters_importancia_log.png"
		csvimportancia =        f"{version}_{siglas_exp}_{test_or_original}_clusters_importancia_log.csv"
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
		logimportcsv = os.path.join(directo, csvimportancia)
		rutaconfusion = os.path.join(directo, mtzconfusion)
		rutaconfusionpng = os.path.join(directo, mtzconfusion2)
		cluster100matriz = os.path.join(directo, conteonichos)
		cluster100matriz_encoded = os.path.join(directo, conteonichos_encoded)
		rutaetiquetas_codificadas = os.path.join(directo, etiquetas_codificadas)
		pred_g = os.path.join(directo, pr)
```

Se eliminaron algunos print que lo hacian repetitivo, solo añadiendo los necesarios
```
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
		print(df_clase.shape, flush=True)

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
		#print("Columnas de df antes de eliminar:", df.columns, flush=True)
		if 'Genomas' not in df.columns:
		    print("Error: 'Genomas' no se encuentra en df antes de eliminar columnas", flush=True)
		columns_to_drop = [col for col in df.columns if col == '' or col is None]
		# print(columns_to_drop, flush=True)
		if len(columns_to_drop) > 0:
			df.drop(columns=columns_to_drop, inplace=True)


		# Verificar la presencia de la columna 'Genomas' después de eliminar columnas
		# print("Columnas de df después de eliminar:", df.columns, flush=True)
		if 'Genomas' not in df.columns:
		    print("Error: 'Genomas' no se encuentra en df después de eliminar columnas", flush=True)
		print("Ahora si las dimensiones de la matriz dataframe", flush=True)
		print(df.shape, flush=True)
```

Lo mismo que el bloque anterior, ademas de que se movieron ciertos bloques para ahorrar algunos pasos. Y por otra parte se modifico la salida del CSV con los nichos codificados.
```
		###################### -- PREPARACION DE LOS DATOS -- ######################
		print("##### PREPARAMOS LOS DATOS #####", flush=True)
		print("Configurando tablas...", flush=True)
		mtz_class_caracteres = pd.merge(df.sort_values(by='Genomas'), df_clase.sort_values(by='Genomas'), on='Genomas')
		#print(mtz_class_caracteres, flush=True)
		mtz_class_caracteres.set_index('Genomas', inplace=True, drop=False) 
		#mtz_class_caracteres.index.name = 'Genomas'

		print("Columna Genomas, convertida como indice", flush=True)
		#print(mtz_class_caracteres, flush=True)
		#print(mtz_class_caracteres.index, flush=True)
		mtz_class_caracteres = mtz_class_caracteres[mtz_class_caracteres['Nicho'] != empty_nicho]
		mtz_idgen_nicho = pd.DataFrame(pd.Series(mtz_class_caracteres['Nicho'])) 

		print("Eliminamos columna Genomas", flush=True)
		mtz_class_caracteres = pd.concat([mtz_class_caracteres.drop(columns=['Genomas'])], axis=1)
		print("Forma final: ", flush=True)
		print(mtz_class_caracteres.shape, flush=True)
		print(mtz_class_caracteres.head(), flush=True)

		print("Los nichos los codificamos en numeros", flush=True)
		labels = np.array(mtz_class_caracteres["Nicho"])
		la_enc = LabelEncoder()
		encoded_labels = la_enc.fit_transform(labels)
		etiquetas = labels.reshape(1, -1) 
		codified =  encoded_labels.reshape(1, -1) 
		class_etiquetas = np.concatenate((etiquetas, codified)).T
		np_clases_eitquetas=pd.DataFrame(class_etiquetas).drop_duplicates()
		np_clases_eitquetas.columns = ["Nicho", "Codificacion"]
		print("Aqui las respectivas codificaciones", flush=True)
		print(np_clases_eitquetas, flush=True)
		print("Guardamos en un csv...", flush=True)
		np_clases_eitquetas.to_csv(rutaetiquetas_codificadas, index=False)
		print("De la matriz eliminamos la columna nicho", flush=True)
		mtz_class_caracteres = mtz_class_caracteres.drop("Nicho", axis=1)
		#print(mtz_class_caracteres)
		mtz_class_caracteres_list = list(mtz_class_caracteres.columns)
		#print(mtz_class_caracteres_list)
		print("DataFrame a Numpy array", flush=True)
		mtz_class_caracteres = np.array(mtz_class_caracteres)
```


**_Parte mas importante, se modifico `RandomForestRegressor` por `RandomForestClassifier`._** Se eliminaron algunas partes del codigo como prints y partes repetitivas, reduciendo algunas operaciones. Ademas de ajustar en la tabla de importancia, el calculo en su version _log10_. Finalmente se añadio modificaciones a la tabla importancia, añadiendo la version numpy.log10 (logaritmica) de la importancia dando como resultado el exponente sobre 10.
```
		###################### -- ENTRENAMIENTO DEL MODELO -- ######################
		print("##### ENTRENANDO EL MODELO #####", flush=True)
		print("Dividimos los datos en entrenamiento (train) y prueba (test), tanto features como labels", flush=True)
		train_mtz_class_caracteres, test_mtz_class_caracteres, train_labels, test_labels = train_test_split(mtz_class_caracteres, 
		                                                                                                    encoded_labels, 
		                                                                                                    test_size=porcen_comprobacion,  
		                                                                                                    random_state=estado_aleatorio1) 
		rf = RandomForestClassifier(n_estimators=n_estima, random_state=estado_aleatorio2) 
		rf.fit(train_mtz_class_caracteres, train_labels)


		###################### -- Caracteristicas que son importantes -- ######################
		print("##### CLUSTERS DE IMPORTANCIA #####", flush=True)
		print("En base a la importancia de Gini, sacamos la importancia de los clusters", flush=True)
		importancias = rf.feature_importances_
		feature_importances = pd.DataFrame(importancias, index=mtz_class_caracteres_list, columns=['Importancia'])
		feature_importances = feature_importances.sort_values(by='Importancia', ascending=False)

		#print(feature_importances, flush=True)
		print("Se extraen los primeros 100...", flush=True)
		primeros100 = feature_importances.iloc[:100]
		print("Los clusters de indices a columna: ", flush=True)
		primeros100 = primeros100.reset_index()
		primeros100.columns = ["Clusters", "Importancia"]

		print("Remplaamos la palabra cluster, por solo el numero que lo constituye", flush=True)
		clusterno = ", ".join(primeros100['Clusters'])
		num = re.findall("[0-9]+", clusterno)
		primeros100["Clusters"] = num # Solo la version normal
		print(primeros100, flush=True)
		# Aplicar log10 a la columna de interés (asegurando que no haya valores <= 0)
		primeros100['Importancia_Log10'] = np.log10(primeros100['Importancia'].replace(0, np.nan)) # Añadimos version logaritmica
		primeros100['Importancia_Log10'] = primeros100['Importancia_Log10'].replace(np.nan, 0)
		print(primeros100, flush=True)
		print("Guardamos las importancias en la version logaritmica como CSV y PNG... ", flush=True)
		print("Importancias en CSV...", flush=True)
		primeros100.to_csv(logimportcsv, index=False)


		#
		#
		# Especificar las columnas
		x_col = 'Clusters'  # Columna para el eje X
		y_col = 'Importancia_Log10'  # Columna para el eje Y (puede ser 'Importancia' o 'Importancia_Log10')
		# Crear la figura
		fig, ax = plt.subplots(figsize=(12, 4))
		# Graficar las barras usando las columnas específicas
		ax.bar(primeros100[x_col], primeros100[y_col], color='skyblue')  # Usar las columnas especificadas
		# Título y etiquetas
		ax.set_title(f'Importancia de las características escala Logaritmica')
		ax.set_xlabel('Clusters')
		ax.set_ylabel('Importancia logarítmica')
		# Ajustar las etiquetas del eje X
		ax.set_xticks(range(len(primeros100[x_col])))
		ax.set_xticklabels(primeros100[x_col], rotation=90, fontsize=6, fontweight='bold')
		# Ajustar el diseño para evitar recortes
		plt.tight_layout()
		# Guardar el gráfico como archivo PNG
		plt.savefig(rutaimportacara2, format='png', dpi=300, bbox_inches='tight')
		#
		#


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


print("-----------------------------------------------------------------------------------------------")
print("")
```


## FECHA 2 DE DICIEMBRE DEL 2024

### Grafico de Arboles
Adaptacion de codigo para graficar arboles de decision generados por Random Forest:
https://stackoverflow.com/questions/40155128/plot-trees-for-a-random-forest-in-python-with-scikit-learn



### Grafico de Superficie de Decisiones
Encontre que hay un grafico para implemetar, se llama `decision surfaces`, encontrado en la siguiente liga https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html y se explica por medio de este blog: https://hackernoon.com/lang/es/como-trazar-un-limite-de-decision-para-algoritmos-de-aprendizaje-maquina-en-python-3o1n3w07 la funcion de este grafico. El cual cito:

> Los algoritmos de clasificación aprenden a asignar etiquetas de clase a ejemplos (observaciones o puntos de datos), aunque sus decisiones pueden parecer opacas.
> Un diagnóstico popular para comprender las decisiones tomadas por un algoritmo de clasificación es la superficie de decisión. Esta es una gráfica que muestra cómo un algoritmo de aprendizaje automático entrenado predice una cuadrícula gruesa en el espacio de características de entrada.
> ***Un gráfico de superficie de decisión es una herramienta poderosa para comprender cómo un modelo determinado "ve" la tarea de predicción y cómo ha decidido dividir el espacio de características de entrada por etiqueta de clase.***

Que en mis palabras

La premisa, es que los **algoritmos de aprendiza automatico**, aprenden a asignar etiquetas en base a su entrenamiento con las observaciones.
Este grafico, puede ser implementado en el modelo RandomForesClassifier https://qu4nt.github.io/sklearn-doc-es/auto_examples/ensemble/plot_forest_iris.html
Ejmplo con DecisionTreeClassifier https://qu4nt.github.io/sklearn-doc-es/auto_examples/tree/plot_iris_dtc.html#sphx-glr-auto-examples-tree-plot-iris-dtc-py, el cual indica como es que el modelo, considera a que clase se asocia de acuerdo a una combinacion especifica de caracteristicas.

En caso de que la clasificacion por Random Fores hace muchos arboles, cada uno puede generar una superficie de decision diferente. Pero en si RandomForestClassifier combina el resultado de todos los arboles generados, lo cual al usar todos la hace mas robusta y menos propensa a sobreajustes. Asi al entrenar y predecir, asigna una clase con un promedio de las predicciones de los arboles y la superficie de decision resultante muestra como esas clases se distribuyen a traves de las combinaciones de las caracteristicas. Nota, las caracteristicas se toman de manera aleatoria para generar la malla.

### Support-Vector Network
En el articulo de Vapnik y Cortes en 2021, proponen el termino de "***support-vector network***" como una nueva tecnica de aprendizaje de maquinas para problemas de clasificacion de dos grupos. Enfoque del articulo:

> The support-vector network implements the following idea: it maps the input vectors into some high dimensional feature space Z through some non-linear mapping chosen a priori. In this space a linear decision surface is constructed with special properties that ensure high generalization ability of the network.

En una vision general, hay dos problemas que abarca conceptual y tecnico respectivamente: ¿Como encontrar un hiperplano de separacion que generalice bien? Y computacionalmente, ¿como tratar con un espacios de muchas dimensiones?
La conceptual, ya fue hecha para clases separables. Donde definien a un hiperplano como una funcion de decision linear con el margen maximo de dos clases. Y el caso de hiperplanos optimos, son que toma entre una pequeña cantidad de datos de entrenamiento son los vectores de soporte, los cuales determinan el margen.

Cabe destacar que el termino Superficie de decisiones (***"Decision Surface"***),

Vapnik, V., & Cortes, C. (1995). Support Vector Networks, machine learning 20, 273-297.
---

### Codigo eliminado
Una vez confirmado que se puede usar, se paso el codigo restante para las matrices de confusion y graficos de distribucion de nichos y eliminacion de codigo del script anterior, eliminando esto de codigo:
```
# Bloque 1
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

#################################################################################################################################
# Bloque 2
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

#################################################################################################################################
Bloque 3
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

```
Lo restante, se dejo y adapto al codigo nuevo

## FECHA 3 DE DICIEMBRE DEL 2024
El dia de hoy se eliminaron algunas variables que no tenian uso en la nueva adaptacion, mismo que se cambiaron los nombres de algunas variables a los nombres de variables que usa en los ejemplos del paquete `scikit-learn`:

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos las librerias necesarias
import time
import datetime
import pandas as pd
import numpy as np
import os
import csv
import sys
import traceback
import io
import re
import codecs
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, ConfusionMatrixDisplay, classification_report
from sklearn import tree
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# direccion donde se encuentra el script
actual_script = os.path.abspath(__file__)
# Ahora extraemos la ruta del directorio
actual_directorio = os.path.dirname(actual_script)

print("")
print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡")
# Nos cambiamos de ruta
os.chdir(actual_directorio)
print("Ya trabajando en directorio actual: ", os.getcwd())
hora_actual = datetime.datetime.now()
print("Fecha y hora de ejecución: ", hora_actual)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")

if __name__ == "__main__":
	try:
		start_time = time.time()
		###################### -- DIRECCIONES, ARCHIVOS Y PARAMETROS -- ######################
		siglas_exp =       "AP"
		test_or_original = "test"
		version =          "v3" 
		################ -- INPUT -- ################
		rutabase=                "./MicroSet/INPUT/" # Ruta base
		filemtz =                f"cluster_pseudomonas_{test_or_original}.csv" #Nombre del archivo con la matriz
		fileclass =              f"{siglas_exp}_nicho_pseudomonas_{test_or_original}.txt" # Nombre de la tabla de clasificacion
		empty_nicho =            'Vacio'
		n_estima =                50
		test_size =               0.50
		random_state_split =      99
		random_state_classifier = 7

		rutamtz = os.path.join(rutabase, filemtz)
		rutaclass = os.path.join(rutabase, fileclass)

		################ -- OUTPUT FOLDERS -- ################ 
		imgrutabase =   "./MicroSet/OUTPUT"
		directo =       f"./{imgrutabase}_{siglas_exp}_{version}_{test_or_original}".upper()
		if not os.path.exists(directo):
			os.makedirs(directo)

		tree_ds =       f"tree_decision_surfaces_{siglas_exp}_{version}_{test_or_original}".upper()
		rutatree_ds =   os.path.join(directo, tree_ds)
		if not os.path.exists(rutatree_ds):
			os.makedirs(rutatree_ds)




		lcodcsv =               f"{version}_{siglas_exp}_{test_or_original}_codificacionichos.csv"
		ilogpng =               f"{version}_{siglas_exp}_{test_or_original}_clusters_importancia_log.png"
		ilogcsv =               f"{version}_{siglas_exp}_{test_or_original}_clusters_importancia_log.csv"
		confcsv =               f"{version}_{siglas_exp}_{test_or_original}_confmatrix.csv"
		confpng =               f"{version}_{siglas_exp}_{test_or_original}_confmatrix.png" # Nombre del histograma si solo son dos nichos que se estan comparando 
		distnichocsv =          f"{version}_{siglas_exp}_{test_or_original}_distribucionichos.csv"
		histot_50=              f"{version}_{siglas_exp}_{test_or_original}_distribucionichos_parte"
		ypred =                 f"{version}_{siglas_exp}_{test_or_original}_ypredicciones.csv"
		report =                f"{version}_{siglas_exp}_{test_or_original}_ypredreport.csv"
		arbol =                 f"{version}_{siglas_exp}_{test_or_original}_tree"
		dsurface =              f"{version}_{siglas_exp}_{test_or_original}_decision_surface_tree"


		rutalcodcsv =           os.path.join(directo, lcodcsv)
		rutaimplogpng =         os.path.join(directo, ilogpng)
		rutaimplogcsv =         os.path.join(directo, ilogcsv)
		rutaconfcsv =           os.path.join(directo, confcsv)
		rutaconfpng =           os.path.join(directo, confpng)
		rutadistnichocsv =      os.path.join(directo, distnichocsv)
		rutaypred =             os.path.join(directo, ypred)
		rutareport =            os.path.join(directo, report)
		rutaarbol =             os.path.join(rutatree_ds, arbol)
		rutadsurface =          os.path.join(rutatree_ds, dsurface)



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
		print(df_clase.shape, flush=True)

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
		#print("Columnas de df antes de eliminar:", df.columns, flush=True)
		if 'Genomas' not in df.columns:
		    print("Error: 'Genomas' no se encuentra en df antes de eliminar columnas", flush=True)
		coldrop = [col for col in df.columns if col == '' or col is None]
		# print(coldrop, flush=True)
		if len(coldrop) > 0:
			df.drop(columns=coldrop, inplace=True)


		# Verificar la presencia de la columna 'Genomas' después de eliminar columnas
		# print("Columnas de df después de eliminar:", df.columns, flush=True)
		if 'Genomas' not in df.columns:
		    print("Error: 'Genomas' no se encuentra en df después de eliminar columnas", flush=True)
		print("Ahora si las dimensiones de la matriz dataframe", flush=True)
		print(df.shape, flush=True)




		###################### -- PREPARACION DE LOS DATOS -- ######################
		print("##### PREPARAMOS LOS DATOS #####", flush=True)
		print("Configurando tablas...", flush=True)
		df = pd.merge(df.sort_values(by='Genomas'), df_clase.sort_values(by='Genomas'), on='Genomas')
		#print(df, flush=True)
		df.set_index('Genomas', inplace=True, drop=False) 
		#df.index.name = 'Genomas'

		print("Columna Genomas, convertida como indice", flush=True)
		#print(df, flush=True)
		#print(df.index, flush=True)
		df = df[df['Nicho'] != empty_nicho]
		Y = pd.DataFrame(pd.Series(df['Nicho'])) 

		print("Eliminamos columna Genomas", flush=True)
		df = pd.concat([df.drop(columns=['Genomas'])], axis=1)
		print("Forma final: ", flush=True)
		print(df.shape, flush=True)
		print(df.head(), flush=True)

		print("Los nichos los codificamos en numeros", flush=True)
		Y_observados = np.array(df["Nicho"])
		la_enc = LabelEncoder()
		Y_encoded = la_enc.fit_transform(Y_observados)
		Y_observados_resh = Y_observados.reshape(1, -1) 
		Y_encoded_resh =  Y_encoded.reshape(1, -1) 
		Y_observados_encoded = np.concatenate((Y_observados_resh, Y_encoded_resh)).T
		np_clases_eitquetas=pd.DataFrame(Y_observados_encoded).drop_duplicates()
		np_clases_eitquetas.columns = ["Nicho", "Codificacion"]
		print("Aqui las respectivas codificaciones", flush=True)
		print(np_clases_eitquetas, flush=True)
		print("Guardamos en un csv...", flush=True)
		np_clases_eitquetas.to_csv(rutalcodcsv, index=False)
		print("De la matriz eliminamos la columna nicho", flush=True)
		X = df.drop("Nicho", axis=1)
		#print(X)
		X_clusters = list(X.columns)
		#print(X_clusters)
		print("DataFrame a Numpy array", flush=True)
		Xnp = np.array(X).astype(int)
		print(Xnp, flush=True)
		print(Y_encoded, flush=True)






		###################### -- ENTRENAMIENTO DEL MODELO -- ######################
		print("##### ENTRENANDO EL MODELO #####", flush=True)
		print("Dividimos los datos en entrenamiento (train) y prueba (test), tanto features como labels", flush=True)
		X_train, X_test, Y_train, Y_test = train_test_split(
															Xnp, 
															Y_encoded, 
															test_size=test_size,  
															random_state=random_state_split
															)

		rf = RandomForestClassifier(n_estimators=n_estima, random_state=random_state_classifier) 
		rf.fit(X_train, Y_train)






		###################### -- CLUSTERS IMPORTANTES -- ######################
		print("##### CLUSTERS DE IMPORTANCIA #####", flush=True)
		print("En base a la importancia de Gini, sacamos la importancia de los clusters", flush=True)
		importancias = rf.feature_importances_
		feature_importances = pd.DataFrame(importancias, index=X_clusters, columns=['Importancia'])
		feature_importances = feature_importances.sort_values(by='Importancia', ascending=False)

		print("Se extraen los primeros 100...", flush=True)
		df_primeros100 = feature_importances.iloc[:100]
		print("Los clusters de indices a columna: ", flush=True)
		df_primeros100 = df_primeros100.reset_index()
		df_primeros100.columns = ["Clusters", "Importancia"]

		print("Remplaamos la palabra cluster, por solo el numero que lo constituye", flush=True)
		clusternum = ", ".join(df_primeros100['Clusters'])
		num = re.findall("[0-9]+", clusternum)
		df_primeros100["Clusters"] = num # Solo la version normal
		print(df_primeros100, flush=True)
		# Aplicar log10 a la columna de interés (asegurando que no haya valores <= 0)
		df_primeros100['Importancia_Log10'] = np.log10(df_primeros100['Importancia'].replace(0, np.nan)) # Añadimos version logaritmica
		df_primeros100['Importancia_Log10'] = df_primeros100['Importancia_Log10'].replace(np.nan, 0)
		print(df_primeros100, flush=True)
		print("Guardamos las importancias en la version logaritmica como CSV y PNG... ", flush=True)
		print("Importancias en CSV...", flush=True)
		df_primeros100.to_csv(rutaimplogcsv, index=False)

		#
		#
		# Especificar las columnas
		x_col = 'Clusters'  # Columna para el eje X
		y_col = 'Importancia_Log10'  # Columna para el eje Y (puede ser 'Importancia' o 'Importancia_Log10')
		# Crear la figura
		fig, ax = plt.subplots(figsize=(12, 4))
		# Graficar las barras usando las columnas específicas
		ax.bar(df_primeros100[x_col], df_primeros100[y_col], color='skyblue')  # Usar las columnas especificadas
		# Título y etiquetas
		ax.set_title(f'Importancia de las características escala Logaritmica')
		ax.set_xlabel('Clusters')
		ax.set_ylabel('Importancia logarítmica')
		# Ajustar las etiquetas del eje X
		ax.set_xticks(range(len(df_primeros100[x_col])))
		ax.set_xticklabels(df_primeros100[x_col], rotation=90, fontsize=6, fontweight='bold')
		# Ajustar el diseño para evitar recortes
		plt.tight_layout()
		# Guardar el gráfico como archivo PNG
		plt.savefig(rutaimplogpng, format='png', dpi=300, bbox_inches='tight')







		###################### -- DISTRIBUCION DE NICHOS -- ######################
		print("##### Distribucion de nichos 100 Clusters #####", flush=True)
		#Tomamos los nombres de los clusters.
		# Como la matriz esta en un numpy array, ahora toca extraer por el numero de las columna. 
		# Nombramos las columnas que necesitamos 
		list100 = [Xnp[:,int(npcol)] for npcol in df_primeros100.iloc[:, 0] if not npcol is None] 
		print("columnas 100; extraidas: ", list100, flush=True)
		#list100 = [Xnp[npcol] for npcol in cienclusters_importantes if npcol in Xnp.columns]
		df_cluster100 = pd.DataFrame(np.array(list100).T, columns=df_primeros100.iloc[:, 0], index=Y.index) 
		# añadimos los nichos 
		df_cluster100['Nicho'] = Y['Nicho'] 
		#print(r"matriz df_cluster100 creada\n", df_cluster100, flush=True)
		#print(r"indices de df_cluster100 \n", df_cluster100.index, flush=True)
		#print(r"columnas de df_cluster100 \n", df_cluster100.columns, flush=True)	

		###################### -- Nichos por Clusters: Hacemos el conteo -- ######################
		print("Continuamos hacia el conteo, juntando en indice y las 100 columnas", flush=True)
		u = Y["Nicho"].unique() 
		c =list(df_cluster100.columns) 
		print("u", u, "c", c, flush=True)
		print("A eliminar la palabra Nicho de la lista c", flush=True)
		del c[c.index('Nicho')] 
		print(c, 'Nicho' in c, flush=True)
		#Creamos una matriz 
		print("matriz vacia, creandose", flush=True)
		zeroconteonichos = pd.DataFrame(0, index=u, columns=c) 

		for i in u: 
			for j in c:
				ev = list(df_cluster100.index[df_cluster100['Nicho'] == i])
				# Asegúrate de que todos los elementos sean enteros
				values_to_sum = list(df_cluster100.loc[ev, j])
				values_to_sum = map(int, values_to_sum)
				sumas = sum(values_to_sum)
				zeroconteonichos.loc[i, j] = sumas
		print("##### Guardando distribucion de nichos... #####", flush=True)
		zeroconteonichos.to_csv(rutadistnichocsv)

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
			#print(len(par), flush=True)
			#print(len(impar), flush=True)
            
            # Dibujar las barras
			for i, cluster in enumerate(clusters):
				#print("###########################", flush=True)
				cluster_data = h3[h3['Cluster'] == cluster]

				pos = [positions[j][i] for j in range(len(caracteristicas))]
				freqs =[]
				for i in list(cluster_data['Frecuencia']):
					freqs.append(i)
					
				freqs = pd.Series(freqs)
				#print("Cluster data \n", cluster_data, flush=True)
				#print("Posiciones: ", pos, flush=True)
				#print("Frecuencias: ", list(cluster_data['Frecuencia']), flush=True)
				#print("Longitud de las frecuencias: ", len(freqs), flush=True)
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
				#plt.close()






		###################### -- PREDICCIONES -- ######################
		Y_pred = rf.predict(X_test)






		##################### -- MATRIZ DE CONFUSION -- ######################
		Ynp_pred = np.round(Y_pred).astype(int)
		dict_predictions = {"Observados": Y_test,
		                       "Predichos": Ynp_pred}

		df_predictions = pd.DataFrame(dict_predictions)
		df_predictions.to_csv(rutaypred)
		mc = confusion_matrix(Y_test, Ynp_pred)
		#tn, fp, fn, tp = confusion_matrix(Y_test, Ynp_pred).ravel()
		#print(tn, fp, fn, tp)
		cero=np_clases_eitquetas[np_clases_eitquetas["Codificacion"] == 0]["Nicho"].to_string(index=False)
		uno=np_clases_eitquetas[np_clases_eitquetas["Codificacion"] == 1]["Nicho"].to_string(index=False)
		df_matrixconf = pd.DataFrame(mc)
		df_matrixconf = df_matrixconf.rename(columns={
			'0': f'{cero}',
			'1': f'{uno}'
		})
		df_matrixconf.index = [f'{cero}', f'{uno}']
		conf_matrix = df_matrixconf.values
		##################### -- Visualizacion de la Matriz de Confusion -- ######################
		# Crear la visualización de la matriz de confusión
		disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=[f'{cero}', f'{uno}'])
		disp.plot()

		# Ajustar el diseño para que no se recorten los elementos
		plt.tight_layout()

		# Guardar la gráfica como un archivo PNG con el tamaño y resolución especificados
		plt.savefig(rutaconfpng, format='png', dpi=300, bbox_inches='tight')

		try:
			df_matrixconf.to_csv(rutaconfcsv)
			print("Matriz de confusión guardada exitosamente", flush=True)
		except Exception as e:
			sys.stderr.write(f"Error al guardar la matriz de confusión: {e}\n")
			sys.stderr.flush()


		df_report = pd.DataFrame(classification_report(Y_test, Y_pred, output_dict=True))
		print(df_report)
		df_report.to_csv(rutareport)






		###################### -- GRAFICOS DE ARBOLES -- ######################
		#fig, axes = plt.subplots(nrows = 1,ncols = 5, figsize=(20,20))
		for i in range(1, 5):
			rutaarbolf = rutaarbol + f"_{i}.png"
			plt.figure(figsize=(6, 5))
			tree.plot_tree(rf.estimators_[i], filled=True)
		#plt.subplots_adjust(wspace=0.5, hspace=0.5)
		# Guardar el gráfico como archivo PNG
			plt.savefig(rutaarbolf, format='png', dpi=300, bbox_inches='tight')
		#plt.close()










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


print("-----------------------------------------------------------------------------------------------")
print("")

# Ya solo falta las metricas y modificar lo de los arboles y añadir lo de la superficie de decision. Y reportar en Github
```
---

Se estructuro un codigo con dos caracteristicas especificas, con el fin de construir graficos sobre arboles y decision surfaces.
El exporta en imagenes independientes, cada uno de lo arboles y decision surfaces. Reduce el tiempo de lectura, abriendo solo dos columnas de la tabla de frecuencias, mas la columna Genomas, personalizando cuales columnas usar y realizar los analisis posteriores de manera auomatica.
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos las librerias necesarias
import time
import datetime
import pandas as pd
import numpy as np
import os
import csv
import sys
import traceback
import io
import re
import codecs
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, ConfusionMatrixDisplay, classification_report
from sklearn import tree
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# direccion donde se encuentra el script
actual_script = os.path.abspath(__file__)
# Ahora extraemos la ruta del directorio
actual_directorio = os.path.dirname(actual_script)

print("")
print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡")
# Nos cambiamos de ruta
os.chdir(actual_directorio)
print("Script para construir graficos de Arboles y Superficies de Decision")
print("Ya trabajando en directorio actual: ", os.getcwd())
hora_actual = datetime.datetime.now()
print("Fecha y hora de ejecución: ", hora_actual)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")

if __name__ == "__main__":
	try:
		start_time = time.time()
		###################### -- DIRECCIONES, ARCHIVOS Y PARAMETROS -- ######################
		siglas_exp =       "AP"
		test_or_original = "test"
		version =          "v3" 
		################ -- INPUT -- ################
		rutabase=                "./MicroSet/INPUT/" # Ruta base
		filemtz =                f"cluster_pseudomonas_{test_or_original}.csv" #Nombre del archivo con la matriz
		fileclass =              f"{siglas_exp}_nicho_pseudomonas_{test_or_original}.txt" # Nombre de la tabla de clasificacion
		empty_nicho =            'Vacio'
		n_estima =                50
		test_size =               0.50
		random_state_split =      99
		random_state_classifier = 7

		rutamtz = os.path.join(rutabase, filemtz)
		rutaclass = os.path.join(rutabase, fileclass)

		################ -- OUTPUT FOLDERS -- ################ 
		imgrutabase =   "./MicroSet/OUTPUT"
		directo =       f"./{imgrutabase}_{siglas_exp}_{version}_{test_or_original}".upper()
		if not os.path.exists(directo):
			os.makedirs(directo)

		tree_ds =       f"tree_decision_surfaces_{siglas_exp}_{version}_{test_or_original}".upper()
		rutatree_ds =   os.path.join(directo, tree_ds)
		if not os.path.exists(rutatree_ds):
			os.makedirs(rutatree_ds)



		arbol =                 f"{version}_{siglas_exp}_{test_or_original}_tree"
		dsurface =              f"{version}_{siglas_exp}_{test_or_original}_decision_surface_tree"

		rutaarbol =             os.path.join(rutatree_ds, arbol)
		rutadsurface =          os.path.join(rutatree_ds, dsurface)


		###################### -- ABRIMOS LOS ARCHIVOS Y PREPARAMOS LOS DATOS -- ###########################
		# CSV con la Tabla de Frecuencias
		df_tf = pd.read_csv(rutamtz, usecols=['Genomas', 'Cluster13000', 'Cluster12345'])

		# TXT con las etiquetas
		df_e = pd.read_csv(rutaclass, delimiter='\t')

		# Unimos acorde a los genomas.
		df = pd.merge(df_tf.sort_values(by='Genomas'), df_e.sort_values(by='Genomas'), on='Genomas')

		# Eliminamos los genomas sin etiquetas
		df = df[df['Nicho'] != empty_nicho]

		# De este DataFrame separamos los nichos y transformamos en numeros como etiquetas
		la_enc = LabelEncoder()
		y_normal = np.array(df['Nicho'])
		y_encoded = la_enc.fit_transform(y_normal)
		y_encoded = y_encoded.astype(int)

		# Extraemos los clusters
		X = np.array(df.iloc[:,[1, 2]])


		print("Presentacion: ", flush=True)
		print(" 'X' que son los clusters en arreglo")
		print(X, flush=True)
		print(" 'y' normal, que son los nichos")
		print(y_normal, flush=True)
		print(" 'y' codificada, que son los nichos")
		print(y_encoded, flush=True)
		print("Dataframe con Genomas, dos clusters y nichos", flush=True)
		print(df, flush=True)

		###################### -- SEPARAMOS DATOS Y CONSTRUIMOS MODELO -- ##################################
		# Dividir los datos
		X_train, X_test, Y_train, Y_test = train_test_split(
			X, y_encoded, test_size=test_size, random_state=random_state_split
		)

		# Entrenar el modelo Random Forest
		rf = RandomForestClassifier(n_estimators=n_estima, random_state=random_state_classifier)
		rf.fit(X_train, Y_train)


		###################### -- GRAFICOS DE ARBOLES -- ######################
		#fig, axes = plt.subplots(nrows = 1,ncols = 5, figsize=(20,20))
		for i in range(1, 5):
			rutaarbolf = rutaarbol + f"_{i}.png"
			plt.figure(figsize=(6, 5))
			tree.plot_tree(rf.estimators_[i], filled=True)
		#plt.subplots_adjust(wspace=0.5, hspace=0.5)
		# Guardar el gráfico como archivo PNG
			plt.savefig(rutaarbolf, format='png', dpi=300, bbox_inches='tight')
		#plt.close()





		###################### -- SUPERFICIE DE DECISIONES -- ######################
		# Generar la superficie de decisión para cada árbol
		for i, tree in enumerate(rf.estimators_[1:5]):
			numero = f"_{i}.png"
			rutadsurfacef = rutadsurface + numero
			plt.figure(figsize=(6, 5))
			# Crear una malla de puntos
			x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
			y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
			xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
								np.arange(y_min, y_max, 0.01))

			# Predecir sobre la malla
			Z = tree.predict(np.c_[xx.ravel(), yy.ravel()])
			Z = Z.reshape(xx.shape)

			# Dibujar la superficie de decisión
			plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.Paired)
			plt.scatter(X_train[:, 0], X_train[:, 1], c=Y_train, edgecolor='k', cmap=plt.cm.Paired)
			plt.title(f"Superficie de Decisión del Árbol {i}")
			plt.xlabel("Feature 1")
			plt.ylabel("Feature 2")
			plt.tight_layout()
			plt.savefig(rutadsurfacef, dpi=300)

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


print("-----------------------------------------------------------------------------------------------")
print("")
```
---

# 4 DE DICIEMBRE DEL 2024
Otra pagina sobre como grafican y usan las `decision surface` https://ogrisel.github.io/scikit-learn.org/sklearn-tutorial/auto_examples/ensemble/plot_forest_iris.html

De esta otra pagina, se pudo cambiar a un color personalizado los puntos y fondo de las `decision surface`: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

Y de esta pagina, se encontro un codigo que se adapto y ajusto con Chat GPT para cambiar a un color personalizado a los nodos de los arboles: https://stackoverflow.com/questions/70437840/how-to-change-colors-for-decision-tree-plot-using-sklearn-plot-tree
