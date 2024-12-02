# Sera la bitacora de modificaciones de Random Forest.
_Finalmente se añadira a la carpeta final con todo y todo._

## FECHA 1 DE DICIEMBRE DEL 2024
Con el fin de optimizar el proceso de creacion del codigo, se adaptara buena parte del script a este.
Se instalo miniconda para la maquina virtual de Ubunut en Windows, de la siguiente liga: https://docs.anaconda.com/miniconda/install/

Por default se instalo python 3.12.7 y solo queda instalar los paquetes scikit-sklearn, numpy, pandas y matplotlib.pyplot
```
conda install -c conda-forge scikit-learn numpy pandas matplotlib
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
Encontre que hay un grafico para implemetar, se llama `decision surfaces`, encontrado en la siguiente liga https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html y se explica por medio de este blog: https://hackernoon.com/lang/es/como-trazar-un-limite-de-decision-para-algoritmos-de-aprendizaje-maquina-en-python-3o1n3w07 la funcion de este grafico. El cual cito:

> Los algoritmos de clasificación aprenden a asignar etiquetas de clase a ejemplos (observaciones o puntos de datos), aunque sus decisiones pueden parecer opacas.
> Este tutorial está escrito por KVS Setty
> Puedes encontrar el código fuente completo en mi repositorio git
> Un diagnóstico popular para comprender las decisiones tomadas por un algoritmo de clasificación es la superficie de decisión . Esta es una gráfica que muestra cómo un algoritmo de aprendizaje automático entrenado predice una cuadrícula gruesa en el espacio de características de entrada.
> ***Un gráfico de superficie de decisión es una herramienta poderosa para comprender cómo un modelo determinado "ve" la tarea de predicción y cómo ha decidido dividir el espacio de características de entrada por etiqueta de clase.***

Que en mis palabras

La premisa, es que los **algoritmos de aprendiza automatico**, aprenden a asignar etiquetas en base a su entrenamiento con las observaciones.
Este grafico, puede ser implementado en el modelo RandomForesClassifier, el cual indica como es que el modelo, considera a que clase se asocia de acuerdo a una combinacion especifica de caracteristicas.
En caso de que la clasificacion por Random Fores hace muchos arboles, cada uno puede generar una superficie de decision diferente. Pero en si RandomForestClassifier combina el resultado de todos los arboles generados, lo cual al usar todos la hace mas robusta y menos propensa a sobreajustes. Asi al entrenar y predecir, asigna una clase con un promedio de las predicciones de los arboles y la superficie de decision resultante muestra como esas clases se distribuyen a traves de las combinaciones de las caracteristicas. Nota, las caracteristicas se toman de manera aleatoria para generar la malla.

Pagina que hace la comparacion con diferentes clasificadores https://qu4nt.github.io/sklearn-doc-es/auto_examples/ensemble/plot_forest_iris.html
