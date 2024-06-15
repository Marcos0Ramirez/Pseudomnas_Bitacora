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
    ###################### -- EXTRACCION DE LOS DATOS -- ######################
    
    rutabase= "Pseudomonas/WORK/ANALYSIS_CDHIT/MATRIXCDHIT/" # Ruta base
    filemtz = "fast_matrizcdhit_pymatrizcdhit.csv" #Nombre del archivo con la matriz
    fileclass = "nichospseudo3894.txt" # Nombre de la tabla de clasificacion
    
    rutamtz = os.path.join(rutabase, filemtz)
    rutaclass = os.path.join(rutabase, fileclass)
    
    imgrutabase = "/Pseudomonas/WORK/ANALYSIS_CDHIT/MATRIXCDHIT/IMAGENES/"
    imgic = "importancia_caracteristicas.png"
    mtzconfusion = "confusion_matrix.csv"

    rutaimportacara = os.path.join(imgrutabase, imgic)
    rutaconfusion = os.path.join(imgrutabase, mtzconfusion)
    
    # Extraemos la data
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
    
    with codecs.open(rutaclass, 'r', encoding='utf-8') as csvclass:
            csvclase = csv.reader(csvclass, delimiter="\t")
            data = list(csvclase)
    
    encabezado = data[0]
    rows = data[1:]
    df_clase = pd.DataFrame(rows, columns=encabezado)
    
    mtz_class_caracteres = pd.merge(df.sort_values(by='Genomas'), df_clase.sort_values(by='Genomas'), on='Genomas')
    mtz_class_caracteres = mtz_class_caracteres[mtz_class_caracteres['Nicho'] != 'vacio']
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
    
    mtz_class_caracteres = mtz_class_caracteres.drop("Nicho", axis=1)
    mtz_class_caracteres_list = list(mtz_class_caracteres.columns)
    print("la matriz la hacemos arreglo")
    sys.stdout.flush()
    mtz_class_caracteres = np.array(mtz_class_caracteres)
    
    train_mtz_class_caracteres, test_mtz_class_caracteres, train_labels, test_labels = train_test_split(mtz_class_caracteres, 
                                                                                                        encoded_labels, 
                                                                                                        test_size=0.20, 
                                                                                                        random_state=99)
    
    print('Training Features Shape:', train_mtz_class_caracteres.shape)
    sys.stdout.flush()
    print('Training Labels Shape:', train_labels.shape)
    sys.stdout.flush()
    print('Testing Features Shape:', test_mtz_class_caracteres.shape)
    sys.stdout.flush()
    print('Testing Labels Shape:', test_labels.shape)
    sys.stdout.flush()
    
    ###################### -- ENTRENAMIENTO DEL MODELO -- ######################
    rf = RandomForestRegressor(n_estimators=50, random_state=7)
    rf.fit(train_mtz_class_caracteres, train_labels)
    
    ###################### -- Caracteristicas que son importantes -- ######################
    importancias = rf.feature_importances_
    feature_importances = pd.DataFrame(importancias, index=mtz_class_caracteres_list, columns=['Importancia'])
    feature_importances = feature_importances.sort_values(by='Importancia', ascending=False)
    
    print(feature_importances)
    sys.stdout.flush()
    primeros20 = feature_importances.iloc[:20]
    
    plt.figure(figsize=(20, 12))
    primeros20.plot(kind='bar')
    plt.title('Importancia de las características')
    plt.xlabel('Características')
    plt.ylabel('Importancia')
    plt.yticks(rotation=0)
    plt.tight_layout()
    
    try:
        plt.savefig(rutaimportacara, format='png', dpi=300, bbox_inches='tight')
        print("Imagen guardada exitosamente")
    except Exception as e:
        sys.stderr.write("Error al guardar la imagen: {}\n".format(e))
        sys.stderr.flush()
    
    predictions = rf.predict(test_mtz_class_caracteres)
    
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
        print("Precision:", precision)
        print("Recall:", recall)
        print("F1 Score:", f1)
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

