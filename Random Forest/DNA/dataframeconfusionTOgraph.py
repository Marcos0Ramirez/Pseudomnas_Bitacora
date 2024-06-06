# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:12:24 2024

@author: 52477
"""

# Confusion Matrix
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score, f1_score

imgrutabase = "C:/Users/52477/Documents/UNAM Octavo semestre/Laboratorio Internacional de Investigación Sobre el Genoma Humano/Laboratorio de evolucion y ecologia/RandomForest/RandomForest_py/DNA"
mtzconfusion = "confusion_matrix.csv"
imgconfusion = "Confusion_graph.png"

rutaconfusion = os.path.join(imgrutabase, mtzconfusion)
imgfugr = os.path.join(imgrutabase, imgconfusion)

mc = pd.read_csv(rutaconfusion)


mc_df = pd.DataFrame(mc)
mc_df = mc_df.drop('Unnamed: 0', axis=1)
mc_df = mc_df.rename(columns={
    '0': 'Hospedero',
    '1': 'Ambiente'
})
mc_df.index = ['Hospedero', 'Ambiente']


conf_matrix = mc_df.values
##################### -- Visualizacion de la Matriz de Confusion -- ######################
# Crear la visualización de la matriz de confusión
disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=['Ambiente', 'Hospedero'])
disp.plot()

# Ajustar el diseño para que no se recorten los elementos
plt.tight_layout()

# Guardar la gráfica como un archivo PNG con el tamaño y resolución especificados
plt.savefig(imgfugr, format='png', dpi=300, bbox_inches='tight')

# Mostrar la gráfica
plt.show()








