# 19 de mayo del 2024
El dia de hoy, se establecio la funcion de la matriz de confusion y asi una forma de saber cuales cluster son importantes para haer las predicciones en python

```

# Importamos las librerias necesarias
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

###################### -- EXTRACCION DE LOS DATOS -- ######################
# Extraemos la data
rutamtz = r"Descargas_NCBI\CDHIT\MATRIXDATA\testpysh_pymatrizcdhit.csv"
matriz = pd.read_csv(rutamtz)

# Extremos la tabla de clasificacion
rutaclass = r"Descargas_NCBI\CDHIT\MATRIXDATA\classificacion_genomas.txt"
classificacion = pd.read_csv(rutaclass)

# Juntamos ambos archivos 
mtz_class_caracteres = pd.merge(matriz, classificacion, on='Genomas')
mtz_class_caracteres = mtz_class_caracteres[mtz_class_caracteres['Nicho'] != 'Unclassified']

###################### -- PREPARACION DE LOS DATOS -- ######################
### -- One-Hot Encoding -- ###
#dummies_specie = pd.get_dummies(mtz_class_caracteres["Specie"]) , dummies_specie
dummies_Genomas = pd.get_dummies(mtz_class_caracteres["Genomas"])
mtz_class_caracteres = pd.concat([mtz_class_caracteres.drop(columns=['Genomas', 'Specie']), dummies_Genomas], axis=1)

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
rf = RandomForestRegressor(n_estimators=1000, random_state=7)
rf.fit(train_mtz_class_caracteres, train_labels)

###################### -- Caracteristicas que son importantes -- ######################
importancias = rf.feature_importances_
feature_importances = pd.DataFrame(importancias, index=mtz_class_caracteres_list, columns=['Importancia'])
feature_importances = feature_importances.sort_values(by='Importancia', ascending=False)

print(feature_importances)
primeros20 = feature_importances.iloc[:20]
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
primeros20.plot(kind='bar')
plt.title('Importancia de las características')
plt.xlabel('Importancia')
plt.ylabel('Características')
# Ajustar la rotación de las etiquetas del eje y
plt.yticks(rotation=0)
# Mostrar la gráfica
plt.show()
###################### -- Hacemos predicciones con el conjunto de prueba -- ######################
predictions = rf.predict(test_mtz_class_caracteres)

##################### -- Matriz de Confusion -- ######################
prediction_discrete = np.round(predictions).astype(int)
mc = confusion_matrix(test_labels, prediction_discrete)

##################### -- Visualizacion de la Matriz de Confusion -- ######################
vis = ConfusionMatrixDisplay(mc)
vis.plot()

##################### -- Exactitud Matriz de Confusion -- ######################
accuracy = accuracy_score(test_labels, prediction_discrete)
precision = precision_score(test_labels, prediction_discrete, average='weighted', zero_division=0)
recall = recall_score(test_labels, prediction_discrete, average='weighted', zero_division=0)
f1 = f1_score(test_labels, prediction_discrete, average='weighted', zero_division=0)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

```

# 25 de mayo del 2024
Se termino el script final para correr en el cluster y analizar las 3,894 secuencias de IMG, el cual esta a disposicion aqui https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/tree/main/Random%20Forest/DNA 

Con el ejecutador del script `runpygraphconfusion.sh` y el script de Python que hace el analisis `RandomForest.py`

# 26 de mayo del 2024
Termino el script y con resultados exitosos del analisis, lo cuales podemos contar con el grafico de importancia

![importancia_caracteristicas](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/cdb8415b-f616-4ab0-add6-e65a17365d68)

Y con una salida csv debido a que en el cluster no se tiene el paquete para visualizar la matriz de confusion

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/7636354b-e6a3-4cb0-b515-1493d7684957)

Pero con el script `dataframeconfusionTOgraph.py` Se pudo obtener el grafico de confusion de manera local.

![Confusion_graph](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/cad56c29-ed1d-40e4-a8f5-52220c7ee104)

# 27 de mayo del 2024
Se observo que genomas se encuntran en le cluster mas importante `Cluster 50634`, los cuales los observados son proteinas reductasas.

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/b41ae281-fb55-4e20-bc77-07b0684d433c)

# 6 de junio del 2024
Trabajando con el analisis en local, se agrego al codigo que pueda guardar la codificaicon de los nichos en numeros.

```
labels = np.array(mtz_class_caracteres["Nicho"])
la_enc = LabelEncoder()
encoded_labels = la_enc.fit_transform(labels)
######## Nuevo de aqui pa bajo ########
etiquetas = labels.reshape(1, -1)
codified =  encoded_labels.reshape(1, -1)

class_etiquetas = np.concatenate((etiquetas, codified)).T
print(class_etiquetas)
pd.DataFrame(class_etiquetas).drop_duplicates().to_csv("np_class_etiquetas.csv", index=False)
```
Se añadio modificaciones para el grafico de importancia, pero ahora tambien se agrego el grafico en version logaritmica

### Los primeros 100
```
importancias = rf.feature_importances_
feature_importances = pd.DataFrame(importancias, index=mtz_class_caracteres_list, columns=['Importancia'])
feature_importances = feature_importances.sort_values(by='Importancia', ascending=False)

print(feature_importances)
primeros100 = feature_importances.iloc[:100]
```
### Normal
```
plt.figure(figsize=(20, 12))
primeros100.plot(kind='bar')
plt.title('Importancia de las características')
plt.xlabel('Características')
plt.ylabel('Importancia')
# Ajustar la rotación de las etiquetas del eje y
plt.xticks(rotation=90, fontsize=3, fontweight='bold') 
# Ajustar el diseño para que no se recorten los elementos
plt.tight_layout()
# Guardar la gráfica como un archivo PNG
plt.savefig(rutaimportacara, format='png', dpi=300, bbox_inches='tight')
```
### Logartimica
```
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

```
Falta poner las diferencias entre cada cateogoria
Usar los 100 primeros cluster y de los genomas que pertenecen a cada cluster. Cuantos pertenecen a hospederos y cuantos a ambiente como este primer ejemplo.
Lo hacemos desde la matriz de cdhit, nombrando con la columnas columnas necesarias y tomando solo los datos que tengan etiquetas diferentes a vacio. Realizamos el conteo.

# 8 de junio del 2024
Se plantea añadir mas codigo para realizar ahora la matriz reducida con los 100 clusters mas importantes y con los genomas usados para hacer las predicciones.

Tener los genomas con indices son muy utiles dibido que al extraer los nichos, podemos obtener un nuevo dataframe con los genomas a usar para las predicciones.
```
# Juntamos ambos archivos 
mtz_class_caracteres = pd.merge(matriz.sort_values(by='Genomas'), classificacion.sort_values(by='Genomas'), on='Genomas')
mtz_class_caracteres.set_index('Genomas', inplace=True) ####### Nueva linea #######
mtz_class_caracteres = mtz_class_caracteres[mtz_class_caracteres['Nicho'] != 'Unclassified']

mtz_idgen_nicho = pd.DataFrame(pd.Series(mtz_class_caracteres['Nicho'])) ####### Nueva linea ####### Debido a que se quitaron los genomas que no se requieren

matriz.sort_values(by='Genomas')
classificacion.sort_values(by='Genomas')
###################### -- PREPARACION DE LOS DATOS -- ######################
### -- One-Hot Encoding -- ###
mtz_class_caracteres = pd.concat([mtz_class_caracteres.drop(columns=['Specie'])], axis=1) 
```
Ya con la informacion de los nichos y los genomas usados, ahora se puede saber cuales son los genomas que pertenecen a cada cluster
```
###################### -- Caracteristicas que son importantes -- ######################
importancias = rf.feature_importances_
feature_importances = pd.DataFrame(importancias, index=mtz_class_caracteres_list, columns=['Importancia'])
feature_importances = feature_importances.sort_values(by='Importancia', ascending=False)

print(feature_importances)
primeros100 = feature_importances.iloc[:100]
###################### -- Nichos por Clusters -- ###################### ####### Nueva linea #######
print(primeros100)
#Tomamos los nombres de los clusters. ####### Nueva linea #######
cienclusters_importantes = " ".join(primeros100.index) ####### Nueva linea #######
# Como la matriz esta en un numpy array, ahora toca extraer por el numero de las columna. ####### Nueva linea #######
cienclusters_importantes = cienclusters_importantes.replace("Cluster", "").split(" ") ####### Nueva linea #######
# Nombramos las columnas que necesitamos ####### Nueva linea #######

# Simplificamos el for anterior ####### Nueva linea #######
clustercien = [mtz_class_caracteres[:,int(npcol)] for npcol in cienclusters_importantes if not npcol is None] ####### Nueva linea #######
mtz_clustercien = pd.DataFrame(np.array(clustercien).T, columns=cienclusters_importantes, index=mtz_idgen_nicho.index) ####### Nueva linea #######
# añadimos los nichos    ####### Nueva linea #######
mtz_clustercien['Nichos'] = mtz_idgen_nicho['Nicho'] ####### Nueva linea #######
# Se virifico que al ordenar los datos, se colocan correctamente sin incosistencias ####### Nueva linea #######
```

# 10 de junio del 2024
Este es el codigo para hacer la imagen, cuando se tenga solo dos nichos
```
# OPCION 11
# UN HISTOGRAMA (dos filas)

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
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/2b3bd46e-6204-4520-84c5-a74dad1d043d)

Asi, para cuando son mas de 2 nichos a analizar
```
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
```

x | a | b |
--|---|---|
1 | ![histograma_mlabels_1](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/f6616bff-e0b7-44e6-b62c-37c82cb6cd51) | ![histograma_mlabels_2](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/21ee387e-847d-4087-992e-9c75538c83a6)  |
2 | ![histograma_mlabels_3](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/89d52403-3fd3-4b5a-b6fb-4ec411544fc8) | ![histograma_mlabels_4](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/30c8b718-11c7-465f-842f-b51efe85f721) |

# 14 de junio del 2024
Se haran adaptaciones para el codigo madre del cluster en el siguiente archivo https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/blob/main/Random%20Forest/DNA/RandomForest_addhist_logimp.py

# 15 de junio del 2024
Estos son los registros de los problemas que fueron apareciendo
```
pyrandom_forgraph_output.477979.out
pyrandom_forgraph_output.477980.out
pyrandom_forgraph_output.477981.out
pyrandom_forgraph_output.477982.out
pyrandom_forgraph_output.477983.out
pyrandom_forgraph_output.477984.out
pyrandom_forgraph_output.477985.out
pyrandom_forgraph_output.477986.out
pyrandom_forgraph_output.477988.out
pyrandom_forgraph_output.477989.out
pyrandom_forgraph_output.477990.out
pyrandom_forgraph_output.477991.out
pyrandom_forgraph_output.477992.out
pyrandom_forgraph_output.477993.out
pyrandom_forgraph_output.477994.out
pyrandom_forgraph_output.477995.out
pyrandom_forgraph_output.477996.out
pyrandom_forgraph_output.477997.out
pyrandom_forgraph_output.477998.out
pyrandom_forgraph_output.477999.out
pyrandom_forgraph_output.478000.out
pyrandom_forgraph_output.478001.out
pyrandom_forgraph_output.478002.out
pyrandom_forgraph_output.478003.out
pyrandom_forgraph_output.478004.out
```
Y se dejaran en la carpeta https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/blob/main/Random%20Forest/DNA/MICROSET_PRUEBA/ERROR_OUTPUT/

Asi, cuando se termine de corregir el archivo se subira a esta carpeta y finalmente se aplicara con el set de datos original.

Mientras tanto al parecer el problema continua con la parte de procesar los datos para hacer la matriz, se toma los datos int, pero aparece un str y no se en que parte sea del codigo
De acuerdo con el registro `pyrandom_forgraph_output.478006.out`, https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/blob/main/Random%20Forest/DNA/MICROSET_PRUEBA/ERROR_OUTPUT/pyrandom_forgraph_output.478006.out no se puede hacer las sumas porque hay str values y no int values.

Parte del codigo
```
.
.
.
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
            ev = list(mtz_clustercien.index[mtz_clustercien['Nicho'] == i]) #------------------------- // NUEVO \\ --------------------------#
            zeroconteonichos.loc[i,j] = int(sum(list(mtz_clustercien.loc[ev,j]))) #------------------------- // NUEVO \\ --------------------------#
.
.
.
```
En base del siguiente reporte https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/blob/main/Random%20Forest/DNA/MICROSET_PRUEBA/ERROR_OUTPUT/pyrandom_forgraph_output.478007.out

Aparecio esto
```
('indices de mtz_clustercien \\n', Index([u'2505313052', u'2517572175', u'2548876750', u'2554235471',
       u'2630968743', u'2713896862', u'2785510749', u'2923166773'],
      dtype='object', name=u'Genomas'))
('columnas de mtz_clustercien \\n', Index([u'1723', u'7836', u'17265', u'18276', u'8078', u'15304', u'7308',
       u'6284', u'12050', u'2818',
       ...
       u'13487', u'1405', u'4830', u'2288', u'18342', u'7526', u'8393',
       u'12084', u'7407', u'Nicho'],
      dtype='object', length=101))
Continuamos hacia el conteo, juntando en indice y las 100 columnas
('u', array(['Patogeno', 'HostHuman', 'HostFungi', 'Patogeno ', 'Ambiente',
       'Hostalga', 'Hostanimal'], dtype=object), 'c', ['1723', '7836', '17265', '18276', '8078', '15304', '7308', '6284', '12050', '2818', '4988', '3716', '18593', '7919', '1955', '18362', '1235', '11450', '372', '16299', '13848', '11344', '4758', '3707', '5175', '12171', '11118', '2835', '13255', '17708', '4493', '17400', '13313', '12102', '5383', '2338', '6023', '11663', '1901', '14141', '17063', '13514', '12486', '1271', '15052', '5719', '12781', '5741', '15134', '16691', '808', '14368', '10777', '11765', '4933', '3019', '13284', '16075', '14016', '15207', '9262', '533', '7050', '15804', '6778', '3873', '16817', '14403', '1985', '10772', '708', '4712', '11642', '2211', '3058', '7217', '7136', '266', '16625', '5974', '15855', '8632', '2946', '3071', '8006', '8782', '7339', '3145', '8188', '17298', '10580', '13487', '1405', '4830', '2288', '18342', '7526', '8393', '12084', '7407', 'Nicho'])
A eliminar la palabra Nicho de la lista c
(['1723', '7836', '17265', '18276', '8078', '15304', '7308', '6284', '12050', '2818', '4988', '3716', '18593', '7919', '1955', '18362', '1235', '11450', '372', '16299', '13848', '11344', '4758', '3707', '5175', '12171', '11118', '2835', '13255', '17708', '4493', '17400', '13313', '12102', '5383', '2338', '6023', '11663', '1901', '14141', '17063', '13514', '12486', '1271', '15052', '5719', '12781', '5741', '15134', '16691', '808', '14368', '10777', '11765', '4933', '3019', '13284', '16075', '14016', '15207', '9262', '533', '7050', '15804', '6778', '3873', '16817', '14403', '1985', '10772', '708', '4712', '11642', '2211', '3058', '7217', '7136', '266', '16625', '5974', '15855', '8632', '2946', '3071', '8006', '8782', '7339', '3145', '8188', '17298', '10580', '13487', '1405', '4830', '2288', '18342', '7526', '8393', '12084', '7407'], False)
matriz vacia, creandose
matriz vacia, creada, continuamos con concatenar los 100 mejores cluster en la matriz vacia
('Patogeno', '1723')
Ha ocurrido un error al usar la funcion confusion_graph(): unsupported operand type(s) for +: 'int' and 'str'
```
Parece ser que las comparaciones las hace con str y no con int

De acuerdo con chatGPT, sugiere estas modifiaciones al codigo, debido a que trabajamos con python 2
```
    zeroconteonichos = pd.DataFrame(0, index=u, columns=c) #------------------------- // NUEVO \\ --------------------------#
    print("matriz vacia, creada, continuamos con concatenar los 100 mejores cluster en la matriz vacia")
    sys.stdout.flush()
    for i in u: #------------------------- // NUEVO \\ --------------------------#
        for j in c: #------------------------- // NUEVO \\ --------------------------#
            print(i, j)
            sys.stdout.flush()
            ev = list(mtz_clustercien.index[mtz_clustercien['Nicho'] == i])
            print(ev)
            sys.stdout.flush()
            # Asegúrate de que todos los elementos sean enteros
            values_to_sum = list(mtz_clustercien.loc[ev, j])
            print("Valores a sumar (antes de convertir):", values_to_sum)
            sys.stdout.flush()
            values_to_sum = map(int, values_to_sum)
            print("Valores a sumar (después de convertir):", values_to_sum)
            sys.stdout.flush()
            sumas = sum(values_to_sum)
            print("sumas: ", sumas)
            sys.stdout.flush()
            zeroconteonichos.loc[i, j] = sumas
            print("zeroconteonichos.loc[i,j]", zeroconteonichos.loc[i, j])
            sys.stdout.flush()
```
Ahora el error es porque no esta la variable primeros20, esto se debe poner primeros100, asi la bitacora de errores  https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/blob/main/Random%20Forest/DNA/MICROSET_PRUEBA/ERROR_OUTPUT/pyrandom_forgraph_output.478009.out

Ya se logro guardar los graficos de importancia, ahora solo falta los histogramas https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/blob/main/Random%20Forest/DNA/MICROSET_PRUEBA/ERROR_OUTPUT/pyrandom_forgraph_output.478010.out

Ahora es en la parte donde se hace los graficos de histogramas https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/blob/main/Random%20Forest/DNA/MICROSET_PRUEBA/ERROR_OUTPUT/pyrandom_forgraph_output.478011.out

# 16 de junio del 2024
Finalmente se logro que el script funcionara, aqui se enuentra https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/blob/main/Random%20Forest/DNA/MICROSET_PRUEBA/RandomForest_addhist_logimp_python275.py

Comprobando que funciona tanto para el set de datos que son muchos nichos o dos nichos como maximo. El codigo, proximamente sera probado con el set de datos original, debido a que fue con datos locales de una base de datos de 10 genomas.

# 17 de junio del 2024 al 19 de junio del 2024
Se probo en el cluster y con el set dedatos original y funciono correctamente para ambos analisis. Tanto para la comparacion entre hospedero y ambiente, como para la comparacion de mamiferos y plantas.

# 6 de julio del 2024
Ahora se modificara la parte del script que recibe dos clasificaciones para que haga 4 graficas con 50 datos cada imagen y de ahi poderlos mostrar. A partir de https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/blob/main/Random%20Forest/Grafio_Confusion_RandomForest.py para entender y modificar el script original de DNA.

Se elimino esta parte del codigo, ya que daba otras medidas para poner las etiquetas
```
        positions2 = []
        for i, caracteristica in enumerate(caracteristicas):
            print(i, caracteristica)
            pos = [i * (bar_width * len(clusters) + 0.5) + j * bar_width for j in range(len(clusters))]
            print(pos)
            positions2.append(pos)
```
Y se agrego esta parte, modificando el inicio
```
else:
    # OPCION 11
    # UN HISTOGRAMA (dos filas)
    # Apilar los datos para combinarlos en una sola serie
    h3_o = pd.DataFrame(np.array([[i, j, zeroconteonichos.loc[i,j]] for j in zeroconteonichos.columns if j for i in zeroconteonichos.index if i]))
    h3_o.columns = ['Caracteristica', 'Cluster', 'Frecuencia']
    for i in [0, 50, 100, 150]:
        h3 = h3_o[i:i+50]
        
        # Crear el histograma
        plt.figure(figsize=(10, 4))
        clusters = h3['Cluster'].unique()
        caracteristicas = h3['Caracteristica'].unique()
        bar_width = 0.4  # Ajusta el ancho de las barras
```
Para hacer imagenes de 25 cluster por imagen, obteniendo 4 de ellas y teniendo una mejor observacion de los datos y etiquetas

Ahora solo falta corregir el porque se mueve el eje y, cambiando las posiciones de las frecuencias y agregar la parte de que aparezcan imagenes por separados y que no se sustituyan.

# 7 de julio del 2024 a 8 de julio del 2024
Finalmente el script se modifico, relizando 4 imagenes con 50 clusters y que con eso se le pudiese agregar con que se esta comparando, corrigiendo el orden del eje y y finalmente agregando de que color son las etiquetas.
```
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
        
        
        # Dibujar las barras
        for i, cluster in enumerate(clusters):
            cluster_data = h3[h3['Cluster'] == cluster]
            pos = [positions[j][i] for j in range(len(caracteristicas))]
            plt.bar(pos, pd.Series(int(i) for i in cluster_data['Frecuencia'] if i), width=bar_width, color=[colors[0],colors[1]])
    
        # Ajustar las posiciones del eje x y las etiquetas
        #flattened_positions = [p for sublist in positions2 for p in sublist]
        flattened_positions = [p for sublist in positions for p in sublist]
        x_labels = ['{}\nCluster {}'.format(caracteristicas[i], clusters[j]) for i in range(len(caracteristicas)) for j in range(len(clusters))]
        plt.xticks(flattened_positions, x_labels, rotation=90, fontsize=5, fontweight='bold')
        
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
        plt.title('Frecuencias por Característica y Clúster ({} y {})'.format(caracteristicas[0], caracteristicas[1]))
        #plt.show()
        # Ajustar el diseño para que no se recorten los elementos
        plt.tight_layout()
        # Guardar la gráfica como un archivo PNG
        plt.savefig(histt50labelspang, format='png', dpi=300, bbox_inches='tight')
        plt.close()
```

Finalmente tambien se modificaron las configuraciones de los graficos para la importancia de las caracteristicas
```
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
```
Finalmente toca adaptar en el cluster, correr con el pequeño subconjunto y finalmente con los datos originales.
https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/blob/main/Random%20Forest/Grafio_Confusion_RandomForest.py

# 25 de julio del 2024
Hasta el dia hoy hay dos script de python que corren un modelo de random forest, el cual uno era para windows, que esta en version 3.8, despues de actualizar de la 2.7.5 y ahora se implementa codigo y modificaciones para python 3.10. Para este punto la lectura de las frecuencias para ser modificadas, no estaban siendo recopiladas correctmente, es asi que se decidio mejorar, señalado los cambios con (<----)
```
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
        y_min, y_max = 0, int(max(h3['Frecuencia']))# + 200
        print(h3)
        histot_50=f"test_histograma_t50labels_{i}.png"
        histt50labelspang = os.path.join(imgrutabase, histot_50)
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
        
        # Dibujar las barras
        for i, cluster in enumerate(clusters):
            cluster_data = h3[h3['Cluster'] == cluster]
            print(cluster_data)
            pos = [positions[j][i] for j in range(len(caracteristicas))]
            print(pos)
            print("hola")
            #values=pd.Series(int(m) for m in cluster_data['Frecuencia'] if m) <--------------------------------------
            values=cluster_data['Frecuencia'].astype(int).tolist() # Esta modificacion se da, porque la anterior si funciona en python 3.8, pero ya en 3.10 ya no. <-----------------------------------------
            print(values)
            plt.bar(pos, values, width=bar_width, color=[colors[0],colors[1]])
```
Por lo que ahora se leen correctamente las frecuencias.

# 26 de julio del 2024 - 27 de julio del 2024
Se añadio, en el script de prueba con el microset de datos en DNA, (MicroSetRANDOMFOREST/RandomForest_python3.8_tmp.py), la parte de la permutacion de los datos, inmediatamente salieron los graficos y tablas esperadas para la permutacion. Se intento correr 3 veces, una se cancelo manualmente "pyrandomforestpy3.8_output.488633.out", la otra se interrumpio por un error "pyrandomforestpy3.8_output.488634.out" y finalmente la ultima termino exitosamente "pyrandomforestpy3.8_output.488663.out" con un total de ~7 horas para un set de 6 genomas.

```
from sklearn.inspection import permutation_importance
.
.
.
permutacion= "test_permutation_importance.png"
permutacion_csv="test_top_100_importances.csv"
.
.
.
importance_permutation = os.path.join(imgrutabase, permutacion)
importance_permutation_csv = os.path.join(imgrutabase, permutacion_csv)
.
.
.
print("Extrayendo la importancia por permutacion")
# Calcular la importancia por permutación
r = permutation_importance(rf, test_mtz_class_caracteres, test_labels, n_repeats=20, random_state=99, n_jobs=30)
# Convertir las importancias a un DataFrame
importances_df = pd.DataFrame({
    'feature': test_mtz_class_caracteres.columns,
    'importance_mean': r.importances_mean,
    'importance_std': r.importances_std
})
# Ordenar las importancias de mayor a menor
importances_df = importances_df.sort_values(by='importance_mean', ascending=False)
# Seleccionar las 100 características más importantes
top_100_importances = importances_df.head(100)
# Guardar los datos en un archivo CSV
top_100_importances.to_csv(importance_permutation_csv, index=False)

# Graficar las importancias
plt.figure(figsize=(14, 10))
plt.barh(top_100_importances['feature'], top_100_importances['importance_mean'], xerr=top_100_importances['importance_std'])
plt.xlabel('Importancia')
plt.ylabel('Características')
plt.title('Top 100 características más importantes')
plt.gca().invert_yaxis()  # Invertir el eje y para que las características más importantes estén en la parte superior
# Rotar las etiquetas del eje y para una mejor legibilidad
plt.yticks(rotation=0, fontsize=7)
plt.tight_layout()
# Guardar la gráfica como un archivo PNG
plt.savefig(importance_permutation, format='png', dpi=300, bbox_inches='tight')
```

